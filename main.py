# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):

    def __init__(self):
        super().__init__()
 


    def setupUi(self, mainWindow):
        mainWindow.setWindowTitle("Retina v_1.0")
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(541, 597)
        mainWindow.setMaximumSize(QtCore.QSize(541, 597))
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeDisp = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeDisp.setGeometry(QtCore.QRect(180, 190, 181, 51))
        self.timeDisp.setObjectName("timeDisp")
        self.rd3 = QtWidgets.QLabel(self.centralwidget)
        self.rd3.setGeometry(QtCore.QRect(150, 330, 31, 31))
        self.rd3.setText("")
        self.rd3.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd3.setScaledContents(True)
        self.rd3.setObjectName("rd3")
        self.outerring = QtWidgets.QLabel(self.centralwidget)
        self.outerring.setGeometry(QtCore.QRect(80, 20, 381, 381))
        self.outerring.setText("")
        self.outerring.setPixmap(QtGui.QPixmap("D:/Downloads/black_circle_outline.png"))
        self.outerring.setScaledContents(True)
        self.outerring.setObjectName("outerring")
        self.innerCircle = QtWidgets.QLabel(self.centralwidget)
        self.innerCircle.setGeometry(QtCore.QRect(120, 60, 301, 301))
        self.innerCircle.setAutoFillBackground(False)
        self.innerCircle.setText("")
        self.innerCircle.setPixmap(QtGui.QPixmap("D:/Downloads/black_circle_outline.png"))
        self.innerCircle.setScaledContents(True)
        self.innerCircle.setObjectName("innerCircle")
        self.ed11 = QtWidgets.QLabel(self.centralwidget)
        self.ed11.setGeometry(QtCore.QRect(260, 20, 31, 31))
        self.ed11.setText("")
        self.ed11.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed11.setScaledContents(True)
        self.ed11.setObjectName("ed11")
        self.ed7 = QtWidgets.QLabel(self.centralwidget)
        self.ed7.setGeometry(QtCore.QRect(90, 140, 31, 31))
        self.ed7.setText("")
        self.ed7.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed7.setScaledContents(True)
        self.ed7.setObjectName("ed7")
        self.ed16 = QtWidgets.QLabel(self.centralwidget)
        self.ed16.setGeometry(QtCore.QRect(430, 190, 31, 31))
        self.ed16.setText("")
        self.ed16.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed16.setScaledContents(True)
        self.ed16.setObjectName("ed16")
        self.ed2 = QtWidgets.QLabel(self.centralwidget)
        self.ed2.setGeometry(QtCore.QRect(200, 360, 31, 31))
        self.ed2.setText("")
        self.ed2.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed2.setScaledContents(True)
        self.ed2.setObjectName("ed2")
        self.ed1 = QtWidgets.QLabel(self.centralwidget)
        self.ed1.setGeometry(QtCore.QRect(260, 370, 31, 31))
        self.ed1.setText("")
        self.ed1.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed1.setScaledContents(True)
        self.ed1.setObjectName("ed1")
        self.ed10 = QtWidgets.QLabel(self.centralwidget)
        self.ed10.setGeometry(QtCore.QRect(210, 30, 31, 31))
        self.ed10.setText("")
        self.ed10.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed10.setScaledContents(True)
        self.ed10.setObjectName("ed10")
        self.ed9 = QtWidgets.QLabel(self.centralwidget)
        self.ed9.setGeometry(QtCore.QRect(160, 50, 31, 31))
        self.ed9.setText("")
        self.ed9.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed9.setScaledContents(True)
        self.ed9.setObjectName("ed9")
        self.ed8 = QtWidgets.QLabel(self.centralwidget)
        self.ed8.setGeometry(QtCore.QRect(120, 90, 31, 31))
        self.ed8.setText("")
        self.ed8.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed8.setScaledContents(True)
        self.ed8.setObjectName("ed8")
        self.ed14 = QtWidgets.QLabel(self.centralwidget)
        self.ed14.setGeometry(QtCore.QRect(390, 90, 31, 31))
        self.ed14.setText("")
        self.ed14.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed14.setScaledContents(True)
        self.ed14.setObjectName("ed14")
        self.ed3 = QtWidgets.QLabel(self.centralwidget)
        self.ed3.setGeometry(QtCore.QRect(150, 330, 31, 31))
        self.ed3.setText("")
        self.ed3.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed3.setScaledContents(True)
        self.ed3.setObjectName("ed3")
        self.ed5 = QtWidgets.QLabel(self.centralwidget)
        self.ed5.setGeometry(QtCore.QRect(90, 240, 31, 31))
        self.ed5.setText("")
        self.ed5.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed5.setScaledContents(True)
        self.ed5.setObjectName("ed5")
        self.ed4 = QtWidgets.QLabel(self.centralwidget)
        self.ed4.setGeometry(QtCore.QRect(110, 290, 31, 31))
        self.ed4.setText("")
        self.ed4.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed4.setScaledContents(True)
        self.ed4.setObjectName("ed4")
        self.ed15 = QtWidgets.QLabel(self.centralwidget)
        self.ed15.setGeometry(QtCore.QRect(420, 140, 31, 31))
        self.ed15.setText("")
        self.ed15.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed15.setScaledContents(True)
        self.ed15.setObjectName("ed15")
        self.ed18 = QtWidgets.QLabel(self.centralwidget)
        self.ed18.setGeometry(QtCore.QRect(400, 290, 31, 31))
        self.ed18.setText("")
        self.ed18.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed18.setScaledContents(True)
        self.ed18.setObjectName("ed18")
        self.ed20 = QtWidgets.QLabel(self.centralwidget)
        self.ed20.setGeometry(QtCore.QRect(320, 360, 31, 31))
        self.ed20.setText("")
        self.ed20.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed20.setScaledContents(True)
        self.ed20.setObjectName("ed20")
        self.ed19 = QtWidgets.QLabel(self.centralwidget)
        self.ed19.setGeometry(QtCore.QRect(360, 330, 31, 31))
        self.ed19.setText("")
        self.ed19.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed19.setScaledContents(True)
        self.ed19.setObjectName("ed19")
        self.ed17 = QtWidgets.QLabel(self.centralwidget)
        self.ed17.setGeometry(QtCore.QRect(420, 240, 31, 31))
        self.ed17.setText("")
        self.ed17.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed17.setScaledContents(True)
        self.ed17.setObjectName("ed17")
        self.ed6 = QtWidgets.QLabel(self.centralwidget)
        self.ed6.setGeometry(QtCore.QRect(80, 190, 31, 31))
        self.ed6.setText("")
        self.ed6.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed6.setScaledContents(True)
        self.ed6.setObjectName("ed6")
        self.ed12 = QtWidgets.QLabel(self.centralwidget)
        self.ed12.setGeometry(QtCore.QRect(310, 30, 31, 31))
        self.ed12.setText("")
        self.ed12.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed12.setScaledContents(True)
        self.ed12.setObjectName("ed12")
        self.ed13 = QtWidgets.QLabel(self.centralwidget)
        self.ed13.setGeometry(QtCore.QRect(360, 60, 31, 31))
        self.ed13.setText("")
        self.ed13.setPixmap(QtGui.QPixmap("img/ed.png"))
        self.ed13.setScaledContents(True)
        self.ed13.setObjectName("ed13")
        self.rd1 = QtWidgets.QLabel(self.centralwidget)
        self.rd1.setGeometry(QtCore.QRect(260, 370, 31, 31))
        self.rd1.setText("")
        self.rd1.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd1.setScaledContents(True)
        self.rd1.setObjectName("rd1")
        self.rd12 = QtWidgets.QLabel(self.centralwidget)
        self.rd12.setGeometry(QtCore.QRect(310, 30, 31, 31))
        self.rd12.setText("")
        self.rd12.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd12.setScaledContents(True)
        self.rd12.setObjectName("rd12")
        self.rd10 = QtWidgets.QLabel(self.centralwidget)
        self.rd10.setGeometry(QtCore.QRect(210, 30, 31, 31))
        self.rd10.setText("")
        self.rd10.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd10.setScaledContents(True)
        self.rd10.setObjectName("rd10")
        self.rd9 = QtWidgets.QLabel(self.centralwidget)
        self.rd9.setGeometry(QtCore.QRect(160, 50, 31, 31))
        self.rd9.setText("")
        self.rd9.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd9.setScaledContents(True)
        self.rd9.setObjectName("rd9")
        self.rd8 = QtWidgets.QLabel(self.centralwidget)
        self.rd8.setGeometry(QtCore.QRect(120, 90, 31, 31))
        self.rd8.setText("")
        self.rd8.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd8.setScaledContents(True)
        self.rd8.setObjectName("rd8")
        self.rd7 = QtWidgets.QLabel(self.centralwidget)
        self.rd7.setGeometry(QtCore.QRect(90, 140, 31, 31))
        self.rd7.setText("")
        self.rd7.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd7.setScaledContents(True)
        self.rd7.setObjectName("rd7")
        self.rd6 = QtWidgets.QLabel(self.centralwidget)
        self.rd6.setGeometry(QtCore.QRect(80, 190, 31, 31))
        self.rd6.setText("")
        self.rd6.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd6.setScaledContents(True)
        self.rd6.setObjectName("rd6")
        self.rd5 = QtWidgets.QLabel(self.centralwidget)
        self.rd5.setGeometry(QtCore.QRect(90, 240, 31, 31))
        self.rd5.setText("")
        self.rd5.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd5.setScaledContents(True)
        self.rd5.setObjectName("rd5")
        self.rd4 = QtWidgets.QLabel(self.centralwidget)
        self.rd4.setGeometry(QtCore.QRect(110, 290, 31, 31))
        self.rd4.setText("")
        self.rd4.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd4.setScaledContents(True)
        self.rd4.setObjectName("rd4")
        self.rd2 = QtWidgets.QLabel(self.centralwidget)
        self.rd2.setGeometry(QtCore.QRect(200, 360, 31, 31))
        self.rd2.setText("")
        self.rd2.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd2.setScaledContents(True)
        self.rd2.setObjectName("rd2")
        self.rd15 = QtWidgets.QLabel(self.centralwidget)
        self.rd15.setGeometry(QtCore.QRect(420, 140, 31, 31))
        self.rd15.setText("")
        self.rd15.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd15.setScaledContents(True)
        self.rd15.setObjectName("rd15")
        self.rd14 = QtWidgets.QLabel(self.centralwidget)
        self.rd14.setGeometry(QtCore.QRect(390, 90, 31, 31))
        self.rd14.setText("")
        self.rd14.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd14.setScaledContents(True)
        self.rd14.setObjectName("rd14")
        self.rd13 = QtWidgets.QLabel(self.centralwidget)
        self.rd13.setGeometry(QtCore.QRect(360, 60, 31, 31))
        self.rd13.setText("")
        self.rd13.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd13.setScaledContents(True)
        self.rd13.setObjectName("rd13")
        self.rd11 = QtWidgets.QLabel(self.centralwidget)
        self.rd11.setGeometry(QtCore.QRect(260, 20, 31, 31))
        self.rd11.setText("")
        self.rd11.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd11.setScaledContents(True)
        self.rd11.setObjectName("rd11")
        self.rd17 = QtWidgets.QLabel(self.centralwidget)
        self.rd17.setGeometry(QtCore.QRect(420, 240, 31, 31))
        self.rd17.setText("")
        self.rd17.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd17.setScaledContents(True)
        self.rd17.setObjectName("rd17")
        self.rd16 = QtWidgets.QLabel(self.centralwidget)
        self.rd16.setGeometry(QtCore.QRect(430, 190, 31, 31))
        self.rd16.setText("")
        self.rd16.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd16.setScaledContents(True)
        self.rd16.setObjectName("rd16")
        self.rd18 = QtWidgets.QLabel(self.centralwidget)
        self.rd18.setGeometry(QtCore.QRect(400, 290, 31, 31))
        self.rd18.setText("")
        self.rd18.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd18.setScaledContents(True)
        self.rd18.setObjectName("rd18")
        self.rd19 = QtWidgets.QLabel(self.centralwidget)
        self.rd19.setGeometry(QtCore.QRect(360, 330, 31, 31))
        self.rd19.setText("")
        self.rd19.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd19.setScaledContents(True)
        self.rd19.setObjectName("rd19")
        self.rd20 = QtWidgets.QLabel(self.centralwidget)
        self.rd20.setGeometry(QtCore.QRect(320, 360, 31, 31))
        self.rd20.setText("")
        self.rd20.setPixmap(QtGui.QPixmap("img/rd.png"))
        self.rd20.setScaledContents(True)
        self.rd20.setObjectName("rd20")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(90, 490, 161, 41))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(290, 490, 161, 41))
        self.stopButton.setObjectName("stopButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle("Retina_v1.0")
        mainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.startButton.setStatusTip(_translate("mainWindow", "Start the timer"))
        self.startButton.setText(_translate("mainWindow", "Start"))
        self.stopButton.setStatusTip(_translate("mainWindow", "Stop the timer"))
        self.stopButton.setText(_translate("mainWindow", "Stop"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())