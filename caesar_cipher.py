import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://localhost:5000/api/caesar/encrypt"
        payload={
            "plain_text": self.ui.plainTextEdit.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data=response.json()
                self.ui.plainTextEdit_3.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption success")
                msg.exec_()
            else:
                print("error while calling api")
        except requests.exceptions.RequestException as e:
            print("Error:%s" % e.message)
    def call_api_decrypt(self):
        url = "http://localhost:5000/api/caesar/decrypt"
        payload={
            "cipher_text": self.ui.plainTextEdit_3.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data=response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption success")
                msg.exec_()
            else:
                print("error while calling api")
        except requests.exceptions.RequestException as e:
            print("Error:%s" % e.message)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())