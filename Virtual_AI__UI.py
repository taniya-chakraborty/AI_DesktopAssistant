# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Virtual_AI__UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Virtual_AI_UI(object):
    def setupUi(self, Virtual_AI_UI):
        Virtual_AI_UI.setObjectName("Virtual_AI_UI")
        Virtual_AI_UI.resize(1108, 847)
        self.centralwidget = QtWidgets.QWidget(Virtual_AI_UI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1111, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Virtual_AI_Assistant/Gif/3.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(960, 730, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(128, 255, 24)")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 720, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 141, 51))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size: 20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(140, 0, 141, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size: 20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 0, 381, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Virtual_AI_Assistant/Gif/4.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Virtual_AI_UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Virtual_AI_UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 26))
        self.menubar.setObjectName("menubar")
        Virtual_AI_UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Virtual_AI_UI)
        self.statusbar.setObjectName("statusbar")
        Virtual_AI_UI.setStatusBar(self.statusbar)

        self.retranslateUi(Virtual_AI_UI)
        QtCore.QMetaObject.connectSlotsByName(Virtual_AI_UI)

    def retranslateUi(self, Virtual_AI_UI):
        _translate = QtCore.QCoreApplication.translate
        Virtual_AI_UI.setWindowTitle(_translate("Virtual_AI_UI", "MainWindow"))
        self.pushButton.setText(_translate("Virtual_AI_UI", "RUN"))
        self.pushButton_2.setText(_translate("Virtual_AI_UI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Virtual_AI_UI = QtWidgets.QMainWindow()
    ui = Ui_Virtual_AI_UI()
    ui.setupUi(Virtual_AI_UI)
    Virtual_AI_UI.show()
    sys.exit(app.exec_())
