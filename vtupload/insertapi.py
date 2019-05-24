from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.apikey=""

    def setupUi(self, Form,api):
        self.apikey = api
        Form.setObjectName("Form")
        Form.resize(700, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 150))
        Form.setMaximumSize(QtCore.QSize(700, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setMouseTracking(True)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 100, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 700, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 550, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEditOld = QtWidgets.QLineEdit(Form)
        self.lineEditOld.setGeometry(QtCore.QRect(120, 17, 550, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditOld.setFont(font)
        self.lineEditOld.setFrame(False)
        self.lineEditOld.setReadOnly(True)
        self.lineEditOld.setObjectName("lineEditOld")
        self.textBrowser.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEditOld.raise_()
        self.pushButton.clicked.connect(self.getKey)
        self.pushButton.clicked.connect(Form.accept)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Insert API Key"))
        self.pushButton.setText(_translate("Form", "Insert"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    In Use      :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Insert Key :</span></p></body></html>"))
        self.lineEditOld.setText(_translate("Form", self.apikey))


    def getKey(self):
        self.apikey = self.lineEdit.text()