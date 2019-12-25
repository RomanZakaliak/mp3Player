# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 200)
        MainWindow.setMinimumSize(QtCore.QSize(360, 200))
        MainWindow.setMaximumSize(QtCore.QSize(360, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playPauseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playPauseBtn.setEnabled(False)
        self.playPauseBtn.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.playPauseBtn.setObjectName("playPauseBtn")
        self.filesList = QtWidgets.QComboBox(self.centralwidget)
        self.filesList.setGeometry(QtCore.QRect(10, 80, 331, 22))
        self.filesList.setObjectName("filesList")
        self.prevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.prevBtn.setEnabled(False)
        self.prevBtn.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.prevBtn.setObjectName("prevBtn")
        self.nxtBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nxtBtn.setEnabled(False)
        self.nxtBtn.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.nxtBtn.setObjectName("nxtBtn")
        self.playingTimeline = QtWidgets.QSlider(self.centralwidget)
        self.playingTimeline.setGeometry(QtCore.QRect(70, 120, 221, 22))
        self.playingTimeline.setOrientation(QtCore.Qt.Horizontal)
        self.playingTimeline.setObjectName("playingTimeline")
        self.curPos = QtWidgets.QLabel(self.centralwidget)
        self.curPos.setGeometry(QtCore.QRect(10, 120, 51, 21))
        self.curPos.setObjectName("curPos")
        self.endPos = QtWidgets.QLabel(self.centralwidget)
        self.endPos.setGeometry(QtCore.QRect(300, 120, 51, 21))
        self.endPos.setObjectName("endPos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelect_folder = QtWidgets.QAction(MainWindow)
        self.actionSelect_folder.setObjectName("actionSelect_folder")
        self.menuFile.addAction(self.actionSelect_folder)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GovnoCode mp3-player"))
        self.playPauseBtn.setText(_translate("MainWindow", "Play"))
        self.prevBtn.setText(_translate("MainWindow", "Previous"))
        self.nxtBtn.setText(_translate("MainWindow", "Next"))
        self.curPos.setText(_translate("MainWindow", "0.0.0"))
        self.endPos.setText(_translate("MainWindow", "0.0.0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSelect_folder.setText(_translate("MainWindow", "Select folder"))

