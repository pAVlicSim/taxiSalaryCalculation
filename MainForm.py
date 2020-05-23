# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(747, 383)
        mainWindow.setMaximumSize(QtCore.QSize(16777215, 450))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [UKWN]")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        mainWindow.setTabletTracking(False)
        mainWindow.setAnimated(False)
        mainWindow.setDocumentMode(False)
        mainWindow.setDockOptions(QtWidgets.QMainWindow.ForceTabbedDocks | QtWidgets.QMainWindow.VerticalTabs)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_tableShifts = QtWidgets.QFrame(self.centralWidget)
        self.frame_tableShifts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tableShifts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tableShifts.setLineWidth(2)
        self.frame_tableShifts.setMidLineWidth(3)
        self.frame_tableShifts.setObjectName("frame_tableShifts")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_tableShifts)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableView_shifts = QtWidgets.QTableView(self.frame_tableShifts)
        self.tableView_shifts.setMinimumSize(QtCore.QSize(500, 250))
        self.tableView_shifts.setMaximumSize(QtCore.QSize(1200, 400))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tableView_shifts.setFont(font)
        self.tableView_shifts.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableView_shifts.setLineWidth(2)
        self.tableView_shifts.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableView_shifts.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_shifts.setObjectName("tableView_shifts")
        self.horizontalLayout_2.addWidget(self.tableView_shifts)
        self.horizontalLayout.addWidget(self.frame_tableShifts)
        mainWindow.setCentralWidget(self.centralWidget)
        self.menBbar = QtWidgets.QMenuBar(mainWindow)
        self.menBbar.setGeometry(QtCore.QRect(0, 0, 747, 30))
        self.menBbar.setObjectName("menBbar")
        self.menu_setting = QtWidgets.QMenu(self.menBbar)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.menu_setting.setFont(font)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_shifts = QtWidgets.QMenu(self.menBbar)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.menu_shifts.setFont(font)
        self.menu_shifts.setSeparatorsCollapsible(False)
        self.menu_shifts.setObjectName("menu_shifts")
        mainWindow.setMenuBar(self.menBbar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.dockWidget_setting = QtWidgets.QDockWidget(mainWindow)
        self.dockWidget_setting.setMaximumSize(QtCore.QSize(250, 350))
        self.dockWidget_setting.setFloating(False)
        self.dockWidget_setting.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        self.dockWidget_setting.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget_setting.setObjectName("dockWidget_setting")
        self.widgetContents = QtWidgets.QWidget()
        self.widgetContents.setObjectName("widgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dateEdit_shiftSelected = QtWidgets.QDateEdit(self.widgetContents)
        self.dateEdit_shiftSelected.setCalendarPopup(True)
        self.dateEdit_shiftSelected.setObjectName("dateEdit_shiftSelected")
        self.verticalLayout_2.addWidget(self.dateEdit_shiftSelected, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_selectTariff = QtWidgets.QComboBox(self.widgetContents)
        self.comboBox_selectTariff.setObjectName("comboBox_selectTariff")
        self.comboBox_selectTariff.addItem("")
        self.comboBox_selectTariff.addItem("")
        self.comboBox_selectTariff.addItem("")
        self.comboBox_selectTariff.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_selectTariff)
        self.tableView_settingTariff = QtWidgets.QTableView(self.widgetContents)
        self.tableView_settingTariff.setMaximumSize(QtCore.QSize(170, 200))
        self.tableView_settingTariff.setObjectName("tableView_settingTariff")
        self.tableView_settingTariff.horizontalHeader().setDefaultSectionSize(80)
        self.verticalLayout_2.addWidget(self.tableView_settingTariff)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.dockWidget_setting.setWidget(self.widgetContents)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_setting)
        self.action_addRow = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.action_addRow.setFont(font)
        self.action_addRow.setObjectName("action_addRow")
        self.action_removeRow = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.action_removeRow.setFont(font)
        self.action_removeRow.setObjectName("action_removeRow")
        self.action_addShift = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.action_addShift.setFont(font)
        self.action_addShift.setObjectName("action_addShift")
        self.action_removeShift = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.action_removeShift.setFont(font)
        self.action_removeShift.setObjectName("action_removeShift")
        self.action_calculatedShift = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.action_calculatedShift.setFont(font)
        self.action_calculatedShift.setObjectName("action_calculatedShift")
        self.action_saveSetting = QtWidgets.QAction(mainWindow)
        self.action_saveSetting.setObjectName("action_saveSetting")
        self.action_saveTariff = QtWidgets.QAction(mainWindow)
        self.action_saveTariff.setObjectName("action_saveTariff")
        self.menu_setting.addAction(self.action_addRow)
        self.menu_setting.addAction(self.action_removeRow)
        self.menu_setting.addSeparator()
        self.menu_setting.addAction(self.action_saveSetting)
        self.menu_setting.addAction(self.action_saveTariff)
        self.menu_shifts.addAction(self.action_addShift)
        self.menu_shifts.addAction(self.action_removeShift)
        self.menu_shifts.addAction(self.action_calculatedShift)
        self.menu_shifts.addSeparator()
        self.menBbar.addAction(self.menu_setting.menuAction())
        self.menBbar.addAction(self.menu_shifts.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Расчёт зарплаты  в такси"))
        self.menu_setting.setTitle(_translate("mainWindow", "Меню настройки"))
        self.menu_shifts.setTitle(_translate("mainWindow", "Меню смен"))
        self.dockWidget_setting.setWindowTitle(_translate("mainWindow", "Настройка оплаты"))
        self.dateEdit_shiftSelected.setDisplayFormat(_translate("mainWindow", "dd.MM.yy"))
        self.comboBox_selectTariff.setItemText(0, _translate("mainWindow", "Эконом"))
        self.comboBox_selectTariff.setItemText(1, _translate("mainWindow", "Эконом+"))
        self.comboBox_selectTariff.setItemText(2, _translate("mainWindow", "Комфорт"))
        self.comboBox_selectTariff.setItemText(3, _translate("mainWindow", "Комфорт+"))
        self.action_addRow.setText(_translate("mainWindow", "Добавить строку"))
        self.action_removeRow.setText(_translate("mainWindow", "Удалить строку"))
        self.action_addShift.setText(_translate("mainWindow", "Добавить смену"))
        self.action_removeShift.setText(_translate("mainWindow", "Удалить смену"))
        self.action_calculatedShift.setText(_translate("mainWindow", "Расчитать смену"))
        self.action_saveSetting.setText(_translate("mainWindow", "Сохранить настройки"))
        self.action_saveTariff.setText(_translate("mainWindow", "Сохранить тариф"))