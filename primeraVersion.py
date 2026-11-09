from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import sys
import json

class ventanaPrincipal(QMainWindow):
    def ventanaBase(self):
        self.matrizPixeles = [
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
        ]

        self.matrizBotones = []
        self.colorActual = "#FFFFFF"
        self.setBaseSize(700,700)
        self.setStyleSheet("background: #F8F3EE;")

        self.layoutGeneral = QVBoxLayout()
        self.layoutGeneral.setContentsMargins(8, 8, 8, 8)

        self.barraSuperior = QFrame()
        self.barraSuperior.setStyleSheet("background: #EADBD0; border-radius: 15px;")

        self.cuadrosPrincipales = QFrame()
        self.cuadrosPrincipales.setStyleSheet("background: #F8F3EE;")

        self.setupBarraSuperior()
        self.setupCuadrosPrincipales()

        self.layoutGeneral.addWidget(self.barraSuperior,12)
        self.layoutGeneral.addWidget(self.cuadrosPrincipales,88)

        self.widgetPrincipal = QWidget()
        self.widgetPrincipal.setLayout(self.layoutGeneral)
        self.setCentralWidget(self.widgetPrincipal)

    def setupBarraSuperior(self):
        self.layoutBarraSuperior = QHBoxLayout(self.barraSuperior)

        self.titulo = QLabel("FastLED Pixel Studio")
        self.titulo.setStyleSheet(
            'font-family: "Pixelify Sans"; font-size: 50px; font-weight: bold;'
        )

        self.frameBotonesArchivo = QFrame(self.barraSuperior)
        self.layoutBotonesArchivo = QHBoxLayout(self.frameBotonesArchivo)

        self.botonNuevoArchivo = QPushButton()
        self.botonNuevoArchivo.clicked.connect(self.nuevoArchivo)
        
        self.botonAbrirArchivo = QPushButton()
        self.botonAbrirArchivo.clicked.connect(self.abrirArchivo)
        
        self.botonGuardarArchivo = QPushButton()
        self.botonGuardarArchivo.clicked.connect(self.guardarArchivo)
        
        self.botonBorrarArchivo = QPushButton()
        self.botonBorrarArchivo.clicked.connect(self.borrarCuadricula)

        carpeta_iconos = Path(__file__).parent / "icons"

        self.botonNuevoArchivo.setIcon(QIcon(str(carpeta_iconos / "archivoNuevo.png")))
        self.botonAbrirArchivo.setIcon(QIcon(str(carpeta_iconos / "abrirArchivo.png")))
        self.botonGuardarArchivo.setIcon(QIcon(str(carpeta_iconos / "guardarArchivo.png")))
        self.botonBorrarArchivo.setIcon(QIcon(str(carpeta_iconos / "borrarArchivo.png")))

        for boton in (
            self.botonNuevoArchivo,
            self.botonAbrirArchivo,
            self.botonGuardarArchivo,
            self.botonBorrarArchivo,
        ):
            boton.setIconSize(QSize(28, 28))

        for boton in (
            self.botonNuevoArchivo,
            self.botonAbrirArchivo,
            self.botonGuardarArchivo,
            self.botonBorrarArchivo,
        ):
            boton.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Expanding,
            )
            self.layoutBotonesArchivo.addWidget(boton, 1)

        self.layoutBarraSuperior.addWidget(self.titulo, 60)
        self.layoutBarraSuperior.addWidget(self.frameBotonesArchivo, 30)

    def setupCuadrosPrincipales(self):
        self.layoutCuadrosPrincipales = QHBoxLayout(self.cuadrosPrincipales)
        self.layoutCuadrosPrincipales.setContentsMargins(0, 0, 0, 0)

        self.framePaleta = QFrame()
        self.framePaleta.setStyleSheet("background: #EADBD0; border-radius: 15px;")
        self.setupPaleta()

        self.frameLienzo = QFrame()
        self.frameLienzo.setStyleSheet("background: #F3E9DF; border-radius: 15px;")
        self.setupLienzo()

        self.layoutCuadrosPrincipales.addWidget(self.framePaleta, 15)
        self.layoutCuadrosPrincipales.addWidget(self.frameLienzo,85)

    def setupPaleta(self):
        self.layoutPaleta = QVBoxLayout(self.framePaleta)

        self.textoPaleta = QLabel("Paleta")
        self.textoPaleta.setStyleSheet('font-family: "Acme"; font-size: 40px;')
        self.textoPaleta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.frameColores = QFrame()
        self.layoutColores = QGridLayout(self.frameColores)

        self.boton1 = QPushButton()
        self.boton1.setFixedSize(50,50)
        self.boton1.setStyleSheet("""
            QPushButton {background: #FF2B00; border-radius: 25px;}

            QPushButton:hover {border: 3px solid #35424A;}
        
        """)
        self.boton1.setProperty("color", "#FF2B00")

        self.boton2 = QPushButton()
        self.boton2.setFixedSize(50,50)
        self.boton2.setStyleSheet("""
            QPushButton {background: #FFA600; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton2.setProperty("color", "#FFA600")
        
        self.boton3 = QPushButton()
        self.boton3.setFixedSize(50,50)
        self.boton3.setStyleSheet("""
            QPushButton {background: #FAFF54; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton3.setProperty("color", "#FAFF54")

        self.boton4 = QPushButton()
        self.boton4.setFixedSize(50,50)
        self.boton4.setStyleSheet("""
            QPushButton {background: #8DFF54; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton4.setProperty("color", "#8DFF54")

        self.boton5 = QPushButton()
        self.boton5.setFixedSize(50,50)
        self.boton5.setStyleSheet("""
            QPushButton {background: #5470FF; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton5.setProperty("color", "#5470FF")

        self.boton6 = QPushButton()
        self.boton6.setFixedSize(50,50)
        self.boton6.setStyleSheet("""
            QPushButton {background: #C354FF; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton6.setProperty("color", "#C354FF")

        self.boton7 = QPushButton()
        self.boton7.setFixedSize(50,50)
        self.boton7.setStyleSheet("""
            QPushButton {background: #FFFFFF; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton7.setProperty("color", "#FFFFFF")

        self.boton8 = QPushButton()
        self.boton8.setFixedSize(50,50)
        self.boton8.setStyleSheet("""
            QPushButton {background: #000000; border-radius: 25px;}
            QPushButton:hover {border: 3px solid #35424A;}
        """)
        self.boton8.setProperty("color", "#000000")

        for boton in (self.boton1, self.boton2, self.boton3, self.boton4, self.boton5, self.boton6, self.boton7, self.boton8):
            boton.clicked.connect(self.cambiarColorActualBoton)


        self.layoutColores.addWidget(self.boton1,1,1)
        self.layoutColores.addWidget(self.boton2,1,2)
        self.layoutColores.addWidget(self.boton3,2,1)
        self.layoutColores.addWidget(self.boton4,2,2)
        self.layoutColores.addWidget(self.boton5,3,1)
        self.layoutColores.addWidget(self.boton6,3,2)
        self.layoutColores.addWidget(self.boton7,4,1)
        self.layoutColores.addWidget(self.boton8,4,2)

        self.tituloColorActual = QLabel(self.colorActual)
        self.tituloColorActual.setStyleSheet('font-family: "Jetbrains Mono"; font-weight: bold;')

        self.frameColorActual = QPushButton()
        self.frameColorActual.clicked.connect(self.seleccionarColor)
        self.frameColorActual.setStyleSheet("border-radius: 20px; background: white;")
        self.frameColorActual.setMinimumHeight(150)

        self.colorHex = QLineEdit(placeholderText= "Color Hexadecimal")
        self.colorHex.setStyleSheet('background: #D9B79F; font-family: "Jetbrains Mono"; font-weight: bold; border-radius: 20px;')
        self.colorHex.returnPressed.connect(self.cambiarColorActualTexto)

        self.layoutPaleta.addWidget(self.textoPaleta)
        self.layoutPaleta.addWidget(self.frameColores)
        
        self.layoutPaleta.addStretch()
        
        self.layoutPaleta.addWidget(self.tituloColorActual)
        self.layoutPaleta.addWidget(self.frameColorActual)
        self.layoutPaleta.addWidget(self.colorHex)

    def cambiarColorActualBoton(self):
        boton = self.sender()
        color = boton.property("color")
        self.frameColorActual.setStyleSheet(f"background: {color};border-radius: 20px;") 

        self.colorActual = color
        self.tituloColorActual.setText(self.colorActual)

    def cambiarColorActualTexto(self):
            color = self.colorHex.text()

            deteccion = 0
            for caracter in color:
                if caracter not in ("#ABCDEF0123456789") or len(color) != 7:
                    deteccion = 1

            if deteccion == 0:
                self.frameColorActual.setStyleSheet(f"background: {color};border-radius: 20px;")
                self.colorActual = color
                self.tituloColorActual.setText(self.colorActual)
            else:
                print("no")

    def setupLienzo(self):
        self.layoutLienzo = QVBoxLayout(self.frameLienzo)

        self.tituloLienzo = QLabel("Lienzo 8x8")
        self.tituloLienzo.setStyleSheet('font-size: 40px; font-family: "Acme"; font-weight: bold;')
        self.tituloLienzo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.framePixeles = QFrame()
        self.layoutPixeles = QGridLayout(self.framePixeles)
        self.layoutPixeles.setSizeConstraint( QLayout.SizeConstraint.SetFixedSize)
        self.layoutPixeles.setHorizontalSpacing(5)
        self.layoutPixeles.setVerticalSpacing(5)

        self.pixeles = []

        for fila in range(8):
            filaPixeles = []
            filaBotones = []

            for columna in range(8):
                pixel = QPushButton()
                filaBotones.append(pixel)
                pixel.setProperty("posicionX", int(fila))
                pixel.setProperty("posicionY", int(columna))
                pixel.setProperty("color", "#FFFFFF")
                pixel.setFixedSize(55, 55)
                pixel.setStyleSheet("""
                    QPushButton {background: white; border: none; padding: 0px;}
                    QPushButton:hover {border: 3px solid #35424A;}
                """)
                pixel.clicked.connect(self.cambiarColorPixel)
                self.layoutPixeles.addWidget(pixel, fila, columna)
                filaPixeles.append(pixel)

            self.pixeles.append(filaPixeles)
            self.matrizBotones.append(filaBotones)

        self.botonExportar = QPushButton("EXPORTAR")
        self.botonExportar.clicked.connect(self.exportarCodigo)
        self.botonExportar.setStyleSheet("""
            QPushButton {font-size: 40px; font-family: "Acme"; background: #C98B70; color: white;}
        QPushButton:hover {background: #B4765B;}
        """)
        self.botonExportar.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.layoutLienzo.addWidget(self.tituloLienzo,10)
        self.layoutLienzo.addWidget(self.framePixeles,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layoutLienzo.addWidget(self.botonExportar,10)

    def cambiarColorPixel(self): # Esta va a actualizar la matriz interna
        pixel = self.sender()
        
        posicionX = pixel.property("posicionX")
        posicionY = pixel.property("posicionY")
        
        self.matrizPixeles[posicionX][posicionY] = self.colorActual
        
        self.pintarPixel(posicionX, posicionY, self.colorActual)
    
    def pintarPixel(self, posx, posy, color): # Esta va a actualizar la informacion en pantalla
        self.matrizBotones[posx][posy].setStyleSheet(f"""
            QPushButton {{background: {color}}}
            QPushButton:hover {{border: 3px solid #35424A;}}
        """)
    
    def borrarCuadricula(self):
        for i in range(8):
            for j in range(8):
                self.matrizPixeles[i][j] = "#FFFFFF"
                self.pintarPixel(i,j,"#FFFFFF")
    
    def nuevoArchivo(self):
        mensaje = QMessageBox()
        
        mensaje.setWindowTitle("Nuevo archivo")
        mensaje.setText("¿Quieres borrar el pixel art actual?")
        
        mensaje.setStandardButtons(
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        
        mensaje.setStyleSheet("""
                                QMessageBox {
                                    background-color: #F1E7DE;
                                }
                                
                                QLabel {
                                    color: #000000;
                                    font-size: 14px;
                                }
                                
                                QPushButton {
                                    background-color: #EEDCD0;
                                    color: #624839;
                                    padding: 6px 12px;
                                }
                                
                                QPushButton:hover {
                                    background-color: #D4D2D7;
                                }
                                """)
        
        respuesta = mensaje.exec()
        
        if respuesta == QMessageBox.StandardButton.Yes:
            self.borrarCuadricula()
        
    def guardarArchivo(self):
        ruta, filtro = QFileDialog.getSaveFileName(
            self,
            "Guardar pixel art",
            "",
            "Archivos JSON (*.json)"
        )
        
        if ruta != "":
            with open(ruta, "w") as archivo:
                json.dump(self.matrizPixeles,archivo, indent=4)
        
    def abrirArchivo(self):
        ruta, filtro = QFileDialog.getOpenFileName(
            self,
            "Abrir pixel art",
            "",
            "Archivos JSON (*.json)"
        )
        
        if ruta != "":
            with open(ruta,"r") as archivo:
                self.matrizPixeles = json.load(archivo)
                self.rellenarCuadricula()
                
    def rellenarCuadricula(self):
        for i in range(8):
            for j in range(8):
                color = self.matrizPixeles[i][j]
                self.pintarPixel(i,j,color)

    def seleccionarColor(self):
        dialogo = QColorDialog(self.colorActual, self)
        dialogo.setWindowTitle("Seleccionar color")

        dialogo.setStyleSheet("""
            QColorDialog {
                background-color: #F1E7DE;
            }

            QLabel {
                color: #000000;
            }

            QPushButton {
                background-color: #D9B79F;
                color: #000000;
                padding: 6px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #C99A80;
            }

            QLineEdit {
                background-color: white;
                color: black;
            }

            QSpinBox {
                background-color: white;
                color: black;
            }
        """)

        if dialogo.exec():
            color = dialogo.currentColor()

            if color.isValid():
                self.colorActual = color.name().upper()

                self.frameColorActual.setStyleSheet(
                    f"background: {self.colorActual}; border-radius: 20px;"
                )

                self.tituloColorActual.setText(self.colorActual)
    
    def exportarCodigo(self):
        matrizLeds = []
        
        for i in range(8):
            fila = []
            for j in range(8):
                fila.append(self.matrizPixeles[i][j])
            if i % 2 == 1:
                fila.reverse()
            matrizLeds.append(fila)
        
        
        texto, aceptado = QInputDialog.getText(
            self,
            "Exportar código",
            "Nombre del Pixel Art (sin espacios): "
        )
        
        if aceptado and " " not in texto:
            nombrePixelArt = texto
            
            codigoExportado = f"void {nombrePixelArt}()" + "{\n"
            
            numeroLED = 0
            for i in range(8):
                for j in range(8):
                    codigoExportado += f"\tleds[{numeroLED}] = CRGB" + f"{self.hexARGB(matrizLeds[i][j])};\n"
                    numeroLED += 1
            
            codigoExportado += "\n\tFastLED.show();\n"
            codigoExportado += "}"
            
            print(codigoExportado)
            
            portapapeles = QApplication.clipboard()
            portapapeles.setText(codigoExportado)
            
            QMessageBox.information(
                self,
                "Codigo exportado",
                "El codigo se copio correctamente al portapapeles."
            )
        
        elif aceptado and " " in texto:
            print("Titulo invalido")
            QMessageBox.warning(
                self,
                "Error",
                "El nombre es inválido."
            )
        
    
    def hexARGB(self, color):
        r = int(color[1:3],16)
        g = int(color[3:5],16)
        b = int(color[5:],16)
        
        rgb = r, g, b
        
        return str(rgb)



colorActual = "#FFFFFF"

app = QApplication(sys.argv)

app.setStyleSheet("""
        QMainWindow {
        background-color: #F1E7DE;
    }


    /* ===== TEXTOS ===== */

    QLabel {
        color: #624839;
        font-family: "JetBrains Mono";
        font-weight: bold;
    }


    /* ===== BOTONES ===== */

    QPushButton {
        background-color: #D9B79F;
        color: #624839;

        font-family: "JetBrains Mono";
        font-weight: bold;

        border: none;
        border-radius: 10px;

        padding: 6px;
    }

    QPushButton:hover {
        background-color: #D4D2D7;
    }

    QPushButton:pressed {
        background-color: #C99A80;
    }


    /* ===== CAMPOS DE TEXTO ===== */

    QLineEdit {
        background-color: #D9B79F;
        color: #624839;

        font-family: "JetBrains Mono";
        font-weight: bold;

        border: none;
        border-radius: 20px;

        padding: 6px 10px;
    }

    QLineEdit:focus {
        border: 2px solid #624839;
    }


    /* ===== FRAMES ===== */

    QFrame {
        background-color: #F1E7DE;
    }


    /* ===== DIÁLOGOS ===== */

    QDialog {
        background-color: #F1E7DE;
        color: #624839;
    }

    QMessageBox {
        background-color: #F1E7DE;
    }

    QMessageBox QLabel {
        color: #624839;
    }

    QMessageBox QPushButton {
        min-width: 70px;
    }
""")

si = ventanaPrincipal()
si.ventanaBase()
si.show()

sys.exit(app.exec())
