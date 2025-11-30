from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit,QTableWidget, QMessageBox,QApplication
from PyQt5 import uic
import os ,sys
import pyodbc

class UI_delete_add(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('delete_add.ui', self)

        # label Widgets
        self.label_picdel = self.findChild(QLabel, 'label_picdel')
        self.label_picdisplay = self.findChild(QLabel, 'label_picdisplay')
        self.label_name = self.findChild(QLabel, 'label_name')
        self.label_bid = self.findChild(QLabel, 'label_bid')
        self.label_Title = self.findChild(QLabel, 'label_Title')
        self.label_Borro_by = self.findChild(QLabel, 'label_Borro_by')
        self.label_Bdate = self.findChild(QLabel, 'label_Bdate')
        self.label_due_date = self.findChild(QLabel, 'label_due_date')
        self.label_picadd = self.findChild(QLabel, 'label_picadd')

        self.tableWidget = self.findChild(QTableWidget, "tableWidget")


        # textEdit Widgets
        self.textEdit_bid = self.findChild(QTextEdit, 'textEdit_bid')
        self.textEdit_Title = self.findChild(QTextEdit, 'textEdit_Title')
        self.textEdit_Borrow_by = self.findChild(QTextEdit, 'textEdit_Borrow_by')
        self.textEdit_borrow_date = self.findChild(QTextEdit, 'textEdit_borrow_date')
        self.textEdit_Due = self.findChild(QTextEdit, 'textEdit_Due')
        # PushButton Widgets
        self.pushButton_Delete = self.findChild(QPushButton, 'pushButton_Delete')
        self.pushButton_Display = self.findChild(QPushButton, 'pushButton_Display')
        self.pushButton_Add = self.findChild(QPushButton, 'pushButton_Add')

        self.show()



os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_delete_add()
    sys.exit(app.exec_())
