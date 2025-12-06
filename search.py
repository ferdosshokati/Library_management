import sys,os
import pyodbc
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QTableWidget,QMainWindow,QLabel,QPushButton,QTextEdit

class UI_Search(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('search.ui',self)

        # define widgets
        self.labelpicsearch = self.findChild(QLabel,'labelpicsearch')
        self.label_user = self.findChild(QLabel,'label_user')
        self.label = self.findChild(QLabel,'label')
        self.pushButton_Display = self.findChild(QPushButton,'pushButton_Display')
        self.tableWidget = self.findChild(QTableWidget,'tableWidget')
        self.textEdit_search = self.findChild(QTextEdit,'textEdit_search')

        self.show()


os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_Search()
    sys.exit(app.exec_())