# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reproductor.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(3, 0, 561, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.video = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.video.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.video.setContentsMargins(0, 0, 0, 0)
        self.video.setObjectName("video")
        self.volumen = QtWidgets.QSlider(self.centralwidget)
        self.volumen.setEnabled(False)
        self.volumen.setGeometry(QtCore.QRect(390, 330, 170, 40))
        self.volumen.setSliderPosition(60)
        self.volumen.setOrientation(QtCore.Qt.Horizontal)
        self.volumen.setTickInterval(1)
        self.volumen.setObjectName("volumen")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setEnabled(False)
        self.play.setGeometry(QtCore.QRect(10, 330, 40, 40))
        self.play.setText("")
        self.play.setObjectName("play")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setEnabled(False)
        self.stop.setGeometry(QtCore.QRect(70, 330, 40, 40))
        self.stop.setText("")
        self.stop.setObjectName("stop")
        self.proceso = QtWidgets.QSlider(self.centralwidget)
        self.proceso.setEnabled(False)
        self.proceso.setGeometry(QtCore.QRect(2, 300, 560, 16))
        self.proceso.setOrientation(QtCore.Qt.Horizontal)
        self.proceso.setObjectName("proceso")
        self.mute = QtWidgets.QPushButton(self.centralwidget)
        self.mute.setEnabled(False)
        self.mute.setGeometry(QtCore.QRect(340, 330, 40, 40))
        self.mute.setText("")
        self.mute.setObjectName("mute")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 19))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_abrir = QtWidgets.QAction(MainWindow)
        self.menu_abrir.setObjectName("menu_abrir")
        self.menu_salir = QtWidgets.QAction(MainWindow)
        self.menu_salir.setObjectName("menu_salir")
        self.menuArchivo.addAction(self.menu_abrir)
        self.menuArchivo.addAction(self.menu_salir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reproductor"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menu_abrir.setText(_translate("MainWindow", "Abrir"))
        self.menu_salir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

