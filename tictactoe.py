from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys

class Menu(QMainWindow):
    def setup_ui(self):
        self.size = QSize(350,500)

        self.layoutPrincipal = QVBoxLayout()

        self.frameTitulo = QFrame()
        self.frameTitulo.setStyleSheet("background: black;")

        self.frameInputs = QFrame()
        self.frameInputs.setStyleSheet("background: black;")

        self.layoutPrincipal.addWidget(self.frameTitulo,30)
        self.layoutPrincipal.addWidget(self.frameInputs,70)

        self.widget = QWidget()
        self.widget.setLayout(self.layoutPrincipal)

        self.setCentralWidget(self.widget)




app = QApplication(sys.argv)

Menu = Menu()
Menu.setup_ui()
Menu.show()

sys.exit(app.exec())

