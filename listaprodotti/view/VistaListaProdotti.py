from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QMessageBox
import keyboard
import time

import home.view.VistaHome
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaprodotti.model.ListaProdotti import ListaProdotti
from prodotto.view.VistaModificaProdotto import VistaModificaProdotto
from prodotto.view.VistaProdotto import VistaProdotto
from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.controller.ControllerProdotto import ControllerProdotto

"""
    VISUALIZZAZIONE DELLA LISTA DEI PRODOTTI CON POSSIBILITà DI FILTRAGGIO
"""


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)
        self.controller = ControllerListaProdotti()
        self.listaProdotti = ListaProdotti()
        self.lista_prodotti_filtrata = []
        self.setWindowTitle("Lista Prodotti")
        self.setObjectName("Lista Prodotti")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

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
        pixmap = QPixmap('listaprodotti/data/images/logo_mini.png')
        self.logo.setPixmap(pixmap)
        self.logo.resize(100, 100)
        self.gridLayout_3.addWidget(self.logo, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        # barra di ricerca
        self.cerca_button = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cerca_button.sizePolicy().hasHeightForWidth())
        self.cerca_button.setSizePolicy(sizePolicy)
        self.cerca_button.setObjectName("cerca_button")
        self.gridLayout_3.addWidget(self.cerca_button, 0, 9, 1, 1)
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
        # self.cerca_button.clicked.connect(self.cerca_prodotto())
        # ----------FILTRI COMBOBOX--------------
        # taglia
        self.taglia = QtWidgets.QComboBox(self.topWidget)
        self.taglia.setObjectName("taglia")
        for count in range(16, 49):
            self.taglia.addItem(str(count))
        self.gridLayout_3.addWidget(self.taglia, 3, 7, 1, 1)
        # genere
        self.genere = QtWidgets.QComboBox(self.topWidget)
        self.genere.setObjectName("genere")
        self.genere.addItem("Uomo")
        self.genere.addItem("Uomo")
        self.genere.addItem("Donna")
        self.genere.addItem("Bambino")
        self.genere.addItem("Bambina")
        self.gridLayout_3.addWidget(self.genere, 3, 6, 1, 1)
        # tipo
        self.tipo = QtWidgets.QComboBox(self.topWidget)
        self.tipo.setObjectName("tipo")
        self.tipo.addItem("Eleganti")  # I don't know why but it's ok :)
        self.tipo.addItem("Sneakers")
        self.tipo.addItem("Sportive")
        self.tipo.addItem("Trekking")
        self.tipo.addItem("Eleganti")
        self.gridLayout_3.addWidget(self.tipo, 3, 5, 1, 1)
        # collezione
        self.collezione = QtWidgets.QComboBox(self.topWidget)
        self.collezione.setObjectName("collezione")
        self.collezione.addItem("Primavera / Estate")
        self.collezione.addItem("Primavera / Estate")
        self.collezione.addItem("Autunno / Inverno")
        self.gridLayout_3.addWidget(self.collezione, 3, 8, 1, 1)
        # marca
        self.marca = QtWidgets.QComboBox(self.topWidget)
        self.marca.setObjectName("marca")
        self.marca.addItem("Marca")
        for item in self.controller.get_lista_marche():
            self.marca.addItem(str(item))
        self.gridLayout_3.addWidget(self.marca, 3, 4, 1, 1)
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
        self.in_negozio.clicked.connect(self.show_in_arrivo)
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
        # display prodotto
        r = 0
        c = 0
        i = 1
        cod_precedente = 'S00'
        for prodotto in self.controller.get_lista_prodotti():
            cod = prodotto.cod_prodotto
            if cod != cod_precedente:
                self.display_prodotto = QtWidgets.QWidget(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.display_prodotto.sizePolicy().hasHeightForWidth())
                self.display_prodotto.setSizePolicy(sizePolicy)
                self.display_prodotto.setMinimumSize(QtCore.QSize(200, 400))
                self.display_prodotto.setObjectName("display_prodotto")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.display_prodotto)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.immagine = QtWidgets.QLabel(self.display_prodotto)  # come lo allineo centrale??
                self.immagine.setObjectName("immagine")
                pixmap = QPixmap('listaprodotti/data/images/' + str(cod) + '.jpg')
                self.immagine.setPixmap(pixmap)
                self.verticalLayout_2.addWidget(self.immagine, QtCore.Qt.AlignHCenter)
                self.nome_marca = QtWidgets.QLabel(self.display_prodotto)
                self.nome_marca.setObjectName("nome_marca")
                self.nome_marca.setText(
                    str(self.controller.get_nome_prodotto_by_code(cod)) + " - " + str(self.controller.get_marca_prodotto_by_code(
                        cod)))
                self.verticalLayout_2.addWidget(self.nome_marca)
                self.prezzo = QtWidgets.QLabel(self.display_prodotto)
                self.prezzo.setObjectName("prezzo")
                self.prezzo.setText(self.controller.get_prezzo_prodotto_by_code(cod))
                self.verticalLayout_2.addWidget(self.prezzo)
                # creare un altra classe in cui definiamo la scheda del prodotto ceh prende in argomento il prodotto
                self.dettagli = QtWidgets.QPushButton(self.topWidget)
                self.dettagli.setObjectName("dettagli")
                self.dettagli.setText("Dettagli")
                # self.dettagli.clicked.connect(self.show_prodotto(cod))
                self.verticalLayout_2.addWidget(self.dettagli)

                # c = colonne , r = righe del display
                self.gridLayout_2.addWidget(self.display_prodotto, r, c, 1, 1)
                if c == 4:
                    c = 0
                else:
                    c = c + 2
                if i == 3:
                    i = 1
                    r = r + 2
                else:
                    i = i + 1
                cod_precedente = cod

        # linee separatorie
        # self.line_2 = QtWidgets.QFrame(self.widget)
        # self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")
        # self.gridLayout_2.addWidget(self.line_2, 1, 4, 1, 1)
        # self.line = QtWidgets.QFrame(self.widget)
        # self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        # self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        # self.line_6 = QtWidgets.QFrame(self.widget)
        # self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_6.setObjectName("line_6")
        # self.gridLayout_2.addWidget(self.line_6, 0, 3, 1, 1)
        # self.line_5 = QtWidgets.QFrame(self.widget)
        # self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_5.setObjectName("line_5")
        # self.gridLayout_2.addWidget(self.line_5, 2, 1, 1, 1)
        # self.line_7 = QtWidgets.QFrame(self.widget)
        # self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_7.setObjectName("line_7")
        # self.gridLayout_2.addWidget(self.line_7, 2, 3, 1, 1)
        # self.line_4 = QtWidgets.QFrame(self.widget)
        # self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_4.setObjectName("line_4")
        # self.gridLayout_2.addWidget(self.line_4, 0, 1, 1, 1)
        # self.line_3 = QtWidgets.QFrame(self.widget)
        # self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_3.setObjectName("line_3")
        # self.gridLayout_2.addWidget(self.line_3, 1, 2, 1, 1)

        # CREAZIONE DEI WIDGET
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        # QtWidgets.QMainWindow.setCentralWidget(self.centralwidget)     NON RIESCO A METTERLA A TUTTO SCHERMO
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))  # settata ad una risoluzione HD

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.nome_marca.setText(_translate("MainWindow", "Marca - Nome prodotto"))
        self.prezzo.setText(_translate("MainWindow", "Prezzo"))
        self.dettagli.setText(_translate("MainWindow", "Dettagli"))
        self.cerca_button.setText(_translate("MainWindow", "Cerca"))

    def show_inserici_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.updateUi)
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
            self.filtro_lista(cod_prodotto)
        else:
            self.popup_errore()

    # crea l'elenco dei codici dei prodotti da visualizzare basati sui filtri
    def filtro_lista(self, cod):
        return 'S01'

    def get_lista_filtrata(self):
        return self.lista_prodotti_filtrata

    def show_in_arrivo(self):  # PROVA TEMPORANEA
        prodotto_selezionato = self.controller.get_prodotto_by_code("S01")
        self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_codice,
                                            self.update_ui(self))
        self.vista_prodotto.showMaximized()

    def show_in_negozio(self):
        pass

    def show_venduto(self):
        pass

    def show_reso(self):
        pass

    def show_prodotto(self, cod):
        prodotto_selezionato = self.controller.get_prodotto_by_code(cod)
        self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_codice,
                                            ControllerProdotto.modifica_prodotto_by_codice, self.retranslateUi)
        self.vista_prodotto.showMaximized()
        time.sleep(0.3)
        self.close()

    def closeEvent(self, event):
        pass
        # self.controller.save_data()

    def update_ui(self, event):
        pass

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText("Hai inserito un codice prodotto non valido! \n\nProva con un formato del tipo: S03")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()



    # def show_prodotto(self):
    #     if len(self.list_view.selectedIndexes()) > 0:
    #         selected = self.list_view.selectedIndexes()[0].row()
    #         prodotto_selezionato = self.controller.get_prodotto(selected)
    #         self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_codice,
    #                                             ControllerProdotto.modifica_prodotto_by_codice, self.update_ui)
    #         self.vista_prodotto.showMaximized()
    #         time.sleep(0.3)
    #         self.close()
