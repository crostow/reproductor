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
from PyQt5.QtCore import QEvent, QUrl, Qt, QDir
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QFileDialog,
                             QWidget, QPushButton, QSlider,
                             QVBoxLayout)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


def abrir(self):
    video, _ = QFileDialog.getOpenFileName(self, "Video", QDir.homePath())
    if video != '':
        self.ui.play.setEnabled(True)
        self.ui.stop.setEnabled(True)
        self.ui.mute.setEnabled(True)
        self.ui.volumen.setEnabled(True)
        self.ui.proceso.setEnabled(True)
        self.ui.play.setIcon(self.pausa)
        reproducir(self, video)

def conf_basico(self):
    self.video = QVideoWidget(self)
    self.ui.video.addWidget(self.video)
    self.media = QMediaPlayer()
    self.media.setVideoOutput(self.video)

def reproducir(self, video):
    self.media.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
    self.media.play()

def pausa(self):
    self.ui.play.setIcon(self.play)
    self.media.pause()

def play(self):
    self.ui.play.setIcon(self.pausa)
    self.media.play()

def stop(self):
    self.ui.play.setIcon(self.play)
    self.ui.stop.setEnabled(True)
    self.ui.play.setEnabled(True)
    self.ui.mute.setEnabled(True)
    self.media.stop()