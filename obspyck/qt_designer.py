# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from .util import QMplCanvas
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qMainWindow_obsPyck(object):
    def setupUi(self, qMainWindow_obsPyck):
        qMainWindow_obsPyck.setObjectName("qMainWindow_obsPyck")
        qMainWindow_obsPyck.resize(1281, 789)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            qMainWindow_obsPyck.sizePolicy().hasHeightForWidth())
        qMainWindow_obsPyck.setSizePolicy(sizePolicy)
        qMainWindow_obsPyck.setMaximumSize(QtCore.QSize(2000, 2000))
        qMainWindow_obsPyck.setBaseSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        qMainWindow_obsPyck.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("obspyck.gif"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qMainWindow_obsPyck.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(qMainWindow_obsPyck)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.qSplitter_vertical = QtWidgets.QSplitter(self.centralwidget)
        self.qSplitter_vertical.setOrientation(QtCore.Qt.Vertical)
        self.qSplitter_vertical.setHandleWidth(8)
        self.qSplitter_vertical.setObjectName("qSplitter_vertical")
        self.qSplitter_horizontal = QtWidgets.QSplitter(
            self.qSplitter_vertical)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qSplitter_horizontal.sizePolicy().hasHeightForWidth())
        self.qSplitter_horizontal.setSizePolicy(sizePolicy)
        self.qSplitter_horizontal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qSplitter_horizontal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qSplitter_horizontal.setOrientation(QtCore.Qt.Horizontal)
        self.qSplitter_horizontal.setHandleWidth(8)
        self.qSplitter_horizontal.setObjectName("qSplitter_horizontal")
        self.layoutWidgetxx = QtWidgets.QWidget(self.qSplitter_horizontal)
        self.layoutWidgetxx.setObjectName("layoutWidgetxx")
        self.leftVerticalLayout = QtWidgets.QVBoxLayout(self.layoutWidgetxx)
        self.leftVerticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMinAndMaxSize)
        self.leftVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftVerticalLayout.setSpacing(0)
        self.leftVerticalLayout.setObjectName("leftVerticalLayout")
        self.qToolButton_clearAll = QtWidgets.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_clearAll.sizePolicy().hasHeightForWidth())
        self.qToolButton_clearAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.qToolButton_clearAll.setFont(font)
        self.qToolButton_clearAll.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_clearAll.setStyleSheet("")
        self.qToolButton_clearAll.setCheckable(False)
        self.qToolButton_clearAll.setObjectName("qToolButton_clearAll")
        self.leftVerticalLayout.addWidget(self.qToolButton_clearAll)
        self.qToolButton_clearOrigMag = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_clearOrigMag.sizePolicy().hasHeightForWidth())
        self.qToolButton_clearOrigMag.setSizePolicy(sizePolicy)
        self.qToolButton_clearOrigMag.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_clearOrigMag.setObjectName("qToolButton_clearOrigMag")
        self.leftVerticalLayout.addWidget(self.qToolButton_clearOrigMag)
        self.qToolButton_clearFocMec = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_clearFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_clearFocMec.setSizePolicy(sizePolicy)
        self.qToolButton_clearFocMec.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_clearFocMec.setObjectName("qToolButton_clearFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_clearFocMec)
        spacerItem = QtWidgets.QSpacerItem(
            170, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem)
        self.qToolButton_doGridSearch = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_doGridSearch.sizePolicy().hasHeightForWidth())
        self.qToolButton_doGridSearch.setSizePolicy(sizePolicy)
        self.qToolButton_doGridSearch.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_doGridSearch.setObjectName("qToolButton_doGridSearch")
        self.leftVerticalLayout.addWidget(self.qToolButton_doGridSearch)
        self.qToolButton_doGridSearch.clicked.connect(self.do_grid_search)
        self.qToolButton_doHyp2000 = QtWidgets.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_doHyp2000.sizePolicy().hasHeightForWidth())
        self.qToolButton_doHyp2000.setSizePolicy(sizePolicy)
        self.qToolButton_doHyp2000.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_doHyp2000.setObjectName("qToolButton_doHyp2000")
        self.leftVerticalLayout.addWidget(self.qToolButton_doHyp2000)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.qToolButton_doNlloc = QtWidgets.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_doNlloc.sizePolicy().hasHeightForWidth())
        self.qToolButton_doNlloc.setSizePolicy(sizePolicy)
        self.qToolButton_doNlloc.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_doNlloc.setObjectName("qToolButton_doNlloc")
        self.horizontalLayout_3.addWidget(self.qToolButton_doNlloc)
        self.qComboBox_nllocModel = QtWidgets.QComboBox(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qComboBox_nllocModel.sizePolicy().hasHeightForWidth())
        self.qComboBox_nllocModel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.qComboBox_nllocModel.setFont(font)
        self.qComboBox_nllocModel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qComboBox_nllocModel.setStyleSheet("")
        self.qComboBox_nllocModel.setObjectName("qComboBox_nllocModel")
        self.qComboBox_nllocModel.addItem("")
        self.qComboBox_nllocModel.addItem("")
        self.qComboBox_nllocModel.addItem("")
        self.horizontalLayout_3.addWidget(self.qComboBox_nllocModel)
        self.leftVerticalLayout.addLayout(self.horizontalLayout_3)
        self.qToolButton_doFocMec = QtWidgets.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_doFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_doFocMec.setSizePolicy(sizePolicy)
        self.qToolButton_doFocMec.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_doFocMec.setObjectName("qToolButton_doFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_doFocMec)
        spacerItem1 = QtWidgets.QSpacerItem(
            170, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem1)
        self.qToolButton_showMap = QtWidgets.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_showMap.sizePolicy().hasHeightForWidth())
        self.qToolButton_showMap.setSizePolicy(sizePolicy)
        self.qToolButton_showMap.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_showMap.setCheckable(True)
        self.qToolButton_showMap.setObjectName("qToolButton_showMap")
        self.leftVerticalLayout.addWidget(self.qToolButton_showMap)
        self.qToolButton_showFocMec = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_showFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_showFocMec.setSizePolicy(sizePolicy)
        self.qToolButton_showFocMec.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_showFocMec.setCheckable(True)
        self.qToolButton_showFocMec.setObjectName("qToolButton_showFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_showFocMec)
        self.qToolButton_nextFocMec = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_nextFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_nextFocMec.setSizePolicy(sizePolicy)
        self.qToolButton_nextFocMec.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_nextFocMec.setObjectName("qToolButton_nextFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_nextFocMec)
        self.qToolButton_showWadati = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_showWadati.sizePolicy().hasHeightForWidth())
        self.qToolButton_showWadati.setSizePolicy(sizePolicy)
        self.qToolButton_showWadati.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_showWadati.setCheckable(True)
        self.qToolButton_showWadati.setObjectName("qToolButton_showWadati")
        self.leftVerticalLayout.addWidget(self.qToolButton_showWadati)
        spacerItem2 = QtWidgets.QSpacerItem(
            170, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem2)
        self.qToolButton_getNextEvent = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_getNextEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_getNextEvent.setSizePolicy(sizePolicy)
        self.qToolButton_getNextEvent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_getNextEvent.setObjectName("qToolButton_getNextEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_getNextEvent)
        self.qToolButton_updateEventList = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_updateEventList.sizePolicy().hasHeightForWidth())
        self.qToolButton_updateEventList.setSizePolicy(sizePolicy)
        self.qToolButton_updateEventList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_updateEventList.setObjectName(
            "qToolButton_updateEventList")
        self.leftVerticalLayout.addWidget(self.qToolButton_updateEventList)
        self.qToolButton_sendNewEvent = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_sendNewEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_sendNewEvent.setSizePolicy(sizePolicy)
        self.qToolButton_sendNewEvent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_sendNewEvent.setObjectName("qToolButton_sendNewEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_sendNewEvent)
        self.qToolButton_replaceEvent = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_replaceEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_replaceEvent.setSizePolicy(sizePolicy)
        self.qToolButton_replaceEvent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_replaceEvent.setObjectName("qToolButton_replaceEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_replaceEvent)
        self.qToolButton_deleteEvent = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_deleteEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_deleteEvent.setSizePolicy(sizePolicy)
        self.qToolButton_deleteEvent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_deleteEvent.setObjectName("qToolButton_deleteEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_deleteEvent)
        self.qToolButton_saveEventLocally = QtWidgets.QToolButton(
            self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_saveEventLocally.sizePolicy().hasHeightForWidth())
        self.qToolButton_saveEventLocally.setSizePolicy(sizePolicy)
        self.qToolButton_saveEventLocally.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_saveEventLocally.setObjectName(
            "qToolButton_saveEventLocally")
        self.leftVerticalLayout.addWidget(self.qToolButton_saveEventLocally)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.qCheckBox_public = QtWidgets.QCheckBox(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qCheckBox_public.sizePolicy().hasHeightForWidth())
        self.qCheckBox_public.setSizePolicy(sizePolicy)
        self.qCheckBox_public.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qCheckBox_public.setObjectName("qCheckBox_public")
        self.horizontalLayout_4.addWidget(self.qCheckBox_public)
        self.qComboBox_eventType = QtWidgets.QComboBox(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qComboBox_eventType.sizePolicy().hasHeightForWidth())
        self.qComboBox_eventType.setSizePolicy(sizePolicy)
        self.qComboBox_eventType.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qComboBox_eventType.setObjectName("qComboBox_eventType")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.qComboBox_eventType.addItem("")
        self.horizontalLayout_4.addWidget(self.qComboBox_eventType)
        self.leftVerticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            170, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leftVerticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.qLabel_x_rel = QtWidgets.QLabel(self.layoutWidgetxx)
        self.qLabel_x_rel.setObjectName("qLabel_x_rel")
        self.horizontalLayout_8.addWidget(self.qLabel_x_rel)
        self.qLabel_xdata_rel = QtWidgets.QLabel(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qLabel_xdata_rel.sizePolicy().hasHeightForWidth())
        self.qLabel_xdata_rel.setSizePolicy(sizePolicy)
        self.qLabel_xdata_rel.setMinimumSize(QtCore.QSize(50, 0))
        self.qLabel_xdata_rel.setBaseSize(QtCore.QSize(40, 0))
        self.qLabel_xdata_rel.setAutoFillBackground(False)
        self.qLabel_xdata_rel.setText("")
        self.qLabel_xdata_rel.setObjectName("qLabel_xdata_rel")
        self.horizontalLayout_8.addWidget(self.qLabel_xdata_rel)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.qLabel_y = QtWidgets.QLabel(self.layoutWidgetxx)
        self.qLabel_y.setObjectName("qLabel_y")
        self.horizontalLayout_7.addWidget(self.qLabel_y)
        self.qLabel_ydata = QtWidgets.QLabel(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qLabel_ydata.sizePolicy().hasHeightForWidth())
        self.qLabel_ydata.setSizePolicy(sizePolicy)
        self.qLabel_ydata.setMinimumSize(QtCore.QSize(25, 0))
        self.qLabel_ydata.setBaseSize(QtCore.QSize(40, 0))
        self.qLabel_ydata.setText("")
        self.qLabel_ydata.setObjectName("qLabel_ydata")
        self.horizontalLayout_7.addWidget(self.qLabel_ydata)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8b = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8b.setObjectName("horizontalLayout_8b")
        self.qLabel_x_abs = QtWidgets.QLabel(self.layoutWidgetxx)
        self.qLabel_x_abs.setObjectName("qLabel_x_abs")
        self.horizontalLayout_8b.addWidget(self.qLabel_x_abs)
        self.qLabel_xdata_abs = QtWidgets.QLabel(self.layoutWidgetxx)
        self.qLabel_xdata_abs.setMinimumSize(QtCore.QSize(160, 0))
        self.qLabel_xdata_abs.setText("")
        self.qLabel_xdata_abs.setObjectName("qLabel_xdata_abs")
        self.horizontalLayout_8b.addWidget(self.qLabel_xdata_abs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8b)
        self.leftVerticalLayout.addLayout(self.verticalLayout_2)
        self.qToolButton_debug = QtWidgets.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_debug.sizePolicy().hasHeightForWidth())
        self.qToolButton_debug.setSizePolicy(sizePolicy)
        self.qToolButton_debug.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_debug.setObjectName("qToolButton_debug")
        self.leftVerticalLayout.addWidget(self.qToolButton_debug)
        self.qWidget_mpl = QtWidgets.QWidget(self.qSplitter_horizontal)
        self.qWidget_mpl.setObjectName("qWidget_mpl")
        self.qVBoxLayout_mpl = QtWidgets.QVBoxLayout(self.qWidget_mpl)
        self.qVBoxLayout_mpl.setContentsMargins(0, 0, 0, 0)
        self.qVBoxLayout_mpl.setObjectName("qVBoxLayout_mpl")
        self.qMplCanvas = QMplCanvas(self.qWidget_mpl)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(
            self.qMplCanvas.sizePolicy().hasHeightForWidth())
        self.qMplCanvas.setSizePolicy(sizePolicy)
        self.qMplCanvas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.qMplCanvas.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.qMplCanvas.setMouseTracking(True)
        self.qMplCanvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.qMplCanvas.setObjectName("qMplCanvas")
        self.qVBoxLayout_mpl.addWidget(self.qMplCanvas)
        self.qSplitter_horizontal_new = QtWidgets.QSplitter(self.qWidget_mpl)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qSplitter_horizontal_new.sizePolicy().hasHeightForWidth())
        self.qSplitter_horizontal_new.setSizePolicy(sizePolicy)
        self.qSplitter_horizontal_new.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qSplitter_horizontal_new.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qSplitter_horizontal_new.setOrientation(QtCore.Qt.Horizontal)
        self.qSplitter_horizontal_new.setHandleWidth(8)
        self.qSplitter_horizontal_new.setObjectName("qSplitter_horizontal_new")
        self.xxx = QtWidgets.QWidget(self.qSplitter_horizontal_new)
        self.xxx.setObjectName("xxx")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.xxx)
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.qToolButton_sort_abc = QtWidgets.QToolButton(self.xxx)
        self.qToolButton_sort_abc.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_sort_abc.setObjectName("qToolButton_sort_abc")
        self.verticalLayout_6.addWidget(self.qToolButton_sort_abc)
        self.qToolButton_sort_distance = QtWidgets.QToolButton(self.xxx)
        self.qToolButton_sort_distance.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_sort_distance.setObjectName(
            "qToolButton_sort_distance")
        self.verticalLayout_6.addWidget(self.qToolButton_sort_distance)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.VerticalLayout = QtWidgets.QVBoxLayout()
        self.VerticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.VerticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.VerticalLayout.setSpacing(6)
        self.VerticalLayout.setObjectName("VerticalLayout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.qToolButton_previousStream = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_previousStream.sizePolicy().hasHeightForWidth())
        self.qToolButton_previousStream.setSizePolicy(sizePolicy)
        self.qToolButton_previousStream.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_previousStream.setArrowType(QtCore.Qt.LeftArrow)
        self.qToolButton_previousStream.setObjectName(
            "qToolButton_previousStream")
        self.horizontalLayout_13.addWidget(self.qToolButton_previousStream)
        self.qLabel_streamNumber = QtWidgets.QLabel(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qLabel_streamNumber.sizePolicy().hasHeightForWidth())
        self.qLabel_streamNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.qLabel_streamNumber.setFont(font)
        self.qLabel_streamNumber.setStyleSheet("")
        self.qLabel_streamNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.qLabel_streamNumber.setObjectName("qLabel_streamNumber")
        self.horizontalLayout_13.addWidget(self.qLabel_streamNumber)
        self.qToolButton_nextStream = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_nextStream.sizePolicy().hasHeightForWidth())
        self.qToolButton_nextStream.setSizePolicy(sizePolicy)
        self.qToolButton_nextStream.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_nextStream.setArrowType(QtCore.Qt.RightArrow)
        self.qToolButton_nextStream.setObjectName("qToolButton_nextStream")
        self.horizontalLayout_13.addWidget(self.qToolButton_nextStream)
        self.VerticalLayout.addLayout(self.horizontalLayout_13)
        self.qComboBox_streamName = QtWidgets.QComboBox(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qComboBox_streamName.sizePolicy().hasHeightForWidth())
        self.qComboBox_streamName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.qComboBox_streamName.setFont(font)
        self.qComboBox_streamName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qComboBox_streamName.setStyleSheet("")
        self.qComboBox_streamName.setObjectName("qComboBox_streamName")
        self.VerticalLayout.addWidget(self.qComboBox_streamName)
        self.horizontalLayout_6.addLayout(self.VerticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.qToolButton_overview = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_overview.sizePolicy().hasHeightForWidth())
        self.qToolButton_overview.setSizePolicy(sizePolicy)
        self.qToolButton_overview.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_overview.setCheckable(True)
        self.qToolButton_overview.setObjectName("qToolButton_overview")
        self.verticalLayout_3.addWidget(self.qToolButton_overview)
        self.qComboBox_phaseType = QtWidgets.QComboBox(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qComboBox_phaseType.sizePolicy().hasHeightForWidth())
        self.qComboBox_phaseType.setSizePolicy(sizePolicy)
        self.qComboBox_phaseType.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qComboBox_phaseType.setObjectName("qComboBox_phaseType")
        self.verticalLayout_3.addWidget(self.qComboBox_phaseType)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(
            1, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout_9aa = QtWidgets.QVBoxLayout()
        self.verticalLayout_9aa.setObjectName("verticalLayout_9aa")
        self.horizontalLayout_16aa = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16aa.setObjectName("horizontalLayout_16aa")
        self.qToolButton_physical_units = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_physical_units.sizePolicy().hasHeightForWidth())
        self.qToolButton_physical_units.setSizePolicy(sizePolicy)
        self.qToolButton_physical_units.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_physical_units.setCheckable(True)
        self.qToolButton_physical_units.setObjectName(
            "qToolButton_physical_units")
        self.horizontalLayout_16aa.addWidget(self.qToolButton_physical_units)
        self.verticalLayout_9aa.addLayout(self.horizontalLayout_16aa)
        self.horizontalLayout_14aa = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14aa.setObjectName("horizontalLayout_14aa")
        self.qLabel_waterlevel = QtWidgets.QLabel(self.xxx)
        self.qLabel_waterlevel.setObjectName("qLabel_waterlevel")
        self.horizontalLayout_14aa.addWidget(self.qLabel_waterlevel)
        self.qDoubleSpinBox_waterlevel = QtWidgets.QDoubleSpinBox(self.xxx)
        self.qDoubleSpinBox_waterlevel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_waterlevel.setDecimals(0)
        self.qDoubleSpinBox_waterlevel.setMaximum(1000.0)
        self.qDoubleSpinBox_waterlevel.setSingleStep(5.0)
        self.qDoubleSpinBox_waterlevel.setProperty("value", 20.0)
        self.qDoubleSpinBox_waterlevel.setObjectName(
            "qDoubleSpinBox_waterlevel")
        self.horizontalLayout_14aa.addWidget(self.qDoubleSpinBox_waterlevel)
        self.verticalLayout_9aa.addLayout(self.horizontalLayout_14aa)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9aa)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.qToolButton_filter = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_filter.sizePolicy().hasHeightForWidth())
        self.qToolButton_filter.setSizePolicy(sizePolicy)
        self.qToolButton_filter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_filter.setCheckable(True)
        self.qToolButton_filter.setObjectName("qToolButton_filter")
        self.horizontalLayout_17.addWidget(self.qToolButton_filter)
        self.qToolButton_rotateLQT = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_rotateLQT.sizePolicy().hasHeightForWidth())
        self.qToolButton_rotateLQT.setSizePolicy(sizePolicy)
        self.qToolButton_rotateLQT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_rotateLQT.setCheckable(True)
        self.qToolButton_rotateLQT.setObjectName("qToolButton_rotateLQT")
        self.horizontalLayout_17.addWidget(self.qToolButton_rotateLQT)
        self.qToolButton_rotateZRT = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_rotateZRT.sizePolicy().hasHeightForWidth())
        self.qToolButton_rotateZRT.setSizePolicy(sizePolicy)
        self.qToolButton_rotateZRT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_rotateZRT.setCheckable(True)
        self.qToolButton_rotateZRT.setObjectName("qToolButton_rotateZRT")
        self.horizontalLayout_17.addWidget(self.qToolButton_rotateZRT)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.qToolButton_trigger = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_trigger.sizePolicy().hasHeightForWidth())
        self.qToolButton_trigger.setSizePolicy(sizePolicy)
        self.qToolButton_trigger.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_trigger.setCheckable(True)
        self.qToolButton_trigger.setObjectName("qToolButton_trigger")
        self.horizontalLayout_15.addWidget(self.qToolButton_trigger)
        self.qToolButton_arpicker = QtWidgets.QToolButton(self.xxx)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qToolButton_arpicker.sizePolicy().hasHeightForWidth())
        self.qToolButton_arpicker.setSizePolicy(sizePolicy)
        self.qToolButton_arpicker.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_arpicker.setArrowType(QtCore.Qt.NoArrow)
        self.qToolButton_arpicker.setObjectName("qToolButton_arpicker")
        self.horizontalLayout_15.addWidget(self.qToolButton_arpicker)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(
            1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.qLabel_sta = QtWidgets.QLabel(self.xxx)
        self.qLabel_sta.setObjectName("qLabel_sta")
        self.horizontalLayout_16.addWidget(self.qLabel_sta)
        self.qDoubleSpinBox_sta = QtWidgets.QDoubleSpinBox(self.xxx)
        self.qDoubleSpinBox_sta.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_sta.setSingleStep(0.1)
        self.qDoubleSpinBox_sta.setProperty("value", 0.5)
        self.qDoubleSpinBox_sta.setObjectName("qDoubleSpinBox_sta")
        self.horizontalLayout_16.addWidget(self.qDoubleSpinBox_sta)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.qLabel_lta = QtWidgets.QLabel(self.xxx)
        self.qLabel_lta.setObjectName("qLabel_lta")
        self.horizontalLayout_14.addWidget(self.qLabel_lta)
        self.qDoubleSpinBox_lta = QtWidgets.QDoubleSpinBox(self.xxx)
        self.qDoubleSpinBox_lta.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_lta.setProperty("value", 10.0)
        self.qDoubleSpinBox_lta.setObjectName("qDoubleSpinBox_lta")
        self.horizontalLayout_14.addWidget(self.qDoubleSpinBox_lta)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        spacerItem6 = QtWidgets.QSpacerItem(
            1, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_12)
        spacerItem7 = QtWidgets.QSpacerItem(
            1, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.qVBoxLayout_mpl.addWidget(self.qSplitter_horizontal_new)
        self.qSplitter_horizontal_new2 = QtWidgets.QSplitter(self.qWidget_mpl)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qSplitter_horizontal_new2.sizePolicy().hasHeightForWidth())
        self.qSplitter_horizontal_new2.setSizePolicy(sizePolicy)
        self.qSplitter_horizontal_new2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qSplitter_horizontal_new2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qSplitter_horizontal_new2.setOrientation(QtCore.Qt.Horizontal)
        self.qSplitter_horizontal_new2.setHandleWidth(8)
        self.qSplitter_horizontal_new2.setObjectName(
            "qSplitter_horizontal_new2")
        self.yyy = QtWidgets.QWidget(self.qSplitter_horizontal_new2)
        self.yyy.setObjectName("yyy")
        self.horizontalLayout_2b = QtWidgets.QHBoxLayout(self.yyy)
        self.horizontalLayout_2b.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2b.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2b.setSpacing(6)
        self.horizontalLayout_2b.setObjectName("horizontalLayout_2b")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.qComboBox_filterType = QtWidgets.QComboBox(self.yyy)
        self.qComboBox_filterType.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qComboBox_filterType.setObjectName("qComboBox_filterType")
        self.qComboBox_filterType.addItem("")
        self.qComboBox_filterType.addItem("")
        self.qComboBox_filterType.addItem("")
        self.qComboBox_filterType.addItem("")
        self.horizontalLayout_11.addWidget(self.qComboBox_filterType)
        self.qCheckBox_zerophase = QtWidgets.QCheckBox(self.yyy)
        self.qCheckBox_zerophase.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qCheckBox_zerophase.setObjectName("qCheckBox_zerophase")
        self.horizontalLayout_11.addWidget(self.qCheckBox_zerophase)
        self.qCheckBox_50Hz = QtWidgets.QCheckBox(self.yyy)
        self.qCheckBox_50Hz.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qCheckBox_50Hz.setObjectName("qCheckBox_50Hz")
        self.horizontalLayout_11.addWidget(self.qCheckBox_50Hz)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.qLabel_corners = QtWidgets.QLabel(self.yyy)
        self.qLabel_corners.setObjectName("qLabel_corners")
        self.horizontalLayout_10.addWidget(self.qLabel_corners)
        self.qDoubleSpinBox_corners = QtWidgets.QDoubleSpinBox(self.yyy)
        self.qDoubleSpinBox_corners.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qDoubleSpinBox_corners.setDecimals(0)
        self.qDoubleSpinBox_corners.setMinimum(1.0)
        self.qDoubleSpinBox_corners.setMaximum(8.0)
        self.qDoubleSpinBox_corners.setProperty("value", 1.0)
        self.qDoubleSpinBox_corners.setObjectName("qDoubleSpinBox_corners")
        self.horizontalLayout_10.addWidget(self.qDoubleSpinBox_corners)
        self.qLabel_lowpass = QtWidgets.QLabel(self.yyy)
        self.qLabel_lowpass.setObjectName("qLabel_lowpass")
        self.horizontalLayout_10.addWidget(self.qLabel_lowpass)
        self.qDoubleSpinBox_highpass = QtWidgets.QDoubleSpinBox(self.yyy)
        self.qDoubleSpinBox_highpass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_highpass.setAcceptDrops(False)
        self.qDoubleSpinBox_highpass.setMinimum(0.01)
        self.qDoubleSpinBox_highpass.setSingleStep(0.5)
        self.qDoubleSpinBox_highpass.setProperty("value", 1.0)
        self.qDoubleSpinBox_highpass.setObjectName("qDoubleSpinBox_highpass")
        self.horizontalLayout_10.addWidget(self.qDoubleSpinBox_highpass)
        self.qLabel_highpass = QtWidgets.QLabel(self.yyy)
        self.qLabel_highpass.setObjectName("qLabel_highpass")
        self.horizontalLayout_10.addWidget(self.qLabel_highpass)
        self.qDoubleSpinBox_lowpass = QtWidgets.QDoubleSpinBox(self.yyy)
        self.qDoubleSpinBox_lowpass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_lowpass.setMinimum(0.01)
        self.qDoubleSpinBox_lowpass.setProperty("value", 20.0)
        self.qDoubleSpinBox_lowpass.setObjectName("qDoubleSpinBox_lowpass")
        self.horizontalLayout_10.addWidget(self.qDoubleSpinBox_lowpass)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2b.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6x = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6x.setObjectName("horizontalLayout_6x")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.qToolButton_spectrogram = QtWidgets.QToolButton(self.yyy)
        self.qToolButton_spectrogram.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qToolButton_spectrogram.setCheckable(True)
        self.qToolButton_spectrogram.setObjectName("qToolButton_spectrogram")
        self.horizontalLayout_18.addWidget(self.qToolButton_spectrogram)
        self.qCheckBox_spectrogramLog = QtWidgets.QCheckBox(self.yyy)
        self.qCheckBox_spectrogramLog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qCheckBox_spectrogramLog.setObjectName("qCheckBox_spectrogramLog")
        self.horizontalLayout_18.addWidget(self.qCheckBox_spectrogramLog)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.qLabel_wlen = QtWidgets.QLabel(self.yyy)
        self.qLabel_wlen.setObjectName("qLabel_wlen")
        self.horizontalLayout_19.addWidget(self.qLabel_wlen)
        self.qDoubleSpinBox_wlen = QtWidgets.QDoubleSpinBox(self.yyy)
        self.qDoubleSpinBox_wlen.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_wlen.setSuffix("")
        self.qDoubleSpinBox_wlen.setMinimum(0.1)
        self.qDoubleSpinBox_wlen.setMaximum(99.99)
        self.qDoubleSpinBox_wlen.setSingleStep(0.1)
        self.qDoubleSpinBox_wlen.setProperty("value", 0.4)
        self.qDoubleSpinBox_wlen.setObjectName("qDoubleSpinBox_wlen")
        self.horizontalLayout_19.addWidget(self.qDoubleSpinBox_wlen)
        self.qLabel_perlap = QtWidgets.QLabel(self.yyy)
        self.qLabel_perlap.setObjectName("qLabel_perlap")
        self.horizontalLayout_19.addWidget(self.qLabel_perlap)
        self.qDoubleSpinBox_perlap = QtWidgets.QDoubleSpinBox(self.yyy)
        self.qDoubleSpinBox_perlap.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qDoubleSpinBox_perlap.setMaximum(0.99)
        self.qDoubleSpinBox_perlap.setSingleStep(0.05)
        self.qDoubleSpinBox_perlap.setProperty("value", 0.9)
        self.qDoubleSpinBox_perlap.setObjectName("qDoubleSpinBox_perlap")
        self.horizontalLayout_19.addWidget(self.qDoubleSpinBox_perlap)
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_6x.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2b.addLayout(self.horizontalLayout_6x)
        spacerItem8 = QtWidgets.QSpacerItem(
            1, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2b.addItem(spacerItem8)
        self.qVBoxLayout_mpl.addWidget(self.qSplitter_horizontal_new2)
        self.verticalLayoutWidget = QtWidgets.QWidget(
            self.qSplitter_horizontal)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.rightVerticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.rightVerticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.rightVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rightVerticalLayout.setSpacing(0)
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.qTextEdit_qml = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.qTextEdit_qml.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qTextEdit_qml.sizePolicy().hasHeightForWidth())
        self.qTextEdit_qml.setSizePolicy(sizePolicy)
        self.qTextEdit_qml.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.qTextEdit_qml.setFont(font)
        self.qTextEdit_qml.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qTextEdit_qml.setAcceptDrops(False)
        self.qTextEdit_qml.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.qTextEdit_qml.setReadOnly(True)
        self.qTextEdit_qml.setObjectName("qTextEdit_qml")
        self.rightVerticalLayout.addWidget(self.qTextEdit_qml)
        self.qPushButton_qml_update = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.qPushButton_qml_update.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qPushButton_qml_update.setObjectName("qPushButton_qml_update")
        self.rightVerticalLayout.addWidget(self.qPushButton_qml_update)
        self.layoutWidget = QtWidgets.QWidget(self.qSplitter_vertical)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qPlainTextEdit_stdout = QtWidgets.QPlainTextEdit(
            self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qPlainTextEdit_stdout.sizePolicy().hasHeightForWidth())
        self.qPlainTextEdit_stdout.setSizePolicy(sizePolicy)
        self.qPlainTextEdit_stdout.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.qPlainTextEdit_stdout.setFont(font)
        self.qPlainTextEdit_stdout.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qPlainTextEdit_stdout.setAcceptDrops(False)
        self.qPlainTextEdit_stdout.setUndoRedoEnabled(False)
        self.qPlainTextEdit_stdout.setReadOnly(True)
        self.qPlainTextEdit_stdout.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.qPlainTextEdit_stdout.setObjectName("qPlainTextEdit_stdout")
        self.horizontalLayout.addWidget(self.qPlainTextEdit_stdout)
        self.qPlainTextEdit_stderr = QtWidgets.QPlainTextEdit(
            self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qPlainTextEdit_stderr.sizePolicy().hasHeightForWidth())
        self.qPlainTextEdit_stderr.setSizePolicy(sizePolicy)
        self.qPlainTextEdit_stderr.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.qPlainTextEdit_stderr.setFont(font)
        self.qPlainTextEdit_stderr.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qPlainTextEdit_stderr.setAcceptDrops(False)
        self.qPlainTextEdit_stderr.setUndoRedoEnabled(False)
        self.qPlainTextEdit_stderr.setReadOnly(True)
        self.qPlainTextEdit_stderr.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.qPlainTextEdit_stderr.setObjectName("qPlainTextEdit_stderr")
        self.horizontalLayout.addWidget(self.qPlainTextEdit_stderr)
        self.verticalLayout.addWidget(self.qSplitter_vertical)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        qMainWindow_obsPyck.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(qMainWindow_obsPyck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 26))
        self.menubar.setObjectName("menubar")
        qMainWindow_obsPyck.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(qMainWindow_obsPyck)
        self.statusbar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        qMainWindow_obsPyck.setStatusBar(self.statusbar)

        self.retranslateUi(qMainWindow_obsPyck)
        self.qComboBox_eventType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow_obsPyck)

    def retranslateUi(self, qMainWindow_obsPyck):
        _translate = QtCore.QCoreApplication.translate
        qMainWindow_obsPyck.setWindowTitle(
            _translate("qMainWindow_obsPyck", "ObsPyck"))
        self.qToolButton_clearAll.setText(
            _translate("qMainWindow_obsPyck", "clear All"))
        self.qToolButton_clearOrigMag.setText(
            _translate("qMainWindow_obsPyck", "clear Orig&&Mag"))
        self.qToolButton_clearFocMec.setText(
            _translate("qMainWindow_obsPyck", "clear FocMec"))
        self.qToolButton_doGridSearch.setText(
            _translate("qMainWindow_obsPyck", "Do Grid Search"))
        self.qToolButton_doHyp2000.setText(
            _translate("qMainWindow_obsPyck", "do hyp2000"))
        self.qToolButton_doNlloc.setText(
            _translate("qMainWindow_obsPyck", "do NLLoc"))
        self.qComboBox_nllocModel.setItemText(
            0, _translate("qMainWindow_obsPyck", "BY"))
        self.qComboBox_nllocModel.setItemText(
            1, _translate("qMainWindow_obsPyck", "RH"))
        self.qComboBox_nllocModel.setItemText(
            2, _translate("qMainWindow_obsPyck", "UH"))
        self.qToolButton_doFocMec.setText(
            _translate("qMainWindow_obsPyck", "do focmec"))
        self.qToolButton_showMap.setText(
            _translate("qMainWindow_obsPyck", "show Map"))
        self.qToolButton_showFocMec.setText(
            _translate("qMainWindow_obsPyck", "show FocMec"))
        self.qToolButton_nextFocMec.setText(
            _translate("qMainWindow_obsPyck", "next FocMec"))
        self.qToolButton_showWadati.setText(
            _translate("qMainWindow_obsPyck", "show Wadati"))
        self.qToolButton_getNextEvent.setText(
            _translate("qMainWindow_obsPyck", "get Next Event"))
        self.qToolButton_updateEventList.setText(
            _translate("qMainWindow_obsPyck", "update Event List"))
        self.qToolButton_sendNewEvent.setText(
            _translate("qMainWindow_obsPyck", "send New Event"))
        self.qToolButton_replaceEvent.setText(
            _translate("qMainWindow_obsPyck", "replace Event"))
        self.qToolButton_deleteEvent.setText(
            _translate("qMainWindow_obsPyck", "delete Event"))
        self.qToolButton_saveEventLocally.setText(
            _translate("qMainWindow_obsPyck", "save Event locally"))
        self.qCheckBox_public.setText(
            _translate("qMainWindow_obsPyck", "public"))
        self.qComboBox_eventType.setItemText(
            0, _translate("qMainWindow_obsPyck", "<event type>"))
        self.qComboBox_eventType.setItemText(
            1, _translate("qMainWindow_obsPyck", "not existing"))
        self.qComboBox_eventType.setItemText(
            2, _translate("qMainWindow_obsPyck", "not reported"))
        self.qComboBox_eventType.setItemText(
            3, _translate("qMainWindow_obsPyck", "earthquake"))
        self.qComboBox_eventType.setItemText(4, _translate(
            "qMainWindow_obsPyck", "anthropogenic event"))
        self.qComboBox_eventType.setItemText(
            5, _translate("qMainWindow_obsPyck", "collapse"))
        self.qComboBox_eventType.setItemText(
            6, _translate("qMainWindow_obsPyck", "cavity collapse"))
        self.qComboBox_eventType.setItemText(
            7, _translate("qMainWindow_obsPyck", "mine collapse"))
        self.qComboBox_eventType.setItemText(8, _translate(
            "qMainWindow_obsPyck", "building collapse"))
        self.qComboBox_eventType.setItemText(
            9, _translate("qMainWindow_obsPyck", "explosion"))
        self.qComboBox_eventType.setItemText(10, _translate(
            "qMainWindow_obsPyck", "accidental explosion"))
        self.qComboBox_eventType.setItemText(11, _translate(
            "qMainWindow_obsPyck", "chemical explosion"))
        self.qComboBox_eventType.setItemText(12, _translate(
            "qMainWindow_obsPyck", "controlled explosion"))
        self.qComboBox_eventType.setItemText(13, _translate(
            "qMainWindow_obsPyck", "experimental explosion"))
        self.qComboBox_eventType.setItemText(14, _translate(
            "qMainWindow_obsPyck", "industrial explosion"))
        self.qComboBox_eventType.setItemText(
            15, _translate("qMainWindow_obsPyck", "mining explosion"))
        self.qComboBox_eventType.setItemText(
            16, _translate("qMainWindow_obsPyck", "quarry blast"))
        self.qComboBox_eventType.setItemText(
            17, _translate("qMainWindow_obsPyck", "road cut"))
        self.qComboBox_eventType.setItemText(
            18, _translate("qMainWindow_obsPyck", "blasting levee"))
        self.qComboBox_eventType.setItemText(19, _translate(
            "qMainWindow_obsPyck", "nuclear explosion"))
        self.qComboBox_eventType.setItemText(20, _translate(
            "qMainWindow_obsPyck", "induced or triggered event"))
        self.qComboBox_eventType.setItemText(
            21, _translate("qMainWindow_obsPyck", "rock burst"))
        self.qComboBox_eventType.setItemText(22, _translate(
            "qMainWindow_obsPyck", "reservoir loading"))
        self.qComboBox_eventType.setItemText(
            23, _translate("qMainWindow_obsPyck", "fluid injection"))
        self.qComboBox_eventType.setItemText(
            24, _translate("qMainWindow_obsPyck", "fluid extraction"))
        self.qComboBox_eventType.setItemText(
            25, _translate("qMainWindow_obsPyck", "crash"))
        self.qComboBox_eventType.setItemText(
            26, _translate("qMainWindow_obsPyck", "plane crash"))
        self.qComboBox_eventType.setItemText(
            27, _translate("qMainWindow_obsPyck", "train crash"))
        self.qComboBox_eventType.setItemText(
            28, _translate("qMainWindow_obsPyck", "boat crash"))
        self.qComboBox_eventType.setItemText(
            29, _translate("qMainWindow_obsPyck", "other event"))
        self.qComboBox_eventType.setItemText(30, _translate(
            "qMainWindow_obsPyck", "atmospheric event"))
        self.qComboBox_eventType.setItemText(
            31, _translate("qMainWindow_obsPyck", "sonic boom"))
        self.qComboBox_eventType.setItemText(
            32, _translate("qMainWindow_obsPyck", "sonic blast"))
        self.qComboBox_eventType.setItemText(
            33, _translate("qMainWindow_obsPyck", "acoustic noise"))
        self.qComboBox_eventType.setItemText(
            34, _translate("qMainWindow_obsPyck", "thunder"))
        self.qComboBox_eventType.setItemText(
            35, _translate("qMainWindow_obsPyck", "avalanche"))
        self.qComboBox_eventType.setItemText(
            36, _translate("qMainWindow_obsPyck", "snow avalanche"))
        self.qComboBox_eventType.setItemText(
            37, _translate("qMainWindow_obsPyck", "debris avalanche"))
        self.qComboBox_eventType.setItemText(38, _translate(
            "qMainWindow_obsPyck", "hydroacoustic event"))
        self.qComboBox_eventType.setItemText(
            39, _translate("qMainWindow_obsPyck", "ice quake"))
        self.qComboBox_eventType.setItemText(
            40, _translate("qMainWindow_obsPyck", "slide"))
        self.qComboBox_eventType.setItemText(
            41, _translate("qMainWindow_obsPyck", "landslide"))
        self.qComboBox_eventType.setItemText(
            42, _translate("qMainWindow_obsPyck", "rockslide"))
        self.qComboBox_eventType.setItemText(
            43, _translate("qMainWindow_obsPyck", "meteorite"))
        self.qComboBox_eventType.setItemText(44, _translate(
            "qMainWindow_obsPyck", "volcanic eruption"))
        self.qLabel_x_rel.setText(_translate(
            "qMainWindow_obsPyck", "x (rel):"))
        self.qLabel_y.setText(_translate("qMainWindow_obsPyck", "y:"))
        self.qLabel_x_abs.setText(_translate("qMainWindow_obsPyck", "x:"))
        self.qToolButton_debug.setText(
            _translate("qMainWindow_obsPyck", "debug"))
        self.qToolButton_sort_abc.setToolTip(_translate(
            "qMainWindow_obsPyck", "sort streams alphabetically"))
        self.qToolButton_sort_abc.setText(
            _translate("qMainWindow_obsPyck", "sort ABC"))
        self.qToolButton_sort_distance.setToolTip(_translate(
            "qMainWindow_obsPyck", "sort streams by epicentral distance"))
        self.qToolButton_sort_distance.setText(
            _translate("qMainWindow_obsPyck", "sort Dist."))
        self.qToolButton_previousStream.setText(
            _translate("qMainWindow_obsPyck", "<"))
        self.qLabel_streamNumber.setText(_translate("qMainWindow_obsPyck", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<  html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, l  i { white-space: pre-wrap; }\n"
                                                    "<  /style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                    "<  p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00/00</p></body></html>"))
        self.qToolButton_nextStream.setText(
            _translate("qMainWindow_obsPyck", ">"))
        self.qToolButton_overview.setText(
            _translate("qMainWindow_obsPyck", "Overview"))
        self.qToolButton_physical_units.setToolTip(_translate(
            "qMainWindow_obsPyck", "Convert to physical units doing instrument correction (config: section \"main\", option \"physical_units\"; either \"velocity\", \"displacement\" or \"acceleration\")"))
        self.qToolButton_physical_units.setText(
            _translate("qMainWindow_obsPyck", "physical units"))
        self.qLabel_waterlevel.setText(
            _translate("qMainWindow_obsPyck", "w_lev"))
        self.qToolButton_filter.setText(
            _translate("qMainWindow_obsPyck", "Filter"))
        self.qToolButton_rotateLQT.setText(
            _translate("qMainWindow_obsPyck", "LQT"))
        self.qToolButton_rotateZRT.setText(
            _translate("qMainWindow_obsPyck", "ZRT"))
        self.qToolButton_trigger.setText(
            _translate("qMainWindow_obsPyck", "recSTALTA"))
        self.qToolButton_arpicker.setText(
            _translate("qMainWindow_obsPyck", "arPicker"))
        self.qLabel_sta.setText(_translate("qMainWindow_obsPyck", "STA"))
        self.qLabel_lta.setText(_translate("qMainWindow_obsPyck", "LTA"))
        self.qComboBox_filterType.setItemText(
            0, _translate("qMainWindow_obsPyck", "Bandpass"))
        self.qComboBox_filterType.setItemText(
            1, _translate("qMainWindow_obsPyck", "Bandstop"))
        self.qComboBox_filterType.setItemText(
            2, _translate("qMainWindow_obsPyck", "Lowpass"))
        self.qComboBox_filterType.setItemText(
            3, _translate("qMainWindow_obsPyck", "Highpass"))
        self.qCheckBox_zerophase.setText(
            _translate("qMainWindow_obsPyck", "Zero-Ph."))
        self.qCheckBox_50Hz.setText(_translate("qMainWindow_obsPyck", "50Hz"))
        self.qLabel_corners.setText(_translate("qMainWindow_obsPyck", "Corn."))
        self.qLabel_lowpass.setText(
            _translate("qMainWindow_obsPyck", "Low C."))
        self.qLabel_highpass.setText(
            _translate("qMainWindow_obsPyck", "High C."))
        self.qToolButton_spectrogram.setText(
            _translate("qMainWindow_obsPyck", "Spectrogram"))
        self.qCheckBox_spectrogramLog.setText(
            _translate("qMainWindow_obsPyck", "log"))
        self.qLabel_wlen.setText(_translate("qMainWindow_obsPyck", "wlen"))
        self.qLabel_perlap.setText(_translate("qMainWindow_obsPyck", "%lap"))
        self.qPushButton_qml_update.setText(_translate(
            "qMainWindow_obsPyck", "update QuakeML text"))

    def do_grid_search(self):
        print("Performing grid search...")
