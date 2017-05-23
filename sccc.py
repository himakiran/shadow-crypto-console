from PySide.QtGui import *
from PySide.QtCore import *
import sys
import socket
import gnupg

# Shadows Functions
import functions

# GUI
import mainWindow

# Globals
gpg = gnupg.GPG(gnupghome='~/.gnupg')

class MainDialog(QMainWindow, mainWindow.Ui_mainSCCC):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.statusbar.showMessage('---===:::Shadow Crypto Console [v1.0]:::===--- '
                                   '[http://shadowsgovernment.com]', timeout=0)

        # Connections
        self.connect(self.btnEncrypt, SIGNAL("clicked()"), self.encrypt_message)
        self.connect(self.btnConnect, SIGNAL("clicked()"), self.send_message)
        self.connect(self.btnListGPGKeys, SIGNAL("clicked()"), self.list_gpg_public_keys)
        self.connect(self.btnImportGPGKey, SIGNAL("clicked()"), self.import_gpg_key)
        self.connect(self.btnDeleteGPGKey, SIGNAL("clicked()"), self.delete_gpg_key)
        self.connect(self.btnClearGPGLog, SIGNAL("clicked()"), self.clear_gpg_log)
        self.connect(self.menuClearLog, SIGNAL("triggered()"), self.clear_sys_log)
        self.connect(self.menuExit, SIGNAL("triggered()"), self.exit_system)


        # Function Calls
        self.populate_recipients()
        self.tabControl.setCurrentIndex(0)

    def popup_error(self, msg):
        title = 'Shadow Crypto Console'
        QMessageBox.critical(self, title, msg, QMessageBox.Ok)

    def popup_input(self, msg):
        title = 'Shadow Crypto Console'
        result = QInputDialog.getText(self, title, msg)
        return result

    def clear_sys_log(self):
        self.txtLog.clear()

    def clear_gpg_log(self):
        self.txtGPGLog.clear()

    def exit_system(self):
        app.exit()

    def encrypt_message(self):
        self.txtLog.clear()
        recipient = self.comboRecipients.currentText()
        unencrypted_string = str(self.txtMessagePlain.toPlainText())
        encrypted_data = gpg.encrypt(unencrypted_string, str(recipient))
        self.txtMessageCrypt.setText(str(encrypted_data))
        self.txtLog.append('--> Message encryption status successful? :' + str(encrypted_data.ok) + '\n')
        self.crypto = encrypted_data
        self.txtLog.append(str(encrypted_data))
        self.tabControl.setCurrentIndex(0)

        if not encrypted_data.status:
            self.popup_error('Crypto Trust Error: Read System Log')
            self.tabControl.setCurrentIndex(0)
            self.txtLog.append('--> Encryption Status to ' + str(recipient) + ' failed\r')
            # self.txtLog.append('--> ERROR ' + str(encrypted_data.stderr) + '\r')
            self.txtLog.append('--> Shadow Crypto Chat System requires that the public keys of '
                               'recipients have a GPG trust level of Ultimate to encrypt messages'
                               ' using this application.\r')
            self.txtLog.append('--> The public key for ' + recipient + ' you have selected does not have an Ultimate '
                               'trust level of (5)\r')
            self.txtLog.append('--> If you are absolutely sure that the recipient owns the public key, you must'
                               ' execute the following command(s) in a terminal\r')
            self.txtLog.append('--> gpg --edit-key ' + recipient + '\r')
            self.txtLog.append('--> At the gpg> prompt type the word \"trust\", wait for the list of trust levels '
                               'and then type the number 5 (Ultimate Trust), the system will ask you to type'
                               ' Y or N, once back at the gpg> prompt; type the word \"save\"\r')
            self.txtLog.append('--> You may now encrypt message(s) to ' + recipient + '. This is a security precaution'
                               ' to guarantee that Shadow Crypto Chat knows that you trust the recipient key\r')
        else:
            self.txtLog.append('--> Encryption Status to ' + str(recipient) + '  : ' + str(encrypted_data.status) + '\r')
            self.txtLog.append('--> Message prepared to send to host \r')

    def list_gpg_public_keys(self):
        self.tabControl.setCurrentIndex(2)
        public_keys = gpg.list_keys()
        count = len(public_keys)
        self.txtGPGLog.append('--> GPG Database Contains : ' + str(count) + ' Public Key(s) / Recipients\n')

        for i in range(0, count):
            final = functions.find_between(str(public_keys[i]['uids']), '<', '>')
            self.txtGPGLog.append(final)
            self.txtGPGLog.append(str(public_keys[i]['uids']) + '\n\tFingerprint: ' + str(public_keys[i]['fingerprint'] + '\n'))
        self.txtGPGLog.setTextColor('Green')
        self.txtGPGLog.append('\n-------------------------------------------------------------------- [CMD LIST KEYS SUCCESSFUL]')
        self.txtGPGLog.setTextColor('White')

    def populate_recipients(self):
        public_keys = gpg.list_keys()
        count = len(public_keys)
        for i in range(0, count):
            final = functions.find_between(str(public_keys[i]['uids']), '<', '>')
            self.comboRecipients.addItem(final)

        self.comboRecipients.setCurrentIndex(0)

    def send_message(self):
        host = self.txtHost.text()
        port = self.txtPort.text()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            s.sendall('\n' + str(self.crypto) + '\n')
            s.close()
        except socket.error, v:
                errorcode = v[0]
                if errorcode == socket.errno.ECONNREFUSED:
                    self.txtLog.append('--> The Host has Refused the Connection')
                else:
                    self.txtLog.append('--> Communication Error')

    def import_gpg_key(self):
        fileName = QFileDialog.getOpenFileName(self, 'Select Key File', '/home')
        key_data = open(fileName[0]).read()
        import_result = gpg.import_keys(key_data)
        self.txtGPGLog.append(str(import_result.results))
        print gpg.export_keys()

    def delete_gpg_key(self):
        result = self.popup_input('Delete Key: Please Enter GPG Fingerprint                    ')
        key = gpg.gen_key(gpg.gen_key_input())
        fp = key.fingerprint
        # gpg.delete_keys(str(fp))
        gpg.delete_keys(str(fp), False)

        if gpg.delete_keys(str(result[0])):
            self.clear_gpg_log()
            self.txtGPGLog.append('\n--------------- [CMD SUCCESSFUL KEY DELETED]\n')
            self.list_gpg_public_keys()
        else:
            self.txtGPGLog.setTextColor('Red')
            self.txtGPGLog.append('\n--------------- [CMD FAILED: KEY FINGERPRINT NOT FOUND]\n')
            self.txtGPGLog.setTextColor('White')


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()

__author__ = 'Shadow | shadowsgovernment.com | social.shadowsgovernment.com'
