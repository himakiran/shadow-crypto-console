# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon May 22 19:53:32 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainSCCC(object):
    def setupUi(self, mainSCCC):
        mainSCCC.setObjectName("mainSCCC")
        mainSCCC.resize(864, 600)
        mainSCCC.setMinimumSize(QtCore.QSize(864, 600))
        mainSCCC.setMaximumSize(QtCore.QSize(864, 600))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        mainSCCC.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainSCCC.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(mainSCCC)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabControl = QtGui.QTabWidget(self.centralwidget)
        self.tabControl.setTabPosition(QtGui.QTabWidget.West)
        self.tabControl.setObjectName("tabControl")
        self.tabMain = QtGui.QWidget()
        self.tabMain.setObjectName("tabMain")
        self.groupConnection = QtGui.QGroupBox(self.tabMain)
        self.groupConnection.setGeometry(QtCore.QRect(10, 0, 791, 65))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupConnection.sizePolicy().hasHeightForWidth())
        self.groupConnection.setSizePolicy(sizePolicy)
        self.groupConnection.setObjectName("groupConnection")
        self.txtHost = QtGui.QLineEdit(self.groupConnection)
        self.txtHost.setGeometry(QtCore.QRect(80, 30, 301, 23))
        self.txtHost.setObjectName("txtHost")
        self.txtPort = QtGui.QLineEdit(self.groupConnection)
        self.txtPort.setGeometry(QtCore.QRect(430, 30, 91, 23))
        self.txtPort.setMaxLength(5)
        self.txtPort.setObjectName("txtPort")
        self.lblHost = QtGui.QLabel(self.groupConnection)
        self.lblHost.setGeometry(QtCore.QRect(10, 30, 64, 21))
        self.lblHost.setObjectName("lblHost")
        self.lblPort = QtGui.QLabel(self.groupConnection)
        self.lblPort.setGeometry(QtCore.QRect(390, 30, 31, 21))
        self.lblPort.setObjectName("lblPort")
        self.btnConnect = QtGui.QPushButton(self.groupConnection)
        self.btnConnect.setGeometry(QtCore.QRect(580, 30, 201, 23))
        self.btnConnect.setObjectName("btnConnect")
        self.line = QtGui.QFrame(self.groupConnection)
        self.line.setGeometry(QtCore.QRect(520, 30, 91, 31))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupLog = QtGui.QGroupBox(self.tabMain)
        self.groupLog.setGeometry(QtCore.QRect(8, 65, 801, 451))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupLog.sizePolicy().hasHeightForWidth())
        self.groupLog.setSizePolicy(sizePolicy)
        self.groupLog.setFlat(False)
        self.groupLog.setObjectName("groupLog")
        self.txtLog = QtGui.QTextEdit(self.groupLog)
        self.txtLog.setGeometry(QtCore.QRect(12, 30, 781, 411))
        self.txtLog.setObjectName("txtLog")
        self.tabControl.addTab(self.tabMain, "")
        self.tabMsg = QtGui.QWidget()
        self.tabMsg.setObjectName("tabMsg")
        self.btnEncrypt = QtGui.QPushButton(self.tabMsg)
        self.btnEncrypt.setGeometry(QtCore.QRect(670, 500, 141, 23))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.lblRecipient = QtGui.QLabel(self.tabMsg)
        self.lblRecipient.setGeometry(QtCore.QRect(400, 180, 81, 21))
        self.lblRecipient.setObjectName("lblRecipient")
        self.txtMessagePlain = QtGui.QTextEdit(self.tabMsg)
        self.txtMessagePlain.setGeometry(QtCore.QRect(10, 30, 801, 111))
        self.txtMessagePlain.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtMessagePlain.setObjectName("txtMessagePlain")
        self.txtMessageCrypt = QtGui.QTextEdit(self.tabMsg)
        self.txtMessageCrypt.setGeometry(QtCore.QRect(10, 210, 801, 281))
        self.txtMessageCrypt.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtMessageCrypt.setReadOnly(True)
        self.txtMessageCrypt.setObjectName("txtMessageCrypt")
        self.lblCrypto = QtGui.QLabel(self.tabMsg)
        self.lblCrypto.setGeometry(QtCore.QRect(10, 170, 211, 21))
        self.lblCrypto.setObjectName("lblCrypto")
        self.lblPlainText = QtGui.QLabel(self.tabMsg)
        self.lblPlainText.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.lblPlainText.setObjectName("lblPlainText")
        self.comboRecipients = QtGui.QComboBox(self.tabMsg)
        self.comboRecipients.setGeometry(QtCore.QRect(480, 180, 331, 23))
        self.comboRecipients.setObjectName("comboRecipients")
        self.tabControl.addTab(self.tabMsg, "")
        self.tabGPG = QtGui.QWidget()
        self.tabGPG.setObjectName("tabGPG")
        self.txtGPGLog = QtGui.QTextEdit(self.tabGPG)
        self.txtGPGLog.setGeometry(QtCore.QRect(10, 40, 801, 481))
        self.txtGPGLog.setReadOnly(True)
        self.txtGPGLog.setObjectName("txtGPGLog")
        self.btnListGPGKeys = QtGui.QPushButton(self.tabGPG)
        self.btnListGPGKeys.setGeometry(QtCore.QRect(10, 10, 121, 25))
        self.btnListGPGKeys.setObjectName("btnListGPGKeys")
        self.btnImportGPGKey = QtGui.QPushButton(self.tabGPG)
        self.btnImportGPGKey.setGeometry(QtCore.QRect(140, 10, 121, 25))
        self.btnImportGPGKey.setObjectName("btnImportGPGKey")
        self.btnDeleteGPGKey = QtGui.QPushButton(self.tabGPG)
        self.btnDeleteGPGKey.setGeometry(QtCore.QRect(270, 10, 121, 25))
        self.btnDeleteGPGKey.setObjectName("btnDeleteGPGKey")
        self.btnClearGPGLog = QtGui.QPushButton(self.tabGPG)
        self.btnClearGPGLog.setGeometry(QtCore.QRect(690, 10, 121, 25))
        self.btnClearGPGLog.setObjectName("btnClearGPGLog")
        self.tabControl.addTab(self.tabGPG, "")
        self.tabAbout = QtGui.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.textEdit = QtGui.QTextEdit(self.tabAbout)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 791, 511))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabControl.addTab(self.tabAbout, "")
        self.verticalLayout.addWidget(self.tabControl)
        mainSCCC.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainSCCC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 22))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuLog = QtGui.QMenu(self.menubar)
        self.menuLog.setObjectName("menuLog")
        mainSCCC.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainSCCC)
        self.statusbar.setObjectName("statusbar")
        mainSCCC.setStatusBar(self.statusbar)
        self.menuListKeys = QtGui.QAction(mainSCCC)
        self.menuListKeys.setObjectName("menuListKeys")
        self.menuClearLog = QtGui.QAction(mainSCCC)
        self.menuClearLog.setObjectName("menuClearLog")
        self.menuExit = QtGui.QAction(mainSCCC)
        self.menuExit.setObjectName("menuExit")
        self.menuMain.addAction(self.menuExit)
        self.menuLog.addAction(self.menuClearLog)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())

        self.retranslateUi(mainSCCC)
        self.tabControl.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainSCCC)

    def retranslateUi(self, mainSCCC):
        mainSCCC.setWindowTitle(QtGui.QApplication.translate("mainSCCC", "Shadow Crypto Console [sCC] v1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.groupConnection.setTitle(QtGui.QApplication.translate("mainSCCC", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.txtHost.setText(QtGui.QApplication.translate("mainSCCC", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.txtPort.setText(QtGui.QApplication.translate("mainSCCC", "9009", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHost.setText(QtGui.QApplication.translate("mainSCCC", "Host/IP", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPort.setText(QtGui.QApplication.translate("mainSCCC", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConnect.setText(QtGui.QApplication.translate("mainSCCC", "Send Message", None, QtGui.QApplication.UnicodeUTF8))
        self.groupLog.setTitle(QtGui.QApplication.translate("mainSCCC", "System Log", None, QtGui.QApplication.UnicodeUTF8))
        self.txtLog.setHtml(QtGui.QApplication.translate("mainSCCC", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">--&gt; <span style=\" color:#4e9a06;\">[sCC] Initializing...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">--&gt; <span style=\" color:#4e9a06;\">System Ready</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabControl.setTabText(self.tabControl.indexOf(self.tabMain), QtGui.QApplication.translate("mainSCCC", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEncrypt.setText(QtGui.QApplication.translate("mainSCCC", "Encrypt >>>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRecipient.setText(QtGui.QApplication.translate("mainSCCC", "Recipient:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtMessagePlain.setHtml(QtGui.QApplication.translate("mainSCCC", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Type your secret message here and select a recipient from the drop down. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Now click the Encrypt Button!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCrypto.setText(QtGui.QApplication.translate("mainSCCC", "<-- Encrypted Message -->", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPlainText.setText(QtGui.QApplication.translate("mainSCCC", "<-- Plain Text -->", None, QtGui.QApplication.UnicodeUTF8))
        self.tabControl.setTabText(self.tabControl.indexOf(self.tabMsg), QtGui.QApplication.translate("mainSCCC", "Crypto", None, QtGui.QApplication.UnicodeUTF8))
        self.btnListGPGKeys.setText(QtGui.QApplication.translate("mainSCCC", "List GPG Keys", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImportGPGKey.setText(QtGui.QApplication.translate("mainSCCC", "Import Key", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeleteGPGKey.setText(QtGui.QApplication.translate("mainSCCC", "Delete Key", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClearGPGLog.setText(QtGui.QApplication.translate("mainSCCC", "Clear Log", None, QtGui.QApplication.UnicodeUTF8))
        self.tabControl.setTabText(self.tabControl.indexOf(self.tabGPG), QtGui.QApplication.translate("mainSCCC", "GPG", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("mainSCCC", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Shadow Crypto Console v1.0a</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-style:italic;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">Shadow Crypto Console is a simple GPG front-end for Linux distributions with bulit in network communication capabilities. sCC [Shadow Crypto Console] is developed ONLY for Linux and its variants, there will never be a Windows version of this application, sorry. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">The prerequisites for this application are:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">    -GPG</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">    -GPG Keyring</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">    -python-gnupg </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">        Arch [pacman -S python-gnupg </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">        Debian [apt-get install python-gnupg]</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shadows Government </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    http://shadowsgovernment.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shadow Social Net     </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    http://social.shadowsgovernment.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shadow News G+     </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    https://plus.google.com/u/0/collection/ky-iQB</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shadow InfoSec G+     </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    https://plus.google.com/u/0/communities/111905196411962990538</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contact:          </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    shadow-corp@shadowsgovernment.com</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabControl.setTabText(self.tabControl.indexOf(self.tabAbout), QtGui.QApplication.translate("mainSCCC", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMain.setTitle(QtGui.QApplication.translate("mainSCCC", "Mai&n", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLog.setTitle(QtGui.QApplication.translate("mainSCCC", "&Log", None, QtGui.QApplication.UnicodeUTF8))
        self.menuListKeys.setText(QtGui.QApplication.translate("mainSCCC", "&List Keys", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClearLog.setText(QtGui.QApplication.translate("mainSCCC", "&Clear Log", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExit.setText(QtGui.QApplication.translate("mainSCCC", "&Exit", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
