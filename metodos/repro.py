# -*- coding: utf-8 -*-
#-------------------------------------------
# Programa: Reproductor de video
#-------------------------------------------
# Proposito: manejo de botones y logica
#-------------------------------------------
#Autor: Abuelazo
#-------------------------------------------
#fecha: 14/12/2016
#-------------------------------------------


# importamos librerias necesarias
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaContent

# metodo para abrir un video yreproducirlo
def abrir(self):
    '''
    abrimos un dialogo para selecionar la ubicacion del video
    y lo guardamos en la variable video
    se pone "video, _" porque si no te regresa el valor en una
    lista y nosotros solo queremos el primer valor de esa lista
    '''
    video, _ = QFileDialog.getOpenFileName(self, "Video", QDir.homePath())
    # si la variable esta vacia no se hace nada
    if video != "":
        # se activan los botones necesarios para el funcionamiento del programa
        self.ui.play.setEnabled(True)
        self.ui.stop.setEnabled(True)
        self.ui.mute.setEnabled(True)
        self.ui.volumen.setEnabled(True)
        self.ui.proceso.setEnabled(True)
        self.ui.play.setIcon(self.pausa)
        # se manda a llamar el metodo reproducir y se le pasa como
        # parametro la direccion del video
        reproducir(self, video)

#metodo para reproducir el video
def reproducir(self, video):
    # se le indica al reproductor que va a reproducir un archivo local
    # y se le asigna la direccion del video
    self.media.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
    # se reproduce el video
    self.media.play()
    # bandera para poner pausa
    self.pp = 0
    # bandera para silenciar el video
    self.sm = 1


#metodo para pausar el video
def pausa(self):
    # se cambia el icono al boton
    self.ui.play.setIcon(self.play)
    # se pone pausa al video
    self.media.pause()

#metodo para pausar y reproducir
def play(self):
    # se cambia el icono al boton
    self.ui.play.setIcon(self.pausa)
    # se reproduce el video
    self.media.play()

#metodo para detener el video
def stop(self):
    # se cambia el icono al boton
    self.ui.play.setIcon(self.play)
    # se desactivan los botones al detener el video
    self.ui.stop.setEnabled(False)
    self.ui.play.setEnabled(False)
    self.ui.mute.setEnabled(False)
    # se detiene el video
    self.media.stop()

#metodo para silenciar el video
def mute(self):
    # se manda el volumen a 0
    self.media.setVolume(0)
    # se cambia el icono a el boton
    self.ui.mute.setIcon(self.mute)


