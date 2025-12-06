from PyQt5.QtWidgets import (QMainWindow, QLabel, QPushButton, QTextEdit,QTableWidget, QMessageBox,QApplication,
                             QTableWidgetItem)
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
        self.label_User_Id = self.findChild(QLabel, 'label_User_Id')
        self.label_due = self.findChild(QLabel, 'label_due')
        self.label_Bdate = self.findChild(QLabel, 'label_Bdate')
        self.label_return = self.findChild(QLabel, 'label_return')
        self.label_picadd = self.findChild(QLabel, 'label_picadd')

        self.tableWidget = self.findChild(QTableWidget, "tableWidget")


        # textEdit Widgets
        self.textEdit_bid = self.findChild(QTextEdit, 'textEdit_bid')
        self.textEdit_user_id = self.findChild(QTextEdit, 'textEdit_user_id')
        self.textEdit_due_date = self.findChild(QTextEdit, 'textEdit_due_date')
        self.textEdit_borrow_date = self.findChild(QTextEdit, 'textEdit_Borrow_date')
        self.textEdit_return = self.findChild(QTextEdit, 'textEdit_return')
        # PushButton Widgets
        self.pushButton_Delete = self.findChild(QPushButton, 'pushButton_Delete')
        self.pushButton_Display = self.findChild(QPushButton, 'pushButton_Display')
        self.pushButton_Add = self.findChild(QPushButton, 'pushButton_Add')
        self.pushButton_Add.clicked.connect(self.Add)
        self.pushButton_Delete.clicked.connect(self.Delete)
        self.pushButton_Display.clicked.connect(self.Display)

        self.show()

    # connect to db
    def connect_to_db(self):
        try:
            conn = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=localhost;"
                "Database=Library;"
                "Trusted_Connection=yes;"
            )
            return conn
        except Exception as e:
            QMessageBox.critical(self, "DB Error", str(e))
            return None

    def Add(self):
        book_id = int(self.textEdit_bid.toPlainText().strip())
        user_id = int(self.textEdit_user_id.toPlainText().strip())
        borrow_date = self.textEdit_borrow_date.toPlainText().strip()
        due_date = self.textEdit_due_date.toPlainText().strip()
        return_date = self.textEdit_return.toPlainText().strip()

        if return_date == '':
            return_date = None

        try:
            conn = self.connect_to_db()
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO dbo.Borrowings
            ([book_id],[user_id],[borrow_date],[due_date],[return_date]) VALUES (?,?,?,?,?)"""
                           , (book_id,user_id,borrow_date,due_date,return_date))

            conn.commit()
            cursor.close()
            conn.close()
            print("data added successfully")
        except Exception as e:
            print("error in add data", e)

        self.Display()

    def Delete(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row < 0:
                QMessageBox.warning(self,"Warning","please choose a Row")
                return
            book_id = self.tableWidget.item(selected_row,0).text()
            user_id = self.tableWidget.item(selected_row,1).text()
            borrow_date = self.tableWidget.item(selected_row,2).text()


            reply = QMessageBox.question(
                self,
                "Confirm Delete",
                f" Are you sure you want to delete this record?\n\n"
                f"Book ID: {book_id}\nUser ID: {user_id}\nBorrow Date: {borrow_date}",
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply != QMessageBox.Yes:
                return

            conn = self.connect_to_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dbo.Borrowings WHERE book_id = ? AND user_id = ? AND borrow_date = ?", (book_id,user_id,borrow_date))
            conn.commit()

            cursor.close()
            conn.close()

            QMessageBox.information(self,"Success","record deleted successfully" )

            self.Display()

        except Exception as e:
            QMessageBox.critical(self, "DB Error", str(e))


    def Display(self):
        try:
            conn = self.connect_to_db()
            if not conn:
                return
            cursor = conn.cursor()
            cursor.execute("SELECT Book_id,user_id,borrow_date,due_date,return_date FROM dbo.Borrowings")
            results = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(len(results[0]))
            self.tableWidget.setHorizontalHeaderLabels([
                "Book id", "user id", "borrow_date", "due date", "return date"
            ])

            for row_idx, row_data in enumerate(results):
                self.tableWidget.insertRow(row_idx)
                for col_idx, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

            cursor.close()
            conn.close()
        except Exception as e:
            print("error in uploading data:", e)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to display: {e}")


os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_delete_add()
    sys.exit(app.exec_())
