# -*- coding: utf-8 -*-
#-------------------------------------------
# Programa: Reproductor de video
#-------------------------------------------
# Proposito: Agregar iconos a la ventana
#-------------------------------------------
#Autor: Abuelazo
#-------------------------------------------
#fecha: 14/12/2016
#-------------------------------------------


#importamos las librerias necesarias
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

'''
Cargamos los iconos a la interfaz
'''
def iconos(self):
    '''
    cargamos todos los iconos a las variables para
    su utilizacion despues y se asignan a los botones
    '''
    self.play = QIcon("iconos/play.png")
    self.pausa = QIcon("iconos/pause.png")
    self.stop = QIcon("iconos/stop.png")
    self.volumen = QIcon("iconos/volume-1.png")
    self.volumen_2 = QIcon("iconos/volume-2.png")
    self.mute = QIcon("iconos/muted.png")
    self.abrir = QIcon("iconos/volume-2.png")
    self.salir = QIcon("iconos/close.png")
    self.ui.menu_abrir.setIcon(self.abrir)
    self.ui.menu_salir.setIcon(self.salir)
    self.ui.stop.setIcon(self.stop)
    self.ui.stop.setIconSize(QSize(30, 30))
    self.ui.play.setIcon(self.play)
    self.ui.play.setIconSize(QSize(30, 30))
    self.ui.mute.setIcon(self.volumen)
    self.ui.mute.setIconSize(QSize(30, 30))
