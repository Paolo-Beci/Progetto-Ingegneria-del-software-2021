import datetime
import sys
import threading
from datetime import date

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QApplication, QLabel
import time

from listaordini.view.VistaListaOrdini import VistaListaOrdini
from listadelpersonale.view.VistaListaDelPersonale import VistaListaDelPersonale
from listaprodotti.view.VistaListaProdotti import VistaListaProdotti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from listastatistiche.view.VistaListaStatistiche import VistaListaStatistiche

"""
    VISTA HOME
"""


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        ###########
        self.setObjectName("Home")
        self.resize(965, 530)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_vendita = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_vendita.sizePolicy().hasHeightForWidth())
        self.pushButton_vendita.setSizePolicy(sizePolicy)
        self.pushButton_vendita.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_vendita.setFont(font)
        self.pushButton_vendita.setObjectName("pushButton_vendita")
        self.gridLayout_2.addWidget(self.pushButton_vendita, 5, 1, 1, 1)
        self.pushButton_personale = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_personale.sizePolicy().hasHeightForWidth())
        self.pushButton_personale.setSizePolicy(sizePolicy)
        self.pushButton_personale.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_personale.setFont(font)
        self.pushButton_personale.setObjectName("pushButton_personale")
        self.gridLayout_2.addWidget(self.pushButton_personale, 7, 5, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini.png')
        self.label.setPixmap(pixmap)
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_prodotti = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_prodotti.sizePolicy().hasHeightForWidth())
        self.pushButton_prodotti.setSizePolicy(sizePolicy)
        self.pushButton_prodotti.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_prodotti.setFont(font)
        self.pushButton_prodotti.setObjectName("pushButton_prodotti")
        self.gridLayout_2.addWidget(self.pushButton_prodotti, 5, 5, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.push_button_login = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_login.sizePolicy().hasHeightForWidth())
        self.push_button_login.setSizePolicy(sizePolicy)
        self.push_button_login.setMinimumSize(QtCore.QSize(100, 20))

        # da fare
        self.push_button_login.setObjectName("push_button_login")
        self.gridLayout_3.addWidget(self.push_button_login, 1, 1, 1, 1)
        self.push_button_login.clicked.connect(self.go_login)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 5, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem4, 6, 3, 1, 1)
        self.pushButton_fornitori = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_fornitori.sizePolicy().hasHeightForWidth())
        self.pushButton_fornitori.setSizePolicy(sizePolicy)
        self.pushButton_fornitori.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_fornitori.setFont(font)
        self.pushButton_fornitori.setObjectName("pushButton_fornitori")
        self.gridLayout_2.addWidget(self.pushButton_fornitori, 7, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 5, 0, 3, 1)
        self.pushButton_statistiche = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_statistiche.sizePolicy().hasHeightForWidth())
        self.pushButton_statistiche.setSizePolicy(sizePolicy)
        self.pushButton_statistiche.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_statistiche.setFont(font)
        self.pushButton_statistiche.setObjectName("pushButton_statistiche")
        self.gridLayout_2.addWidget(self.pushButton_statistiche, 7, 3, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 1, 0, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_4.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 1, 2, 2, 1)

        # DATA
        #self.textBrowser_data = QtWidgets.QTextBrowser(self)
        font_data = QFont('Open Sans', 20)
        self.label_data = QLabel()
        self.label_data.setAlignment(Qt.AlignCenter)
        self.label_data.setFont(font_data)
        self.label_data.setMinimumSize(QtCore.QSize(150, 30))
        self.label_data.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_data.setObjectName("label_data")
        self.gridLayout_4.addWidget(self.label_data, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_4.addItem(spacerItem9, 3, 1, 1, 1)

        # ORARIO
        #self.textBrowser_clock = QtWidgets.QTextBrowser(self)
        font_clock= QFont('Open Sans', 40, QFont.Bold)
        self.label_clock= QLabel()
        self.label_clock.setAlignment(Qt.AlignCenter)
        self.label_clock.setFont(font_clock)
        #self.label_clock.setAutoFillBackground(True) #150,0
        self.label_clock.setMinimumSize(QtCore.QSize(240, 50))
        self.label_clock.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_clock.setObjectName("label_clock")
        self.gridLayout_4.addWidget(self.label_clock, 1, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 2, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 5, 2, 3, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem11, 8, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 5, 6, 3, 1)
        self.pushButton_ordini = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ordini.sizePolicy().hasHeightForWidth())
        self.pushButton_ordini.setSizePolicy(sizePolicy)
        self.pushButton_ordini.setMinimumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ordini.setFont(font)
        self.pushButton_ordini.setObjectName("pushButton_ordini")
        self.gridLayout_2.addWidget(self.pushButton_ordini, 5, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 5, 4, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 2)

        timer= QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)
        self.show_time()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        #t1 = threading.Thread(target=self.show_time_date())
        #t1.start()

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.pushButton_vendita.setText(_translate("Home", "Area vendita"))
        self.pushButton_vendita.clicked.connect(self.go_vista_vendita)
        self.pushButton_personale.setText(_translate("Home", "Area del personale"))
        self.pushButton_personale.clicked.connect(self.go_lista_del_personale)

        #---------------------------------

        i=datetime.datetime.now()
        self.label_data.setText("%s/%s/%s"%((i.day,i.month,i.year)))
        self.pushButton_prodotti.setText(_translate("Home", "Area prodotti"))
        self.pushButton_prodotti.clicked.connect(self.go_lista_prodotti)
        self.push_button_login.setText(_translate("Home", "Logout"))
        self.pushButton_fornitori.setText(_translate("Home", "Area fornitori"))
        self.pushButton_fornitori.clicked.connect(self.go_lista_fornitori)
        self.pushButton_statistiche.setText(_translate("Home", "Area statistiche"))
        self.pushButton_statistiche.clicked.connect(self.go_lista_statistiche)
        self.pushButton_ordini.setText(_translate("Home", "Area ordini"))
        ###########

    def show_time(self):
        currentTime= QTime.currentTime()
        display_text= currentTime.toString("hh:mm:ss")
        self.label_clock.setText(display_text)

    def go_lista_statistiche(self):
        self.vista_lista_statistiche = VistaListaStatistiche()
        self.vista_lista_statistiche.showMaximized()
        time.sleep(0.3)

    def go_lista_prodotti(self):
        self.vista_lista_prodotti = VistaListaProdotti()
        self.vista_lista_prodotti.showMaximized()
        time.sleep(0.3)

    def go_lista_fornitori(self):
        self.vista_lista_fornitori = VistaListaFornitori()
        self.vista_lista_fornitori.showMaximized()
        time.sleep(0.3)

    def go_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.showMaximized()
        time.sleep(0.3)

    def go_vista_vendita(self):
        pass

    def go_lista_del_personale(self):
        self.vista_lista_del_personale = VistaListaDelPersonale()
        self.vista_lista_del_personale.showMaximized()
        time.sleep(0.3)

    def go_login(self):
        pass
