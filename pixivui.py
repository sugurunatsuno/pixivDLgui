# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pixiv.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PixivDownloader(object):
    def setupUi(self, PixivDownloader):
        PixivDownloader.setObjectName("PixivDownloader")
        PixivDownloader.resize(405, 201)
        self.gridLayoutWidget = QtWidgets.QWidget(PixivDownloader)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(PixivDownloader)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(PixivDownloader)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 10, 191, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(PixivDownloader)
        self.pushButton.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PixivDownloader)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PixivDownloader)
        QtCore.QMetaObject.connectSlotsByName(PixivDownloader)

    def retranslateUi(self, PixivDownloader):
        _translate = QtCore.QCoreApplication.translate
        PixivDownloader.setWindowTitle(_translate("PixivDownloader", "PixivDownloader"))
        self.label_2.setText(_translate("PixivDownloader", "password"))
        self.label.setText(_translate("PixivDownloader", "username"))
        self.lineEdit.setText(_translate("PixivDownloader", "example_username"))
        self.lineEdit_2.setText(_translate("PixivDownloader", "password"))
        self.label_3.setText(_translate("PixivDownloader", "directory"))
        self.lineEdit_3.setText(_translate("PixivDownloader", "C:/user/username/desktop/"))
        self.label_4.setText(_translate("PixivDownloader", "target user_id"))
        self.lineEdit_4.setText(_translate("PixivDownloader", "12345678"))
        self.pushButton.setText(_translate("PixivDownloader", "download"))
        self.pushButton_2.setText(_translate("PixivDownloader", "cancel"))
