import datetime
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer, Qt, QSize
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QSplashScreen, QApplication
import time

from home.view.VistaLogin import VistaLogin
from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from listaordini.view.VistaListaOrdini import VistaListaOrdini
from listadelpersonale.view.VistaListaDelPersonale import VistaListaDelPersonale
from listaprodotti.view.VistaListaProdotti import VistaListaProdotti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from listastatistiche.view.VistaListaStatistiche import VistaListaStatistiche
from vendita.view.VistaVendita import VistaVendita

"""
    VISTA HOME
"""


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        self.controller_lista_del_personale = ControllerListaDelPersonale()

        ############################
        # FONT
        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        # Icona di avvio
        avvio_icon = QSplashScreen()
        avvio_icon.setPixmap(QPixmap('listaprodotti/data/images/logo_start.jpg'))
        avvio_icon.show()
        time.sleep(2)
        self.setObjectName("Home")
        self.resize(965, 530)
        self.setStyleSheet("background-color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
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
        self.pushButton_vendita.setMinimumHeight(self.height/5)
        self.pushButton_vendita.setMaximumHeight(self.height/5)
        self.pushButton_vendita.setFont(font)
        self.pushButton_vendita.setObjectName("pushButton_vendita")
        self.pushButton_vendita.setStyleSheet("QPushButton {\n"
                                              "    border-radius:22px;\n"
                                              "    background-color:rgb(228, 107, 41);\n"
                                              "    color:white;\n"
                                              "    border-style: outset;\n" 
                                              "    border-width: 4px;\n"    
                                              "    border-color: black;\n"  
                                              "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_vendita.png'))
        self.pushButton_vendita.setIcon(icon)

        self.pushButton_vendita.setIconSize(QSize(self.width / 7, self.height / 7))
        self.gridLayout_2.addWidget(self.pushButton_vendita, 5, 1, 1, 1)

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
        self.pushButton_prodotti.setMaximumHeight(self.height/5)
        self.pushButton_prodotti.setMaximumWidth(self.width / 6)
        self.pushButton_prodotti.setFont(font)
        self.pushButton_prodotti.setObjectName("pushButton_prodotti")
        self.pushButton_prodotti.setStyleSheet("QPushButton {\n"
                                               "    border-radius:22px;\n"
                                               "    background-color:rgb(26, 108, 218);\n"
                                               "    color:white;\n"
                                               "    border-style: outset;\n" 
                                               "    border-width: 4px;\n"    
                                               "    border-color: black;\n"  
                                               "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_prodotti.png'))
        self.pushButton_prodotti.setIcon(icon)
        self.pushButton_prodotti.setIconSize(QSize(self.width / 6, self.height / 6))
        self.gridLayout_2.addWidget(self.pushButton_prodotti, 5, 5, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_prodotti.clicked.connect(self.go_lista_prodotti)
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
        spacerItem5 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 5, 0, 3, 1)
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

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 5, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 2)

        # DATA
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
        font_clock = QFont('Open Sans', 40, QFont.Bold)
        self.label_clock = QLabel()
        self.label_clock.setAlignment(Qt.AlignCenter)
        self.label_clock.setFont(font_clock)
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
        self.pushButton_ordini.setMaximumHeight(self.height/5)
        self.pushButton_ordini.setMaximumWidth(self.width / 6)
        self.pushButton_ordini.setFont(font)
        self.pushButton_ordini.setObjectName("pushButton_ordini")
        self.pushButton_ordini.setStyleSheet("QPushButton {\n"
                                             "    border-radius:22px;\n"
                                             "    background-color:rgb(26, 108, 218);\n"
                                             "    color:white;\n"
                                             "    border-style: outset;\n" 
                                             "    border-width: 4px;\n"    
                                             "    border-color: black;\n"  
                                             "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_ordini.png'))
        self.pushButton_ordini.setIcon(icon)
        self.pushButton_ordini.setIconSize(QSize(self.width / 9, self.height / 9))
        self.gridLayout_2.addWidget(self.pushButton_ordini, 5, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 5, 4, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.pushButton_ordini.clicked.connect(self.go_lista_ordini)
        self.pushButton_vendita.clicked.connect(self.go_vista_vendita)

        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)
        self.show_time()
        self.setWindowTitle("Home")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    '''
            Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        # FONT
        font = QtGui.QFont()
        font.setPointSize(20)

        # passo la data odierna alla label_data
        data_odierna = datetime.datetime.now()
        self.label_data.setText("%s/%s/%s" % ((data_odierna.day, data_odierna.month, data_odierna.year)))

        # self.pushButton_vendita.setText(_translate("Home", "Vendita"))
        self.pushButton_prodotti.setText(_translate("Home", ""))
        self.pushButton_ordini.setText(_translate("Home", ""))
        self.label_2.setFont(font)
        self.label_2.setText(_translate("Home", "Vendita"))
        self.label_4.setFont(font)
        self.label_4.setText(_translate("Home", "Prodotti"))
        self.label_3.setFont(font)
        self.label_3.setText(_translate("Home", "Ordini"))

        # Parti visibili solo dopo aver effettuato il login (get_status==True)
        if self.controller_lista_del_personale.get_status():
            self.push_button_login = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.push_button_login.sizePolicy().hasHeightForWidth())
            self.push_button_login.setSizePolicy(sizePolicy)
            self.push_button_login.setMinimumSize(QtCore.QSize(150, self.height / 22))
            self.push_button_login.setObjectName("push_button_login")
            self.push_button_login.setMaximumSize(self.width / 13, self.height / 22)
            self.push_button_login.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
            self.gridLayout_3.addWidget(self.push_button_login, 1, 1, 1, 1)
            self.push_button_login.setText(_translate("Home", "LOGOUT"))
            self.push_button_login.clicked.connect(self.go_login)

            self.pushButton_personale = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton_personale.sizePolicy().hasHeightForWidth())
            self.pushButton_personale.setSizePolicy(sizePolicy)
            self.pushButton_personale.setMinimumSize(QtCore.QSize(130, self.height/5))
            self.pushButton_personale.setMaximumHeight(self.height/5)
            self.pushButton_personale.setMaximumWidth(self.width / 6)
            self.pushButton_personale.setFont(font)
            self.pushButton_personale.setObjectName("pushButton_personale")
            self.pushButton_personale.setStyleSheet("QPushButton {\n"
                                                    "    border-radius:22px;\n"
                                                    "    background-color:rgb(26, 108, 218);\n"
                                                    "    color:white;\n"
                                                    "    border-style: outset;\n"
                                                    "    border-width: 4px;\n"
                                                    "    border-color: black;\n"
                                                    "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_personale.png'))
            self.pushButton_personale.setIcon(icon)
            self.pushButton_personale.setIconSize(QSize(self.width / 6, self.height / 6))
            self.gridLayout_2.addWidget(self.pushButton_personale, 7, 5, 1, 1)

            self.pushButton_fornitori = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton_fornitori.sizePolicy().hasHeightForWidth())
            self.pushButton_fornitori.setSizePolicy(sizePolicy)
            self.pushButton_fornitori.setMinimumSize(QtCore.QSize(130, self.height / 5))
            self.pushButton_fornitori.setMaximumHeight(self.height/ 5)
            self.pushButton_fornitori.setFont(font)
            self.pushButton_fornitori.setObjectName("pushButton_fornitori")
            self.pushButton_fornitori.setStyleSheet("QPushButton {\n"
                                                    "    border-radius:22px;\n"
                                                    "    background-color:rgb(26, 108, 218);\n"
                                                    "    color:white;\n"
                                                    "    border-style: outset;\n" 
                                                    "    border-width: 4px;\n"    
                                                    "    border-color: black;\n"  
                                                    "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_fornitori.png'))
            self.pushButton_fornitori.setIcon(icon)
            self.pushButton_fornitori.setIconSize(QSize(self.width / 7, self.height / 7))
            self.gridLayout_2.addWidget(self.pushButton_fornitori, 7, 1, 1, 1)

            self.pushButton_statistiche = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton_statistiche.sizePolicy().hasHeightForWidth())
            self.pushButton_statistiche.setSizePolicy(sizePolicy)
            self.pushButton_statistiche.setMinimumSize(QtCore.QSize(130, 60))
            self.pushButton_statistiche.setFont(font)
            self.pushButton_statistiche.setMaximumHeight(self.height/5)
            self.pushButton_statistiche.setObjectName("pushButton_statistiche")
            self.pushButton_statistiche.setStyleSheet("QPushButton {\n"
                                                      "    border-radius:22px;\n"
                                                      "    background-color:rgb(26, 108, 218);\n"
                                                      "    color:white;\n"
                                                      "    border-style: outset;\n" 
                                                      "    border-width: 4px;\n"    
                                                      "    border-color: black;\n"  
                                                      "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_statistiche.png'))
            self.pushButton_statistiche.setIcon(icon)
            self.pushButton_statistiche.setIconSize(QSize(self.width / 7, self.height / 7))
            self.gridLayout_2.addWidget(self.pushButton_statistiche, 7, 3, 1, 1)

            self.pushButton_personale.setText(_translate("Home", ""))
            self.pushButton_personale.clicked.connect(self.go_lista_del_personale)
            self.pushButton_fornitori.setText(_translate("Home", ""))
            self.pushButton_fornitori.clicked.connect(self.go_lista_fornitori)
            self.pushButton_statistiche.setText(_translate("Home", ""))
            self.pushButton_statistiche.clicked.connect(self.go_lista_statistiche)
            self.label_5 = QtWidgets.QLabel(self)
            self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.label_5.setObjectName("label_5")
            self.gridLayout_2.addWidget(self.label_5, 8, 1, 1, 1)
            self.label_5.setFont(font)
            self.label_5.setText(_translate("Home", "Fornitori"))
            self.label_6 = QtWidgets.QLabel(self)
            self.label_6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.label_6.setObjectName("label_6")
            self.gridLayout_2.addWidget(self.label_6, 8, 3, 1, 1)
            self.label_6.setFont(font)
            self.label_6.setText(_translate("Home", "Statistiche"))
            self.label_7 = QtWidgets.QLabel(self)
            self.label_7.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.label_7.setObjectName("label_7")
            self.gridLayout_2.addWidget(self.label_7, 8, 5, 1, 1)
            self.label_7.setFont(font)
            self.label_7.setText(_translate("Home", "Personale"))
        else:
            self.push_button_login = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.push_button_login.sizePolicy().hasHeightForWidth())
            self.push_button_login.setSizePolicy(sizePolicy)
            self.push_button_login.setMinimumSize(QtCore.QSize(150, self.height / 22))
            self.push_button_login.setObjectName("push_button_login")
            self.push_button_login.setMaximumSize(self.width / 13, self.height / 22)
            self.push_button_login.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
            self.gridLayout_3.addWidget(self.push_button_login, 1, 1, 1, 1)
            self.push_button_login.setText(_translate("Home", "LOGIN"))
            self.push_button_login.clicked.connect(self.go_login)

    # Metodo: consente la visualizzazione dell'orario
    def show_time(self):
        currentTime = QTime.currentTime()
        display_text = currentTime.toString("hh:mm:ss")
        self.label_clock.setText(display_text)

    # Metodo: consente l'acceso all'area delle statistiche
    def go_lista_statistiche(self):
        self.vista_lista_statistiche = VistaListaStatistiche()
        self.vista_lista_statistiche.showMaximized()
        time.sleep(0.3)

    # Metodo: consente l'acceso all'area dei prodotti
    def go_lista_prodotti(self):
        self.vista_lista_prodotti = VistaListaProdotti()
        self.vista_lista_prodotti.showMaximized()

    # Metodo: consente l'accesso all'area dei fornitori
    def go_lista_fornitori(self):
        self.vista_lista_fornitori = VistaListaFornitori()
        self.vista_lista_fornitori.showMaximized()
        time.sleep(0.3)

    # Metodo: consente l'accesso all'area dei ordini
    def go_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.showMaximized()
        time.sleep(0.3)

    # Metodo: consente l'accesso all'area vendita
    def go_vista_vendita(self):
        self.vista_vendita = VistaVendita()
        self.vista_vendita.show()

    # Metodo: consente l'accesso all'area del personale
    def go_lista_del_personale(self):
        self.vista_lista_del_personale = VistaListaDelPersonale()
        self.vista_lista_del_personale.showMaximized()
        time.sleep(0.3)

    # Metodo: consente l'accesso all'area riservata all'amministratore
    def go_login(self):
        if not self.controller_lista_del_personale.get_status():
            self.vista_login = VistaLogin(self.controller_lista_del_personale, self.retranslateUi)
            self.vista_login.show()
        else:
            reply = QMessageBox.question(self, "Logout?",
                                         "Sicuro di voler uscire dal tuo account?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.controller_lista_del_personale.set_status(False)
                self.gridLayout_2.removeWidget(self.pushButton_personale)
                self.pushButton_personale.deleteLater()
                self.gridLayout_2.removeWidget(self.label_7)
                self.label_7.deleteLater()
                self.gridLayout_2.removeWidget(self.pushButton_fornitori)
                self.pushButton_fornitori.deleteLater()
                self.gridLayout_2.removeWidget(self.label_5)
                self.label_5.deleteLater()
                self.gridLayout_2.removeWidget(self.pushButton_statistiche)
                self.pushButton_statistiche.deleteLater()
                self.gridLayout_2.removeWidget(self.label_6)
                self.label_6.deleteLater()
                self.retranslateUi()
            else:
                return

    #Metodo: verifica che l'utente sia consapevole della scelta presa
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Chiudere?',
                                     'Sicuro di voler chiudere il programma?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()
