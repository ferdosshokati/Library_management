# login_window.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit, QMessageBox,QApplication
from PyQt5 import uic
import os ,sys
import pyodbc
from secondwindow import UI_secondwindow

class UI_Managers(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("managers.ui", self)

        self.label_user = self.findChild(QLabel, "label_user")
        self.label_password = self.findChild(QLabel, "label_password")
        self.textEdit_user = self.findChild(QTextEdit, "textEdit_user")
        self.textEdit_password = self.findChild(QTextEdit, "textEdit_password")
        self.pushButton_submituser = self.findChild(QPushButton, "pushButton_submituser")
        self.pushButton_submituser.clicked.connect(self.submituser)
        self.show()

    def connect_to_db(self):
            conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=localhost;'
                'DATABASE=Library;'
                'Trusted_Connection=yes;'
            )
            return conn

            return None

    def submituser(self):
        try:
            username = self.textEdit_user.toPlainText().strip()
            password = self.textEdit_password.toPlainText().strip()

            # print(f"🔍 ورود کاربر: {username} / {password}")

            # connect to database
            conn = self.connect_to_db()
            if not conn:
                QMessageBox.critical(self, "error", "connect to database failed")
                return

            cursor = conn.cursor()

            query = "SELECT * FROM dbo.Admin WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                try:
                    self.second_window = UI_secondwindow()
                    self.second_window.show()
                    self.hide()  # یا self.close() بسته به نیاز
                except Exception as e:
                    print("❌ error from opening second window:", e)
            else:
                print("❌ wrong data")

            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "error", f"error:\n{e}")


os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_Managers()
    window.show()
    sys.exit(app.exec_())