from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QApplication

from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from listaprodotti.view.VistaDisplayProdotto import VistaDisplayProdotto

"""
    VISUALIZZAZIONE DELLA LISTA DEI PRODOTTI CON POSSIBILITà DI FILTRAGGIO
"""


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)
        self.controller_lista_ordini = ControllerListaOrdini()
        self.controller_lista_prodotti = ControllerListaProdotti()
        self.lista_prodotti = self.controller_lista_prodotti.get_lista_prodotti()
        self.lista_prodotti_filtrata = self.lista_prodotti[:]
        self.lista_prodotti_cercati = []
        self.cerca_flag = False
        self.setWindowTitle("Lista Prodotti")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)


        ''' 
            Costruzione parte statica dell'interfaccia
        '''
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
        # ricerca
        self.cerca = QtWidgets.QLineEdit(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cerca.sizePolicy().hasHeightForWidth())
        self.cerca.setSizePolicy(sizePolicy)
        self.cerca.setMinimumSize(QtCore.QSize(250, 0))
        self.cerca.setObjectName("cerca")
        self.cerca.setPlaceholderText("Cerca per Cod. prodotto")
        self.cerca.setClearButtonEnabled(False)
        self.gridLayout_3.addWidget(self.cerca, 0, 10, 1, 1)
        self.cerca.setStyleSheet("QLineEdit {\n"
                                  "   border-width: 2px;\n"
                                  "   border-radius: 10px;\n"
                                  "   border: 2px solid gray;\n"
                                  "   font: 12px;\n"
                                  "   padding: 6px;\n"
                                  "}")
        self.cerca.returnPressed.connect(self.cerca_prodotto)
        # inserisci prodotto
        self.inserisci_button = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inserisci_button.sizePolicy().hasHeightForWidth())
        self.inserisci_button.setSizePolicy(sizePolicy)
        self.inserisci_button.setObjectName("inserisci_button")
        self.inserisci_button.setStyleSheet("QPushButton {\n"
                                        "   background-color:rgb(26, 108, 218);\n"
                                        "   border-width: 2px;\n"
                                        "   border-radius: 10px;\n"
                                        "   font: bold 12px;\n"
                                        "   padding: 6px;\n"
                                        "   color: white;\n"
                                        "}")
        self.gridLayout_3.addWidget(self.inserisci_button, 0, 9, 1, 1)
        self.inserisci_button.clicked.connect(self.show_inserisci_prodotto)
        # ----------FILTRI COMBOBOX--------------
        # taglia
        self.taglia = QtWidgets.QComboBox(self.topWidget)
        self.taglia.setObjectName("taglia")
        for count in range(16, 49):
            self.taglia.addItem(str(count))
        self.taglia.setStyleSheet("QComboBox {\n"
                                        "   background-color:rgb(26, 108, 218);\n"
                                        "   border-width: 2px;\n"
                                        "   font: 12px;\n"
                                        "   padding: 3px;\n"
                                        "   color: white;\n"
                                        "}")
        self.gridLayout_3.addWidget(self.taglia, 3, 7, 1, 1)
        self.taglia.currentIndexChanged.connect(self.filtro_combobox)
        # genere
        self.genere = QtWidgets.QComboBox(self.topWidget)
        self.genere.setObjectName("genere")
        self.genere.addItem("Uomo")
        self.genere.addItem("Uomo")
        self.genere.addItem("Donna")
        self.genere.addItem("Bambino")
        self.genere.addItem("Bambina")
        self.gridLayout_3.addWidget(self.genere, 3, 6, 1, 1)
        self.genere.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(26, 108, 218);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: white;\n"
                                  "}")
        self.genere.currentIndexChanged.connect(self.filtro_combobox)
        # tipo
        self.tipo = QtWidgets.QComboBox(self.topWidget)
        self.tipo.setObjectName("tipo")
        self.tipo.addItems(["Eleganti", "Eleganti", "Sneakers", "Sportive", "Trekking"])
        self.gridLayout_3.addWidget(self.tipo, 3, 5, 1, 1)
        self.tipo.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(26, 108, 218);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: white;\n"
                                  "}")
        self.tipo.currentIndexChanged.connect(self.filtro_combobox)
        # collezione
        self.collezione = QtWidgets.QComboBox(self.topWidget)
        self.collezione.setObjectName("collezione")
        self.collezione.addItem("Primavera / Estate")
        self.collezione.addItem("Primavera / Estate")
        self.collezione.addItem("Autunno / Inverno")
        self.gridLayout_3.addWidget(self.collezione, 3, 8, 1, 1)
        self.collezione.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(26, 108, 218);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: white;\n"
                                  "}")
        self.collezione.currentIndexChanged.connect(self.filtro_combobox)
        # marca
        self.marca = QtWidgets.QComboBox(self.topWidget)
        self.marca.setObjectName("marca")
        self.marca.addItem("Marca")
        for item in self.controller_lista_prodotti.get_lista_marche():
            self.marca.addItem(str(item))
        self.gridLayout_3.addWidget(self.marca, 3, 4, 1, 1)
        self.marca.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(26, 108, 218);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: white;\n"
                                  "}")
        self.marca.currentIndexChanged.connect(self.filtro_combobox)
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
        self.in_arrivo.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.in_arrivo, 1, 0, 1, 1)
        self.in_arrivo.clicked.connect(self.show_in_arrivo)
        # in_negozio button
        self.in_negozio = QtWidgets.QPushButton(self.topWidget)
        self.in_negozio.setObjectName("in_negozio")
        self.in_negozio.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.in_negozio, 1, 1, 1, 1)
        self.in_negozio.clicked.connect(self.show_in_negozio)
        # venduto button
        self.venduto = QtWidgets.QPushButton(self.topWidget)
        self.venduto.setObjectName("venduto")
        self.venduto.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.venduto, 1, 2, 1, 1)
        self.venduto.clicked.connect(self.show_venduto)
        # reso button
        self.reso = QtWidgets.QPushButton(self.topWidget)
        self.reso.setObjectName("reso")
        self.reso.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_home.png'))
        self.indietro.setIcon(icon)
        self.indietro.setIconSize(QSize(50, 50))
        self.indietro.setStyleSheet("QPushButton {\n"
                                "   background-color:white;\n"
                                "   border-width: 2px;\n"
                                "   border-radius: 10px;\n"
                                "   padding: 6px;\n"
                                "}")
        self.gridLayout_3.addWidget(self.indietro, 0, 0, 1, 1)
        self.indietro.clicked.connect(self.close)

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

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().setParent(None)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Area prodotti"))
        self.taglia.setItemText(0, _translate("MainWindow", "Taglia"))
        self.genere.setItemText(0, _translate("MainWindow", "Genere"))
        self.in_arrivo.setText(_translate("MainWindow", "IN ARRIVO"))
        self.tipo.setItemText(0, _translate("MainWindow", "Tipo"))
        self.in_negozio.setText(_translate("MainWindow", "IN NEGOZIO"))
        self.collezione.setItemText(0, _translate("MainWindow", "Collezione"))
        self.venduto.setText(_translate("MainWindow", "VENDUTO"))
        self.reso.setText(_translate("MainWindow", "RESO"))
        self.inserisci_button.setText(_translate("MainWindow", "Inserisci prodotto"))

        if self.cerca_flag:
            self.display_build(self.lista_prodotti_cercati)
        else:
            self.display_build(self.lista_prodotti_filtrata)

    """
         Eventi trigger click dei bottoni
    """
    def show_inserisci_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller_lista_prodotti, self.retranslateUi,
                                                               False, None, self.lista_prodotti_filtrata, None)
        self.vista_inserisci_prodotto.show()
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().setParent(None)
        self.retranslateUi()

    def cerca_prodotto(self):
        self.lista_prodotti_cercati = self.lista_prodotti_filtrata[:]

        self.cerca_flag = True
        codice_cerca = self.cerca.text()
        codice_cerca = codice_cerca.upper()
        elementi_da_rimuovere = []
        if codice_cerca.isalnum() and codice_cerca.startswith('S'):
            for prodotto in self.lista_prodotti_cercati:
                cod_prodotto= str(prodotto.cod_prodotto)
                cod_prodotto= cod_prodotto.upper()
                if not (codice_cerca in cod_prodotto):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                if prodotto in self.lista_prodotti_cercati:
                    self.lista_prodotti_cercati.remove(prodotto)
            for i in reversed(range(self.gridLayout_2.count())):
                self.gridLayout_2.itemAt(i).widget().setParent(None)
        else:
            self.popup_errore()
        self.retranslateUi()
        self.cerca_flag = False

    # crea l'elenco dei codici dei prodotti da visualizzare basati sui filtri
    def filtro_lista(self, IA, IN, V, R):
        filtro_marca = str(self.marca.currentText())
        filtro_tipo = str(self.tipo.currentText())
        if str(self.genere.currentText()) == "Uomo":
            filtro_genere = "U"
        elif str(self.genere.currentText()) == "Donna":
            filtro_genere = "D"
        elif str(self.genere.currentText()) == "Bambino":
            filtro_genere = "BO"
        elif str(self.genere.currentText()) == "Bambina":
            filtro_genere = "BA"
        else:
            filtro_genere = "Genere"
        filtro_taglia = str(self.taglia.currentText())
        if str(self.collezione.currentText()) == "Primavera / Estate":
            filtro_collezione = "P/E"
        elif str(self.collezione.currentText()) == "Autunno / Inverno":
            filtro_collezione = "A/I"
        else:
            filtro_collezione = "Collezione"

        elementi_da_rimuovere = []
        lista = self.controller_lista_prodotti.get_lista_prodotti()
        self.lista_prodotti_filtrata = lista[:]

        if IA:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "In arrivo":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if IN:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "In negozio":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if V:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "Venduto":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if R:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "Reso":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_taglia != "Taglia":
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.taglia != int(filtro_taglia):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_marca != "Marca":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.marca) != str(filtro_marca):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_tipo != "Tipo":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.tipo) != str(filtro_tipo):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_genere != "Genere":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.genere) != str(filtro_genere):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_collezione != "Collezione":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.stagione) != str(filtro_collezione):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()

        self.retranslateUi()

    def display_build(self, lista_da_caricare):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        width = self.screenRect.width()

        row = 0
        column = 0
        for prodotto in lista_da_caricare:
            self.widget_generico = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.displayprodotto1 = VistaDisplayProdotto(prodotto, self.retranslateUi, self.controller_lista_prodotti, self.lista_prodotti_filtrata)
            self.widget_generico = self.displayprodotto1
            self.widget_generico.setMinimumSize(QtCore.QSize((width / 3.2), 450))

            self.gridLayout_2.addWidget(self.widget_generico, row, column, 1, 1)

            if column == 2:
                row = row + 1
                column = 0
            else:
                column = column + 1

    def show_in_arrivo(self):
        self.filtro_lista(True, False, False, False)

    def show_in_negozio(self):
        self.filtro_lista(False, True, False, False)

    def show_venduto(self):
        self.filtro_lista(False, False, True, False)

    def show_reso(self):
        self.filtro_lista(False, False, False, True)

    def filtro_combobox(self):
        self.filtro_lista(False, False, False, False)

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText("Hai inserito un codice prodotto non valido! \n\nProva con un formato del tipo: S03")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def popup_no_prodotti(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText("Nessun prodotto corrisponde ai criteri di ricerca. \n\nProva con altri filtri")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def closeEvent(self, event):
        self.controller_lista_ordini.save_data()
        self.controller_lista_prodotti.save_data()
