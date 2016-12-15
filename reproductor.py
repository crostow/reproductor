# -*- coding: utf-8 -*-
#-----------------------------------
# Programa: Reproductor de video
#-----------------------------------
# Autor: Abuelazo
#-----------------------------------
# fecha: 12/12/2016
#-----------------------------------


# importamos lbrerias necesarias
import sys
from functools import partial
from PyQt5.QtCore import QEvent, QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from pantalla import reproductor
from metodos import iconos, repro

# clase heredada de QmainWindow(constructor de ventanas)
class Reproductor_video(QMainWindow):
    # metodo constructor de clase
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        # cargamos el archivo .py grafico
        self.ui = reproductor.Ui_MainWindow()
        self.ui.setupUi(self)

        self.pp = 0

        # conectamos los elementos graficos con los metodos
        self.ui.menu_abrir.triggered.connect(self.abrir)
        self.ui.menu_salir.triggered.connect(self.salir)
        self.ui.play.clicked.connect(self.play_pausa)
        self.ui.stop.clicked.connect(self.alto)

        # mandamos a llamar el metodo iconos
        iconos.iconos(self)
        #mandamos a llamar la configuracion del reproductor
        repro.conf_basico(self)


    #metodo para abrir un video
    def abrir(self):
        repro.abrir(self)

    # metodo para pausar o reproducir video
    def play_pausa(self):
        if self.pp == 0:
            repro.pausa(self)
            self.pp = 1
        else:
            repro.play(self)
            self.pp = 0

    # metodo para detener el video
    def alto(self):
        repro.stop(self)






    #metodo para salir de la aplicacion
    def salir(self):
        self.close()

# codigo para lanzar aplicacíon
if __name__ == "__main__":
    # instancia para iniciar una plicacíon
    app = QApplication(sys.argv)
    # crear un objeto de la clase
    ventana = Reproductor_video()
    # mostrar la ventana
    ventana.show()
    # ejecutamos la aplicacion
    sys.exit(app.exec())

