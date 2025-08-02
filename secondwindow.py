from PyQt5.QtWidgets import QMainWindow,QLabel,QPushButton,QTableWidget,QTableWidgetItem,QApplication
from PyQt5 import uic
import pyodbc
import os ,sys
class UI_secondwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("secondwindow.ui", self)
        # define widgets
        self.pushButton_search = self.findChild(QPushButton, "pushButton_search")
        self.pushButton_deleteadd = self.findChild(QPushButton, "pushButton_deleteadd")
        self.pushButton_display = self.findChild(QPushButton, "pushButton_display")
        self.tableWidget = self.findChild(QTableWidget, "tableWidget")
        self.label_pix = self.findChild(QLabel, "label_pix")
        self.label = self.findChild(QLabel, "label")
        # connect to buttons
        self.pushButton_display.clicked.connect(self.display)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_deleteadd.clicked.connect(self.deleteadd)
        self.show()
    def connect_to_db(self):
            conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=localhost;'
                'DATABASE=Library;'
                'Trusted_Connection=yes;'
            )
            return conn
    def display(self):
        try:
            conn = self.connect_to_db()
            cursor = conn.cursor()
            cursor.execute('''SELECT 
    B.book_id,
    B.title,
    U.name AS borrowed_by,
    BR.borrow_date,
    BR.due_date
FROM Books B
JOIN Borrowings BR ON B.book_id = BR.book_id
JOIN Users U ON BR.user_id = U.user_id
WHERE BR.return_date IS NULL;''')
            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels([
                'book_id', 'title', 'borrowed_by', 'borrow_date', 'due_date'
            ])
            for row_idx, row_data in enumerate(result):
                self.tableWidget.insertRow(row_idx)
                for col_idx, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

            cursor.close()
            conn.close()

        except Exception as e:
            print(e,"ERROR to load database")
    def search(self):
        pass
    def deleteadd(self):
        pass


# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UI_secondwindow()
#     sys.exit(app.exec_())




