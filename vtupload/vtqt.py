import sys
import re
import os
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QFile
from . import about, openfile, insertapi
from vtupload.vtapi import vtapi
import threading
import time

class Ui_MainWindow(object):
    def __init__(self):
        self.tableLength = 0
        self.tableUsed = 0
        self.hashlist = []
        self.icon = QtGui.QIcon()
        #print(QFile.exists('vtupload/bug.png'))
        self.icon.addPixmap(QtGui.QPixmap("vtupload/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.apikey = ""
        self.alive = True
        self.files = []
        self.scanresult=[]
        self.scanned=[]


    def setupUi(self, MainWindow):
        #MAIN UI SETUP
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 200))
        MainWindow.setMaximumSize(QtCore.QSize(500, 750))
        MainWindow.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 500, 200))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setMouseTracking(False)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
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
        self.actionInsert_API_Key.triggered.connect(self.insertApiUi)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        conn = threading.Thread(target=self.keepAlive, args=('1',),daemon=True)
        conn.start()
        scn = threading.Thread(target=self.scanInit,args=('2',),daemon=True)
        scn.start()
        self.sessionCheck()



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
            self.files.append(filename)
        else:
            alert = QtWidgets.QWidget()
            alert.setWindowIcon(self.icon)
            QtWidgets.QMessageBox.about(alert, "Alert", "File Already added !")
            
    def scanInit(self,threadno):
        while 1:
            n = len(self.files)
            # print(n)
            if n == 0 :
                time.sleep(5)
                continue
            if not self.verifyKey():
                time.sleep(1)
                continue
            for i in range(n):
                if not self.files[i] in self.scanned:
                    self.scanresult.append(vtapi.upload(self.apikey,self.files[i]))
                    self.scanned.append(self.files[i])
                    



    def verifyKey(self):
        if not self.alive:
            self.noConn()
            return
        alert = QtWidgets.QWidget()
        alert.setWindowIcon(self.icon)
        if not vtapi.checkapi(self.apikey):
            if self.apikey == "":
                QtWidgets.QMessageBox.about(alert, "Alert", "API Key Required !")
            else:
                QtWidgets.QMessageBox.about(alert, "Alert", "Invlaid API Key !")
            return False
        return True

    def insertApiUi(self):
        oldkey = self.apikey
        if not self.alive:
            self.noConn()
            return
        dwin = QtWidgets.QDialog()
        x = insertapi.Ui_Form()
        x.setupUi(dwin,self.apikey)
        dwin.setWindowIcon(self.icon)
        dwin.exec()
        self.apikey = x.apikey
        alert = QtWidgets.QWidget()
        alert.setWindowIcon(self.icon)
        if not re.match('[a-z0-9]{64}',self.apikey):
            QtWidgets.QMessageBox.about(alert, "Alert", "Invlaid API Key !")
        elif not self.verifyKey():
            self.apikey=""
        elif oldkey != self.apikey:
            log = "Key In Use "+self.apikey
            old = self.plainTextEdit.toPlainText()
            self.plainTextEdit.setPlainText(old+log+"\n")
            self.sessionCreate()

    def sessionCheck(self):
        if os.name == 'nt':
            sdir = os.getenv('TMP')+'\\vtup104d3r'
            if not os.path.isfile(sdir+'\\apikey.vt'):
                return False
            kfile = open(sdir+'\\apikey.vt','r')
            ckey = kfile.read()
            kfile.close()
            if re.match('[a-z0-9]{64}',ckey):
                self.apikey=ckey
                print("Session Found")
                log = "Key In Use "+self.apikey
                old = self.plainTextEdit.toPlainText()
                self.plainTextEdit.setPlainText(old+log+"\n")
                return True
            print("Session Not Found")
            return False

        elif os.name == 'posix':
            sdir = os.getenv('HOME')+'/.vtup104d3r'
            if not os.path.isdir(sdir):
                os.mkdir(sdir)
            kfile = open(sdir+'/apikey.vt','r')
            ckey = kfile.read()
            kfile.close()
            if re.match('[a-z0-9]{64}',ckey):
                self.apikey=ckey
                return True
            return False

        # else:
            # print("Session Failed")
        return False

    def sessionCreate(self):
        if os.name == 'nt':
            sdir = os.getenv('TMP')+'\\vtup104d3r'
            if not os.path.isdir(sdir):
                os.mkdir(sdir)
            kfile = open(sdir+'\\apikey.vt','w')
            kfile.write(self.apikey)
            kfile.close()

        elif os.name == 'posix':
            sdir = os.getenv('HOME')+'/.vtup104d3r'
            if not os.path.isdir(sdir):
                os.mkdir(sdir)
            kfile = open(sdir+'/apikey.vt','w')
            kfile.write(self.apikey)
            kfile.close()

        # else:
            # print("Session Failed")
        return

    def keepAlive(self,threadno):
        while 1:
            self.alive=vtapi.checkconnection()
            # print(self.alive)
            if not self.alive:
                time.sleep(1)

    def noConn(self):
        alert = QtWidgets.QWidget()
        alert.setWindowIcon(self.icon)
        QtWidgets.QMessageBox.about(alert, "Alert", "No Internet !")