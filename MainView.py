# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movieone.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
from PyQt5 import QtCore, QtGui, QtWidgets
from Learn.Weather.WeatherTool import Weather
from PyQt5.QtWidgets import *



# UI主类
class MainUIView(object):
    # UI属性方法
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 500)
        Dialog.setMinimumSize(QtCore.QSize(430, 0))
        # 菜单
        self.addMenu = self.menuBar().addMenu("&File")
        self.addMenu.addAction(QAction("&None", self, triggered=self.Test))
        self.addMenu = self.menuBar().addMenu("&Tools")
        self.addMenu.addAction(QAction("&Weather", self, triggered=self.Weather))

        # group1
        self.group1 = QtWidgets.QGroupBox(Dialog)
        self.group1.setGeometry(QtCore.QRect(10, 30, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.group1.setFont(font)
        self.group1.setAlignment(QtCore.Qt.AlignCenter)
        self.group1.setFlat(False)
        self.group1.setCheckable(False)
        self.group1.setObjectName("group1")

        self.labelTips = QtWidgets.QLabel(self.group1)
        self.labelTips.setGeometry(QtCore.QRect(10, 55, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTips.setFont(font)
        self.labelTips.setObjectName("labelTips")

        self.lineEditInput = QtWidgets.QLineEdit(self.group1)
        self.lineEditInput.setGeometry(QtCore.QRect(170, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditInput.setFont(font)
        self.lineEditInput.setText("")
        self.lineEditInput.setObjectName("lineEditInput")

        self.BtnSearching = QtWidgets.QCommandLinkButton(self.group1)
        self.BtnSearching.setGeometry(QtCore.QRect(270, 80, 131, 41))
        self.BtnSearching.setObjectName("BtnSearching")

        self.checkIsOffline = QtWidgets.QCheckBox(self.group1)
        self.checkIsOffline.setGeometry(QtCore.QRect(10, 90, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkIsOffline.setFont(font)
        self.checkIsOffline.setObjectName("checkIsOffline")
        # 内容框
        self.tableLinks = QtWidgets.QTableWidget(self.group1)
        self.tableLinks.setGeometry(QtCore.QRect(10, 125, 390, 171))
        self.tableLinks.setObjectName("tableWidget")
        # self.tableWidget.setRowCount(2)

        self.group2 = QtWidgets.QGroupBox(Dialog)
        self.group2.setGeometry(QtCore.QRect(10, 320, 500, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group2.setFont(font)
        self.group2.setTitle("")
        self.group2.setObjectName("group2")
        self.checkIsRecord = QtWidgets.QCheckBox(self.group2)
        self.checkIsRecord.setGeometry(QtCore.QRect(30, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)

        self.checkIsRecord.setFont(font)
        self.checkIsRecord.setObjectName("checkIsRecord")

        self.labelPassword = QtWidgets.QLabel(self.group2)
        self.labelPassword.setGeometry(QtCore.QRect(30, 55, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")

        self.lineEditAccount = QtWidgets.QLineEdit(self.group2)
        self.lineEditAccount.setGeometry(QtCore.QRect(120, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditAccount.setFont(font)
        self.lineEditAccount.setText("")
        self.lineEditAccount.setObjectName("lineEditAccount")

        self.lineEditPassword = QtWidgets.QLineEdit(self.group2)
        self.lineEditPassword.setGeometry(QtCore.QRect(120, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setObjectName("lineEditPassword")

        self.labelAccount = QtWidgets.QLabel(self.group2)
        self.labelAccount.setGeometry(QtCore.QRect(30, 15, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAccount.setFont(font)
        self.labelAccount.setObjectName("labelAccount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # UI组件
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MovieOne"))
        self.group1.setTitle(_translate("Dialog", "Let\'s Movie"))
        self.labelTips.setText(_translate("Dialog", "请输入您需要的电影:"))
        self.BtnSearching.setText(_translate("Dialog", "Seraching"))
        self.checkIsOffline.setText(_translate("Dialog", "是否离线下载到百度网盘"))
        self.checkIsRecord.setText(_translate("Dialog", "记住密码"))
        self.labelPassword.setText(_translate("Dialog", "网盘密码："))
        self.labelAccount.setText(_translate("Dialog", "网盘账号："))

    def SetTableData(self, table):
        self.tableLinks.clearContents()
        self.tableLinks.setColumnCount(2)
        self.tableLinks.setRowCount(len(table))
        self.tableLinks.setHorizontalHeaderLabels(['电影名称', '双击链接'])
        self.tableLinks.setColumnWidth(1, 400)
        # self.tableLinks.resizeColumnsToContents()
        count = 0
        for name, url in table.items():
            # print(name, url, end=' ')
            name_item = QTableWidgetItem(name)
            url_item = QTableWidgetItem(url)
            self.tableLinks.setItem(0, count * 2, name_item)
            self.tableLinks.setItem(0, count * 2 + 1, url_item)
            count += 1

    def Test(self):
        print("Test")

    def Weather(self):
        print("Weather")
        forecast, pos_info = Weather().GetWeather()
        print(forecast, pos_info )






