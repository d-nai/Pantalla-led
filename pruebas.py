from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import sys

class ventanaLol(QMainWindow):
    def setupUi(self):
        self.setFixedSize(500,330)
        self.setStyleSheet("background: #242526;")

        self.frameTitulo = QFrame(self)
        self.frameTitulo.setGeometry(10,10,480, 100)
        self.frameTitulo.setStyleSheet("background: #0CA8AC;")

        self.titulo = QLabel(self.frameTitulo)
        self.titulo.setText("queeeeeeeeeeeeeeeeeeeeeeee")
        self.titulo.setGeometry(0,0,480,40)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.titulo.setStyleSheet("background: white; color: black; font-size: 25px; font-weight: bold;")


        self.inputs = QFrame(self)
        self.inputs.setGeometry(10,120,480, 200)
        self.inputs.setStyleSheet("background: #0CA8AC;")

        self.input = QLineEdit(self.inputs)
        self.input.setGeometry(10, 70, 460, 45)
        self.input.setStyleSheet("background: white;")

        self.boton = QPushButton(self.inputs)
        self.boton.setText("Apretame")
        self.boton.setGeometry(10,125,460,45)
        self.boton.clicked.connect(self.cambiarColorVentana)
        self.boton.clicked.connect(self.mostrarDialogo)

        self.dialogo = QDialog(self)
        self.dialogo.setFixedSize(300,300)
        

    def obtenerTexto(self):
        print(self.input.text())

    def mostrarDialogo(self):
        self.dialogo.show()

    def cambiarColorVentana(self):
        color = self.input.text()

        self.frameTitulo.setStyleSheet(f"background: {color};")
        self.dialogo.setStyleSheet(f"background: {color};")
app = QApplication(sys.argv)

ventana = ventanaLol()
ventana.setupUi()
ventana.show()

sys.exit(app.exec_())