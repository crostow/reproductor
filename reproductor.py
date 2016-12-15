# -*- coding: utf-8 -*-
#-----------------------------------
#Programa: Reproductor de video
#-----------------------------------
#Autor: Abuelazo
#-----------------------------------
#fecha: 12/12/2016


#importamos lbrerias necesarias
import sys
from functools import partial

from PyQt5.QtCore import QEvent, QUrl, Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,
                             QWidget, QPushButton, QSlider,
                             QVBoxLayout)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from pantalla import reproductor
from metodos import iconos

#clase heredada de QmainWindow(constructor de ventanas)
class Reproductor_video(QMainWindow):
    #metodo constructor de clase
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        #cargamos el archivo .py grafico
        self.ui = reproductor.Ui_MainWindow()
        self.ui.setupUi(self)

        iconos.iconos(self)




        # video = "/home/mauricio/proyectos/reproductor/videos/P!nk - Just Give Me A Reason ft Nate Ruess.mp4"
        #
        # self.video = QVideoWidget(self)
        # self.ui.video.addWidget(self.video)
        #
        # self.media = QMediaPlayer()
        # self.media.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
        # self.media.setVideoOutput(self.video)
        # self.media.play()







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

