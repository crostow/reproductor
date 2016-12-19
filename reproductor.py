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
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

# llamamos a la interfaz
from pantalla import reproductor

# llamamos a los otros metodos
from metodos import iconos, repro

# clase heredada de QmainWindow(constructor de ventanas)
class Reproductor_video(QMainWindow):
    # metodo constructor de clase
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)

        # cargamos el archivo .py grafico
        self.ui = reproductor.Ui_MainWindow()
        self.ui.setupUi(self)

        # creamos el reproductor
        self.media = QMediaPlayer()
        # creamos el widget de video
        self.video = QVideoWidget()
        # agregamos el widget de video al grid
        self.ui.video.addWidget(self.video)
        # definimos a donde se va a mandar el video
        self.media.setVideoOutput(self.video)
        # configuramos el nivel de volumen inicial
        self.media.setVolume(60)

        # conectamos los elementos graficos con los metodos
        self.ui.menu_abrir.triggered.connect(self.abrir)
        self.ui.menu_salir.triggered.connect(self.salir)
        self.ui.play.clicked.connect(self.play_pausa)
        self.ui.stop.clicked.connect(self.alto)
        self.ui.mute.clicked.connect(self.silencio)

        # conectamos los slider con el del proceso y volumen
        self.ui.proceso.sliderMoved.connect(self.setPosition)
        self.ui.volumen.sliderMoved.connect(self.volumen)
        self.media.positionChanged.connect(self.positionChanged)
        self.media.durationChanged.connect(self.durationChanged)


        # mandamos a llamar este metodo para agregar los iconos
        iconos.iconos(self)

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

    #metodo para poner silencio
    def silencio(self):
        if self.sm == 0:
            self.media.setVolume(60)
            self.sm = 1
            self.ui.mute.setIcon(self.volumen_2)
        else:
            repro.mute(self)
            self.sm = 0
            self.ui.mute.setIcon(self.mute)

    # metodo para subir o bajar el volumen
    def volumen(self, position):
        self.media.setVolume(position)
        if position <= 50:
            self.ui.mute.setIcon(self.volumen_2)
        else:
            self.ui.mute.setIcon(self.volumen)

    # metodo que detecta cada que avanza el video cambia la slider
    def positionChanged(self, position):
        self.ui.proceso.setValue(position)

    # metodo que detecta la duracion del video
    def durationChanged(self, duration):
        self.ui.proceso.setRange(0, duration)

    # metodo que toma la posicion del slider y se lo manda al video
    # para adelantar o retroceder
    def setPosition(self, position):
        self.media.setPosition(position)

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

