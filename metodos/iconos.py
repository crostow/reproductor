# -*- coding: utf-8 -*-
#-------------------------------------------
# Programa: Reproductor de video
#-------------------------------------------
# Proposito: Agregar iconos a la ventana
#-------------------------------------------
#Autor: Abuelazo
#-------------------------------------------
#fecha: 12/12/2016
#-------------------------------------------


#importamos las librerias necesarias
from PyQt5.QtGui import QIcon

'''
Cargamos los iconos a la interfaz
'''
def iconos(self):
    self.play = QIcon("iconos/play.png")
    self.pausa = QIcon("iconos/pause.png")
    self.stop = QIcon("iconos/stop.png")
    self.volumen = QIcon("iconos/volume-1.png")
    self.volumen_2 = QIcon("iconos/volume-2.png")
    self.mute = QIcon("iconos/muted.png")
    self.abrir = QIcon("iconos/volume-2.png")
    self.salir = QIcon("iconos/muted.png")
    self.ui.menu_abrir.setIcon(self.abrir)
    self.ui.menu_salir.setIcon(self.salir)
    self.ui.stop.setIcon(self.stop)
    self.ui.play.setIcon(self.play)
    self.ui.mute.setIcon(self.volumen)
