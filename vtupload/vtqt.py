# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QFile
from . import about, openfile
from vtupload.vtapi import vtapi


class Ui_MainWindow(object):
    def __init__(self):
        self.tableLength = 0
        self.tableUsed = 0
        self.hashlist = []
        self.icon = QtGui.QIcon()
        #print(QFile.exists('vtupload/bug.png'))
        self.icon.addPixmap(QtGui.QPixmap("vtupload/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.apikey = ""


    def setupUi(self, MainWindow):
    	#MAIN UI SETUP
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 750))
        MainWindow.setMaximumSize(QtCore.QSize(500, 750))
        MainWindow.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 500, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setMouseTracking(True)
        self.textBrowser.setStyleSheet("font-style: \"Consolas\";")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 200, 500, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(249)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setColumnWidth(0,399)
        self.tableWidget.setColumnWidth(1,99)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionInsert_API_Key = QtWidgets.QAction(MainWindow)
        self.actionInsert_API_Key.setObjectName("actionInsert_API_Key")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        #MENU ACTION SETUP
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionInsert_API_Key)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.actionAbout)
		#MENU ACTION TRIGGER        
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionAbout.triggered.connect(self.aboutUi)
        self.actionOpen.triggered.connect(self.openFileUi)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
    	#MAIN UI TEXT (to translate)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "vtup104d3r"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Scan Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionInsert_API_Key.setText(_translate("MainWindow", "Insert API Key"))
        self.actionInsert_API_Key.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def aboutUi(self):
    	#ABOUT DIALOG
    	dwin = QtWidgets.QDialog()
    	x = about.Ui_Dialog()
    	x.setupUi(dwin)
    	dwin.setWindowIcon(self.icon)
    	dwin.exec()

    def openFileUi(self):
    	#ADD FILE DIALOG
        if not self.verifyKey():
        	return
        x = openfile.Ui_Widget()
        filename = x.initUI()
        if not filename:
        	return
        hash = vtapi.gethash(filename)
        if hash not in self.hashlist:
        	self.hashlist.append(hash)
        	self.tableWidget.insertRow(self.tableLength)
        	self.tableLength += 1
        	item = QtWidgets.QTableWidgetItem(filename)
        	self.tableWidget.setItem(self.tableUsed,0,item)
        	self.tableWidget.update()
        	self.tableUsed += 1
        	self.scanInit(filename)
        else:
        	alert = QtWidgets.QWidget()
        	alert.setWindowIcon(self.icon)
        	QtWidgets.QMessageBox.about(alert, "Alert", "File Already added !")
        	
    def scanInit(self,filename):
    	self.verifyKey()

    def verifyKey(self):
    	while not vtapi.checkapi(self.apikey):
    		alert = QtWidgets.QWidget()
    		alert.setWindowIcon(self.icon)
    		if self.apikey == "":
    			QtWidgets.QMessageBox.about(alert, "Alert", "API Key Required !")
    		else:
    			QtWidgets.QMessageBox.about(alert, "Alert", "Invlaid API Key !")
    		oldkey = self.apikey
    		self.insertApiUi()
    		if oldkey == self.apikey:
    			return False
    	return True

    def insertApiUi(self):
    	return