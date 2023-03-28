# -*- coding: utf-8 -*-
"""
Rotation routines backported from obspy/obspy#1310
"""
import warnings

import numpy as np

from obspy import UTCDateTime


def _get_common_channels_info(self):
    """
    Returns a dictionary with information on common channels.
    """
    # get all ids down to location code
    ids_ = set([tr.id.rsplit(".", 1)[0] for tr in self])
    all_channels = {}
    # work can be separated by net.sta.loc, so iterate over each
    for id_ in ids_:
        net, sta, loc = id_.split(".")
        channels = {}
        st_ = self.select(network=net, station=sta, location=loc)
        # for each individual channel collect earliest start time and
        # latest endtime
        for tr in st_:
            cha = tr.stats.channel
            cha_common = cha and cha[:-1] or None
            cha_common_dict = channels.setdefault(cha_common, {})
            cha_dict = cha_common_dict.setdefault(cha, {})
            cha_dict["start"] = min(tr.stats.starttime.timestamp,
                                    cha_dict.get("start", np.inf))
            cha_dict["end"] = max(tr.stats.endtime.timestamp,
                                  cha_dict.get("end", -np.inf))
        # convert all timestamp objects back to UTCDateTime
        for cha_common_dict in channels.values():
            for cha_dict in cha_common_dict.values():
                cha_dict["start"] = UTCDateTime(cha_dict["start"])
                cha_dict["end"] = UTCDateTime(cha_dict["end"])
        # now for every combination of common channels determine earliest
        # common start time and latest common end time, as well as gap
        # information in between
        for cha_common, channels_ in channels.items():
            if cha_common is None:
                cha_pattern = ""
            else:
                cha_pattern = cha_common + "?"
            st__ = self.select(network=net, station=sta, location=loc,
                               channel=cha_pattern)
            start = max(
                [cha_dict_["start"] for cha_dict_ in channels_.values()])
            end = min(
                [cha_dict_["end"] for cha_dict_ in channels_.values()])
            gaps = st__.get_gaps()
            all_channels[(net, sta, loc, cha_pattern)] = {
                "start": start, "end": end, "gaps": gaps,
                "channels": channels_}
    return all_channels


def _trim_common_channels(self):
    """
    Trim all channels that have the same ID down to the component character
    to the earliest common start time and latest common end time. Works in
    place.
    """
    self._cleanup()
    channel_infos = _get_common_channels_info(self)
    new_traces = []
    for (net, sta, loc, cha_pattern), infos in channel_infos.items():
        st = self.select(network=net, station=sta, location=loc,
                         channel=cha_pattern)
        st.trim(infos["start"], infos["end"])
        for _, _, _, _, start_, end_, _, _ in infos["gaps"]:
            st = st.cutout(start_, end_)
        new_traces += st.traces
    self.traces = new_traces
    return self


def _get_channel_metadata_from_network(net, seed_id, datetime=None):
    """
    Return basic metadata for a given channel.

    :type seed_id: str
    :param seed_id: SEED ID string of channel to get metadata for.
    :type datetime: :class:`~obspy.core.utcdatetime.UTCDateTime`, optional
    :param datetime: Time to get metadata for.
    :rtype: dict
    :return: Dictionary containing coordinates and orientation (latitude,
        longitude, elevation, azimuth, dip)
    """
    network, station, location, channel = seed_id.split(".")
    metadata = []
    if net.code != network:
        pass
    elif net.start_date and net.start_date > datetime:
        pass
    elif net.end_date and net.end_date < datetime:
        pass
    else:
        for sta in net.stations:
            # skip wrong station
            if sta.code != station:
                continue
            # check datetime only if given
            if datetime:
                # skip if start date before given datetime
                if sta.start_date and sta.start_date > datetime:
                    continue
                # skip if end date before given datetime
                if sta.end_date and sta.end_date < datetime:
                    continue
            for cha in sta.channels:
                # skip wrong channel
                if cha.code != channel:
                    continue
                # skip wrong location
                if cha.location_code != location:
                    continue
                # check datetime only if given
                if datetime:
                    # skip if start date before given datetime
                    if cha.start_date and cha.start_date > datetime:
                        continue
                    # skip if end date before given datetime
                    if cha.end_date and cha.end_date < datetime:
                        continue
                # prepare coordinates
                data = {}
                # if channel latitude or longitude is not given use station
                data['latitude'] = cha.latitude or sta.latitude
                data['longitude'] = cha.longitude or sta.longitude
                data['elevation'] = cha.elevation or sta.elevation
                data['local_depth'] = cha.depth
                data['azimuth'] = cha.azimuth
                data['dip'] = cha.dip
                metadata.append(data)
    if len(metadata) > 1:
        msg = ("Found more than one matching channel metadata. "
               "Returning first.")
        warnings.warn(msg)
    elif len(metadata) < 1:
        msg = "No matching channel metadata found."
        raise Exception(msg)
    return metadata[0]


def _get_channel_metadata_from_inventory(inventory, seed_id, datetime=None):
    """
    Return basic metadata for a given channel.

    :type seed_id: str
    :param seed_id: SEED ID string of channel to get metadata for.
    :type datetime: :class:`~obspy.core.utcdatetime.UTCDateTime`, optional
    :param datetime: Time to get metadata for.
    :rtype: dict
    :return: Dictionary containing coordinates and orientation (latitude,
        longitude, elevation, azimuth, dip)
    """
    network, _, _, _ = seed_id.split(".")

    metadata = []
    for net in inventory.networks:
        if net.code != network:
            continue
        try:
            metadata.append(
                _get_channel_metadata_from_network(net, seed_id, datetime))
        except:
            pass
    if len(metadata) > 1:
        msg = ("Found more than one matching channel metadata. "
               "Returning first.")
        warnings.warn(msg)
    elif len(metadata) < 1:
        msg = "No matching channel metadata found."
        raise Exception(msg)
    return metadata[0]


def get_orientation(inventory, seed_id, datetime=None):
    """
    Return orientation for a given channel.

    >>> from obspy import read_inventory, UTCDateTime
    >>> inv = read_inventory()
    >>> t = UTCDateTime("2015-01-01")
    >>> inv.get_orientation("GR.FUR..LHE", t)  # doctest: +SKIP
    {'azimuth': 90.0,
     'dip': 0.0}

    :type seed_id: str
    :param seed_id: SEED ID string of channel to get orientation for.
    :type datetime: :class:`~obspy.core.utcdatetime.UTCDateTime`, optional
    :param datetime: Time to get orientation for.
    :rtype: dict
    :return: Dictionary containing orientation (azimuth, dip).
    """
    metadata = _get_channel_metadata_from_inventory(
        inventory, seed_id, datetime)
    orientation = {}
    for key in ['azimuth', 'dip']:
        orientation[key] = metadata[key]
    return orientation
