from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
import os ,sys
class UI_secondwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("secondwindow.ui", self)
        self.show()




# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UI_secondwindow()
#     sys.exit(app.exec_())




