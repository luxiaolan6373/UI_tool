# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 603)
        MainWindow.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.ed_code_init = QtWidgets.QTextEdit(self.tab)
        self.ed_code_init.setObjectName("ed_code_init")
        self.gridLayout_2.addWidget(self.ed_code_init, 5, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.tab)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.classLabel = QtWidgets.QLabel(self.tab)
        self.classLabel.setObjectName("classLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.classLabel)
        self.uiClassLabel = QtWidgets.QLabel(self.tab)
        self.uiClassLabel.setObjectName("uiClassLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiClassLabel)
        self.uiClassLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiClassLineEdit.setObjectName("uiClassLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiClassLineEdit)
        self.titleLabel = QtWidgets.QLabel(self.tab)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(self.tab)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.sizeLabel = QtWidgets.QLabel(self.tab)
        self.sizeLabel.setObjectName("sizeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sizeLabel)
        self.sizeLineEdit = QtWidgets.QLineEdit(self.tab)
        self.sizeLineEdit.setObjectName("sizeLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sizeLineEdit)
        self.moveLabel = QtWidgets.QLabel(self.tab)
        self.moveLabel.setObjectName("moveLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.moveLabel)
        self.moveLineEdit = QtWidgets.QLineEdit(self.tab)
        self.moveLineEdit.setObjectName("moveLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.moveLineEdit)
        self.flagsLabel = QtWidgets.QLabel(self.tab)
        self.flagsLabel.setObjectName("flagsLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.flagsLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cb_top = QtWidgets.QCheckBox(self.tab)
        self.cb_top.setObjectName("cb_top")
        self.gridLayout.addWidget(self.cb_top, 1, 0, 1, 1)
        self.cb_max_bt = QtWidgets.QCheckBox(self.tab)
        self.cb_max_bt.setTabletTracking(False)
        self.cb_max_bt.setAcceptDrops(False)
        self.cb_max_bt.setAutoFillBackground(False)
        self.cb_max_bt.setChecked(True)
        self.cb_max_bt.setObjectName("cb_max_bt")
        self.gridLayout.addWidget(self.cb_max_bt, 0, 0, 1, 1)
        self.cbb_flags = QtWidgets.QComboBox(self.tab)
        self.cbb_flags.setObjectName("cbb_flags")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.cbb_flags.addItem("")
        self.gridLayout.addWidget(self.cbb_flags, 2, 0, 1, 3)
        self.cb_exit = QtWidgets.QCheckBox(self.tab)
        self.cb_exit.setChecked(True)
        self.cb_exit.setObjectName("cb_exit")
        self.gridLayout.addWidget(self.cb_exit, 0, 2, 1, 1)
        self.cb_bjtm = QtWidgets.QCheckBox(self.tab)
        self.cb_bjtm.setObjectName("cb_bjtm")
        self.gridLayout.addWidget(self.cb_bjtm, 1, 1, 1, 1)
        self.cb_min_bt = QtWidgets.QCheckBox(self.tab)
        self.cb_min_bt.setChecked(True)
        self.cb_min_bt.setObjectName("cb_min_bt")
        self.gridLayout.addWidget(self.cb_min_bt, 0, 1, 1, 1)
        self.cb_wbk = QtWidgets.QCheckBox(self.tab)
        self.cb_wbk.setObjectName("cb_wbk")
        self.gridLayout.addWidget(self.cb_wbk, 1, 2, 1, 1)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.bt_code_generation = QtWidgets.QPushButton(self.tab)
        self.bt_code_generation.setObjectName("bt_code_generation")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.bt_code_generation)
        self.cbb_class = QtWidgets.QComboBox(self.tab)
        self.cbb_class.setObjectName("cbb_class")
        self.cbb_class.addItem("")
        self.cbb_class.addItem("")
        self.cbb_class.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbb_class)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.ed_code_import = QtWidgets.QTextEdit(self.tab)
        self.ed_code_import.setObjectName("ed_code_import")
        self.gridLayout_2.addWidget(self.ed_code_import, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.ed_code_class = QtWidgets.QTextEdit(self.tab)
        self.ed_code_class.setObjectName("ed_code_class")
        self.gridLayout_2.addWidget(self.ed_code_class, 1, 1, 5, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ed_signal = QtWidgets.QTextEdit(self.tab_2)
        self.ed_signal.setObjectName("ed_signal")
        self.gridLayout_3.addWidget(self.ed_signal, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cbb_buttons = QtWidgets.QComboBox(self.groupBox)
        self.cbb_buttons.setToolTipDuration(-1)
        self.cbb_buttons.setObjectName("cbb_buttons")
        self.cbb_buttons.addItem("")
        self.cbb_buttons.addItem("")
        self.cbb_buttons.addItem("")
        self.cbb_buttons.addItem("")
        self.cbb_buttons.addItem("")
        self.cbb_buttons.addItem("")
        self.verticalLayout_6.addWidget(self.cbb_buttons)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cbb_input = QtWidgets.QComboBox(self.groupBox_2)
        self.cbb_input.setToolTipDuration(0)
        self.cbb_input.setObjectName("cbb_input")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.verticalLayout_5.addWidget(self.cbb_input)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbb_display = QtWidgets.QComboBox(self.groupBox_3)
        self.cbb_display.setToolTipDuration(0)
        self.cbb_display.setObjectName("cbb_display")
        self.cbb_display.addItem("")
        self.cbb_display.addItem("")
        self.cbb_display.addItem("")
        self.cbb_display.addItem("")
        self.cbb_display.addItem("")
        self.cbb_display.addItem("")
        self.verticalLayout_4.addWidget(self.cbb_display)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbb_itemViews = QtWidgets.QComboBox(self.groupBox_4)
        self.cbb_itemViews.setToolTipDuration(0)
        self.cbb_itemViews.setObjectName("cbb_itemViews")
        self.cbb_itemViews.addItem("")
        self.cbb_itemViews.addItem("")
        self.cbb_itemViews.addItem("")
        self.cbb_itemViews.addItem("")
        self.cbb_itemViews.addItem("")
        self.verticalLayout_3.addWidget(self.cbb_itemViews)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbb_itemWidgets = QtWidgets.QComboBox(self.groupBox_5)
        self.cbb_itemWidgets.setToolTipDuration(0)
        self.cbb_itemWidgets.setObjectName("cbb_itemWidgets")
        self.cbb_itemWidgets.addItem("")
        self.cbb_itemWidgets.addItem("")
        self.cbb_itemWidgets.addItem("")
        self.verticalLayout_2.addWidget(self.cbb_itemWidgets)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbb_containers = QtWidgets.QComboBox(self.groupBox_6)
        self.cbb_containers.setToolTipDuration(0)
        self.cbb_containers.setObjectName("cbb_containers")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.cbb_containers.addItem("")
        self.horizontalLayout_2.addWidget(self.cbb_containers)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.gridLayout_3.addWidget(self.groupBox_7, 0, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)
        self.ed_connect = QtWidgets.QTextEdit(self.tab_2)
        self.ed_connect.setObjectName("ed_connect")
        self.gridLayout_3.addWidget(self.ed_connect, 1, 1, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.nameLabel_2 = QtWidgets.QLabel(self.groupBox_8)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.nameLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_8)
        self.nameLineEdit_2.setObjectName("nameLineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit_2)
        self.suffixLabel = QtWidgets.QLabel(self.groupBox_8)
        self.suffixLabel.setObjectName("suffixLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.suffixLabel)
        self.suffixLineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.suffixLineEdit.setObjectName("suffixLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.suffixLineEdit)
        self.signalLabel = QtWidgets.QLabel(self.groupBox_8)
        self.signalLabel.setObjectName("signalLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.signalLabel)
        self.cbb_signal = QtWidgets.QComboBox(self.groupBox_8)
        self.cbb_signal.setObjectName("cbb_signal")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbb_signal)
        self.verticalLayout_7.addLayout(self.formLayout_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_8)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.bt_code_signal = QtWidgets.QPushButton(self.groupBox_8)
        self.bt_code_signal.setObjectName("bt_code_signal")
        self.verticalLayout_7.addWidget(self.bt_code_signal)
        self.gridLayout_3.addWidget(self.groupBox_8, 2, 0, 2, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.vbox_web = QtWidgets.QVBoxLayout(self.tab_3)
        self.vbox_web.setContentsMargins(5, 5, 5, 5)
        self.vbox_web.setSpacing(5)
        self.vbox_web.setObjectName("vbox_web")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.ed_api = QtWidgets.QLineEdit(self.tab_3)
        self.ed_api.setObjectName("ed_api")
        self.horizontalLayout_3.addWidget(self.ed_api)
        self.bt_find_api = QtWidgets.QPushButton(self.tab_3)
        self.bt_find_api.setObjectName("bt_find_api")
        self.horizontalLayout_3.addWidget(self.bt_find_api)
        self.vbox_web.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.vbox_QSS_web = QtWidgets.QVBoxLayout(self.tab_4)
        self.vbox_QSS_web.setContentsMargins(5, 5, 5, 5)
        self.vbox_QSS_web.setSpacing(5)
        self.vbox_QSS_web.setObjectName("vbox_QSS_web")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_qss = QtWidgets.QPushButton(self.tab_4)
        self.bt_qss.setObjectName("bt_qss")
        self.horizontalLayout_4.addWidget(self.bt_qss)
        self.ed_qss = QtWidgets.QLineEdit(self.tab_4)
        self.ed_qss.setObjectName("ed_qss")
        self.horizontalLayout_4.addWidget(self.ed_qss)
        self.bt_find_qss = QtWidgets.QPushButton(self.tab_4)
        self.bt_find_qss.setObjectName("bt_find_qss")
        self.horizontalLayout_4.addWidget(self.bt_find_qss)
        self.vbox_QSS_web.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.cbb_buttons.setCurrentIndex(-1)
        self.cbb_input.setCurrentIndex(-1)
        self.cbb_display.setCurrentIndex(-1)
        self.cbb_itemViews.setCurrentIndex(-1)
        self.cbb_itemWidgets.setCurrentIndex(-1)
        self.cbb_containers.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>还有更多功能正在研发中...</p><p>如果您有什么想法可以在论坛或者B站留言!</p><p>论坛地址:www.52pojie.cn</p><p>B站ID:python懒人智能</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "实例化:"))
        self.label.setText(_translate("MainWindow", "模块引用:"))
        self.ed_code_init.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt; font-weight:400;\"><br /></p></body></html>"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.nameLineEdit.setText(_translate("MainWindow", "window_main"))
        self.classLabel.setText(_translate("MainWindow", "Class:"))
        self.uiClassLabel.setText(_translate("MainWindow", "UI_Class:"))
        self.uiClassLineEdit.setText(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Title:"))
        self.titleLineEdit.setText(_translate("MainWindow", "我的主窗口"))
        self.sizeLabel.setText(_translate("MainWindow", "Size"))
        self.sizeLineEdit.setText(_translate("MainWindow", "500*500"))
        self.moveLabel.setText(_translate("MainWindow", "Move:"))
        self.moveLineEdit.setText(_translate("MainWindow", "200,200"))
        self.flagsLabel.setText(_translate("MainWindow", "Flags:"))
        self.cb_top.setText(_translate("MainWindow", "永远置顶"))
        self.cb_max_bt.setText(_translate("MainWindow", "最大化按钮"))
        self.cbb_flags.setItemText(0, _translate("MainWindow", "Qt.Widget默认值 自动识别是什么窗口"))
        self.cbb_flags.setItemText(1, _translate("MainWindow", "Qt.Window 部件始终为窗口"))
        self.cbb_flags.setItemText(2, _translate("MainWindow", "Qt.Dialog 部件为对话框"))
        self.cbb_flags.setItemText(3, _translate("MainWindow", "Qt.Sheet 部件是一个Macintosh表单"))
        self.cbb_flags.setItemText(4, _translate("MainWindow", "Qt.Drawer 部件是一个Macintosh抽屉"))
        self.cbb_flags.setItemText(5, _translate("MainWindow", "Qt.Popup 部件是一个弹出式顶层窗口"))
        self.cbb_flags.setItemText(6, _translate("MainWindow", "Qt.Tool 部件是一个工具窗口"))
        self.cbb_flags.setItemText(7, _translate("MainWindow", "Qt.ToolTip:部件是一个提示窗口"))
        self.cbb_flags.setItemText(8, _translate("MainWindow", "Qt.Desktop 部件是一个桌面"))
        self.cbb_flags.setItemText(9, _translate("MainWindow", "Qt.SplashScreen 部件是一个欢迎窗口"))
        self.cbb_flags.setItemText(10, _translate("MainWindow", "Qt.SubWindow:部件是一个子窗口"))
        self.cb_exit.setText(_translate("MainWindow", "退出按钮"))
        self.cb_bjtm.setText(_translate("MainWindow", "背景透明默认0.5"))
        self.cb_min_bt.setText(_translate("MainWindow", "最小化按钮"))
        self.cb_wbk.setText(_translate("MainWindow", "窗口无边框"))
        self.bt_code_generation.setText(_translate("MainWindow", "一键生成代码"))
        self.cbb_class.setItemText(0, _translate("MainWindow", "QMainWindow"))
        self.cbb_class.setItemText(1, _translate("MainWindow", "QWidget"))
        self.cbb_class.setItemText(2, _translate("MainWindow", "QDialog"))
        self.label_4.setText(_translate("MainWindow", "参数:必须遵守命名规则 ui生成的py文件都对应UI_class参数的值"))
        self.ed_code_import.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "类主体:"))
        self.ed_code_class.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt; font-weight:400;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "UI加载与初始化"))
        self.label_7.setText(_translate("MainWindow", "槽函数/重写 实现代码:"))
        self.groupBox_7.setTitle(_translate("MainWindow", "第一步选择控件:"))
        self.groupBox.setTitle(_translate("MainWindow", "Buttons"))
        self.cbb_buttons.setItemText(0, _translate("MainWindow", "Push Buttoon"))
        self.cbb_buttons.setItemText(1, _translate("MainWindow", "Tool Button"))
        self.cbb_buttons.setItemText(2, _translate("MainWindow", "Radio Button"))
        self.cbb_buttons.setItemText(3, _translate("MainWindow", "Check Box"))
        self.cbb_buttons.setItemText(4, _translate("MainWindow", "Command Link Button"))
        self.cbb_buttons.setItemText(5, _translate("MainWindow", "Dialog Button Box"))
        self.groupBox_2.setTitle(_translate("MainWindow", "input Widgets"))
        self.cbb_input.setItemText(0, _translate("MainWindow", "Combo Box"))
        self.cbb_input.setItemText(1, _translate("MainWindow", "Font Combo Box"))
        self.cbb_input.setItemText(2, _translate("MainWindow", "Line Edit"))
        self.cbb_input.setItemText(3, _translate("MainWindow", "Text Edit"))
        self.cbb_input.setItemText(4, _translate("MainWindow", "Plain Text Edit"))
        self.cbb_input.setItemText(5, _translate("MainWindow", "Spin Box"))
        self.cbb_input.setItemText(6, _translate("MainWindow", "Double Spin Box"))
        self.cbb_input.setItemText(7, _translate("MainWindow", "Time Edit"))
        self.cbb_input.setItemText(8, _translate("MainWindow", "Date Edit"))
        self.cbb_input.setItemText(9, _translate("MainWindow", "Date/Time Edit"))
        self.cbb_input.setItemText(10, _translate("MainWindow", "Dial"))
        self.cbb_input.setItemText(11, _translate("MainWindow", "Horizontal Scroll Bar"))
        self.cbb_input.setItemText(12, _translate("MainWindow", "Vertical Scroll Bar"))
        self.cbb_input.setItemText(13, _translate("MainWindow", "Horizontal Slider"))
        self.cbb_input.setItemText(14, _translate("MainWindow", "VerTical Slider"))
        self.cbb_input.setItemText(15, _translate("MainWindow", "Key Sequence Edit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Display Widgets"))
        self.cbb_display.setItemText(0, _translate("MainWindow", "Label"))
        self.cbb_display.setItemText(1, _translate("MainWindow", "Text Browser"))
        self.cbb_display.setItemText(2, _translate("MainWindow", "Graphics View"))
        self.cbb_display.setItemText(3, _translate("MainWindow", "Calendar Widget"))
        self.cbb_display.setItemText(4, _translate("MainWindow", "LCD Number"))
        self.cbb_display.setItemText(5, _translate("MainWindow", "Progress Bar"))
        self.groupBox_4.setTitle(_translate("MainWindow", "item Views(Model-Based)"))
        self.cbb_itemViews.setItemText(0, _translate("MainWindow", "list View"))
        self.cbb_itemViews.setItemText(1, _translate("MainWindow", "Tree View"))
        self.cbb_itemViews.setItemText(2, _translate("MainWindow", "Table View"))
        self.cbb_itemViews.setItemText(3, _translate("MainWindow", "Column View"))
        self.cbb_itemViews.setItemText(4, _translate("MainWindow", "Undo View"))
        self.groupBox_5.setTitle(_translate("MainWindow", "item Widgets(item-Based)"))
        self.cbb_itemWidgets.setItemText(0, _translate("MainWindow", "List Widget"))
        self.cbb_itemWidgets.setItemText(1, _translate("MainWindow", "Tree Widget"))
        self.cbb_itemWidgets.setItemText(2, _translate("MainWindow", "Table Widget"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Containers"))
        self.cbb_containers.setItemText(0, _translate("MainWindow", "Group Box"))
        self.cbb_containers.setItemText(1, _translate("MainWindow", "Scroll Area"))
        self.cbb_containers.setItemText(2, _translate("MainWindow", "Tool Box"))
        self.cbb_containers.setItemText(3, _translate("MainWindow", "Tab Widget"))
        self.cbb_containers.setItemText(4, _translate("MainWindow", "Stacked Widget"))
        self.cbb_containers.setItemText(5, _translate("MainWindow", "Frame"))
        self.cbb_containers.setItemText(6, _translate("MainWindow", "Widget"))
        self.cbb_containers.setItemText(7, _translate("MainWindow", "MDI Area"))
        self.cbb_containers.setItemText(8, _translate("MainWindow", "Dock Widget"))
        self.label_6.setText(_translate("MainWindow", "信号绑定槽函数:"))
        self.groupBox_8.setTitle(_translate("MainWindow", "第二步填写参数:"))
        self.nameLabel_2.setText(_translate("MainWindow", "name:"))
        self.nameLineEdit_2.setText(_translate("MainWindow", "my"))
        self.suffixLabel.setText(_translate("MainWindow", "suffix"))
        self.suffixLineEdit.setText(_translate("MainWindow", "tt"))
        self.signalLabel.setText(_translate("MainWindow", "Signal"))
        self.label_5.setText(_translate("MainWindow", "suffix为函数名的后缀如:_tt"))
        self.bt_code_signal.setText(_translate("MainWindow", "生成信号与槽代码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "信号与槽"))
        self.bt_find_api.setText(_translate("MainWindow", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "PyQt5官方API文档"))
        self.bt_qss.setText(_translate("MainWindow", "官方QSS文档英文版 建议使用有道词典的截图翻译"))
        self.bt_find_qss.setText(_translate("MainWindow", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "QSS文档查看"))