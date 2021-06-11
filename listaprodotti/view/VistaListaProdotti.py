from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QApplication
import time

import home.view.VistaHome
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from listaprodotti.view.VistaDisplayProdotto import VistaDisplayProdotto

"""
    VISUALIZZAZIONE DELLA LISTA DEI PRODOTTI CON POSSIBILITà DI FILTRAGGIO
"""


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)
        self.controller = ControllerListaProdotti()
        self.lista_prodotti_filtrata = []
        self.display_prodotti_array = []
        self.setWindowTitle("Lista Prodotti")
        self.setObjectName("Lista Prodotti")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)

        # ---------------topWidget------------------
        self.topWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topWidget.sizePolicy().hasHeightForWidth())
        self.topWidget.setSizePolicy(sizePolicy)
        self.topWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.topWidget.setObjectName("topWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.topWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # LOGO
        self.logo = QLabel(self.topWidget)
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.png')
        self.logo.setPixmap(pixmap)
        self.logo.resize(100, 100)
        self.gridLayout_3.addWidget(self.logo, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        # barra di ricerca
        self.cerca = QtWidgets.QLineEdit(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cerca.sizePolicy().hasHeightForWidth())
        self.cerca.setSizePolicy(sizePolicy)
        self.cerca.setMinimumSize(QtCore.QSize(250, 0))
        self.cerca.setObjectName("cerca")
        self.cerca.setPlaceholderText("Cerca per Cod. prodotto")
        self.gridLayout_3.addWidget(self.cerca, 0, 10, 1, 1)
        self.cerca.returnPressed.connect(self.cerca_prodotto)
        # inserisci prodotto
        self.inserisci_button = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inserisci_button.sizePolicy().hasHeightForWidth())
        self.inserisci_button.setSizePolicy(sizePolicy)
        self.inserisci_button.setObjectName("inserisci_button")
        self.gridLayout_3.addWidget(self.inserisci_button, 0, 9, 1, 1)
        self.inserisci_button.clicked.connect(self.inserisci_prodotto)
        # ----------FILTRI COMBOBOX--------------
        # taglia
        self.taglia = QtWidgets.QComboBox(self.topWidget)
        self.taglia.setObjectName("taglia")
        for count in range(16, 49):
            self.taglia.addItem(str(count))
        self.gridLayout_3.addWidget(self.taglia, 3, 7, 1, 1)
        self.taglia.currentIndexChanged.connect(self.filtro_lista)
        # genere
        self.genere = QtWidgets.QComboBox(self.topWidget)
        self.genere.setObjectName("genere")
        self.genere.addItem("Uomo")
        self.genere.addItem("Uomo")
        self.genere.addItem("Donna")
        self.genere.addItem("Bambino")
        self.genere.addItem("Bambina")
        self.gridLayout_3.addWidget(self.genere, 3, 6, 1, 1)
        self.genere.currentIndexChanged.connect(self.filtro_lista)
        # tipo
        self.tipo = QtWidgets.QComboBox(self.topWidget)
        self.tipo.setObjectName("tipo")
        self.tipo.addItem("Eleganti")  # I don't know why but it's ok :)
        self.tipo.addItem("Sneakers")
        self.tipo.addItem("Sportive")
        self.tipo.addItem("Trekking")
        self.tipo.addItem("Eleganti")
        self.gridLayout_3.addWidget(self.tipo, 3, 5, 1, 1)
        self.tipo.currentIndexChanged.connect(self.filtro_lista)
        # collezione
        self.collezione = QtWidgets.QComboBox(self.topWidget)
        self.collezione.setObjectName("collezione")
        self.collezione.addItem("Primavera / Estate")
        self.collezione.addItem("Primavera / Estate")
        self.collezione.addItem("Autunno / Inverno")
        self.gridLayout_3.addWidget(self.collezione, 3, 8, 1, 1)
        self.collezione.currentIndexChanged.connect(self.filtro_lista)
        # marca
        self.marca = QtWidgets.QComboBox(self.topWidget)
        self.marca.setObjectName("marca")
        self.marca.addItem("Marca")
        for item in self.controller.get_lista_marche():
            self.marca.addItem(str(item))
        self.gridLayout_3.addWidget(self.marca, 3, 4, 1, 1)
        self.marca.currentIndexChanged.connect(self.filtro_lista)
        # spacer
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 10, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 11)
        # in_arrivo button
        self.in_arrivo = QtWidgets.QPushButton(self.topWidget)
        self.in_arrivo.setObjectName("in_arrivo")
        self.gridLayout_3.addWidget(self.in_arrivo, 1, 0, 1, 1)
        self.in_arrivo.clicked.connect(self.show_in_arrivo)
        # in_negozio button
        self.in_negozio = QtWidgets.QPushButton(self.topWidget)
        self.in_negozio.setObjectName("in_negozio")
        self.gridLayout_3.addWidget(self.in_negozio, 1, 1, 1, 1)
        self.in_negozio.clicked.connect(self.show_in_negozio)
        # venduto button
        self.venduto = QtWidgets.QPushButton(self.topWidget)
        self.venduto.setObjectName("venduto")
        self.gridLayout_3.addWidget(self.venduto, 1, 2, 1, 1)
        self.venduto.clicked.connect(self.show_venduto)
        # reso button
        self.reso = QtWidgets.QPushButton(self.topWidget)
        self.reso.setObjectName("reso")
        self.gridLayout_3.addWidget(self.reso, 1, 3, 1, 1)
        self.reso.clicked.connect(self.show_reso)

        # indietro
        self.indietro = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indietro.sizePolicy().hasHeightForWidth())
        self.indietro.setSizePolicy(sizePolicy)
        self.indietro.setObjectName("indietro")
        self.gridLayout_3.addWidget(self.indietro, 0, 0, 1, 1)
        self.indietro.clicked.connect(self.show_home)

        self.verticalLayout.addWidget(self.topWidget)

        # -------------centralWidget---------------
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1172, 851))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # CREAZIONE DEI WIDGET
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.taglia.setItemText(0, _translate("MainWindow", "Taglia"))
        self.genere.setItemText(0, _translate("MainWindow", "Genere"))
        self.in_arrivo.setText(_translate("MainWindow", "IN ARRIVO"))
        self.tipo.setItemText(0, _translate("MainWindow", "Tipo"))
        self.in_negozio.setText(_translate("MainWindow", "IN NEGOZIO"))
        self.marca.setCurrentText(_translate("MainWindow", "Marca"))
        self.collezione.setItemText(0, _translate("MainWindow", "Collezione"))
        self.venduto.setText(_translate("MainWindow", "VENDUTO"))
        self.indietro.setText(_translate("MainWindow", "< Indietro"))
        self.reso.setText(_translate("MainWindow", "RESO"))
        self.inserisci_button.setText(_translate("MainWindow", "Inserisci prodotto"))

        r = 0
        c = 0
        i = 1
        # display prodotto
        if not self.lista_prodotti_filtrata:
            for prodotto in self.controller.get_lista_prodotti():
                self.vista_display_prodotto = VistaDisplayProdotto(prodotto, self.retranslateUi, self.widget, r, c,
                                                                   self.gridLayout_2)
                self.display_prodotti_array.append(self.vista_display_prodotto)
                if c == 4:
                    c = 0
                else:
                    c = c + 2
                if i == 3:
                    i = 1
                    r = r + 2
                else:
                    i = i + 1
        else:
            self.scrollArea.close()
            self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1172, 851))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
            self.gridLayout.setObjectName("gridLayout")
            self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.widget.setObjectName("widget")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
            self.gridLayout_2.setObjectName("gridLayout_2")

            # CREAZIONE DEI WIDGET
            self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.scrollArea)
            for prodotto in self.lista_prodotti_filtrata:
                self.vista_display_prodotto = VistaDisplayProdotto(prodotto, self.retranslateUi, self.widget, r, c,
                                                                   self.gridLayout_2)
                self.display_prodotti_array.append(self.vista_display_prodotto)
                if c == 4:
                    c = 0
                else:
                    c = c + 2
                if i == 3:
                    i = 1
                    r = r + 2
                else:
                    i = i + 1

    """
         Eventi trigger click dei bottoni
    """

    def show_inserici_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.retranslateUi)
        self.vista_inserisci_prodotto.show()

    def show_home(self):
        self.vista_home = home.view.VistaHome.VistaHome()
        self.vista_home.showMaximized()
        time.sleep(0.3)
        self.close()

    def cerca_prodotto(self):
        cod_prodotto = self.cerca.text()
        cod_prodotto.capitalize()
        if cod_prodotto.isalnum() and cod_prodotto.startswith('S'):
            for prodotto in self.controller.get_lista_prodotti():
                if prodotto.cod_prodotto == cod_prodotto:
                    self.lista_prodotti_filtrata.append(prodotto)
        else:
            self.popup_errore()
        self.retranslateUi()

    # crea l'elenco dei codici dei prodotti da visualizzare basati sui filtri
    def filtro_lista(self):
        filtro_marca = str(self.marca.currentText())
        filtro_tipo = str(self.tipo.currentText())
        filtro_genere = str(self.genere.currentText())
        filtro_taglia = str(self.taglia.currentText())
        filtro_collezione = str(self.collezione.currentText())
        print(filtro_taglia)
        print(filtro_marca)
        print(filtro_genere)
        print(filtro_collezione)
        print(filtro_tipo)
        lista = self.controller.get_lista_prodotti()
        self.lista_prodotti_filtrata = lista[:]

        if filtro_taglia != "Taglia":
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.taglia != int(filtro_taglia):
                    self.lista_prodotti_filtrata.remove(prodotto)
        if filtro_marca != "Marca":
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.marca != str(filtro_marca):
                    self.lista_prodotti_filtrata.remove(prodotto)
        if filtro_tipo != "Tipo":
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.tipo != str(filtro_tipo):
                    self.lista_prodotti_filtrata.remove(prodotto)
        if filtro_genere != "Genere":
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.genere != str(filtro_genere):
                    self.lista_prodotti_filtrata.remove(prodotto)
        if filtro_collezione != "Collezione":
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stagione != str(filtro_collezione):
                    self.lista_prodotti_filtrata.remove(prodotto)
        self.retranslateUi()

    def get_lista_filtrata(self):
        return self.lista_prodotti_filtrata

    def show_in_arrivo(self):
        self.lista_prodotti_filtrata.clear()
        for prodotto in self.controller.get_lista_prodotti():
            if prodotto.stato == "In arrivo":
                self.lista_prodotti_filtrata.append(prodotto)
        self.retranslateUi()

    def show_in_negozio(self):
        self.lista_prodotti_filtrata.clear()
        for prodotto in self.controller.get_lista_prodotti():
            if prodotto.stato == "In negozio":
                self.lista_prodotti_filtrata.append(prodotto)
        self.retranslateUi()

    def show_venduto(self):
        self.lista_prodotti_filtrata.clear()
        for prodotto in self.controller.get_lista_prodotti():
            if prodotto.stato == "Venduto":
                self.lista_prodotti_filtrata.append(prodotto)

        self.retranslateUi()

    def show_reso(self):
        self.lista_prodotti_filtrata.clear()
        for prodotto in self.controller.get_lista_prodotti():
            if prodotto.stato == "Reso":
                self.lista_prodotti_filtrata.append(prodotto)

        self.display_prodotti_array.clear()
        self.retranslateUi()

    def inserisci_prodotto(self):
        self.inserisci_prodotto = VistaInserisciProdotto(self.controller, self.retranslateUi)
        self.inserisci_prodotto.showMaximized()

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText("Hai inserito un codice prodotto non valido! \n\nProva con un formato del tipo: S03")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()




