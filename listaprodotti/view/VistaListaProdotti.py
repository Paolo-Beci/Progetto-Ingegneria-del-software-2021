from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit
import time

import home.view.VistaHome
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.view.VistaProdotto import VistaProdotto
from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.controller.ControllerProdotto import ControllerProdotto

"""
    VISUALIZZAZIONE DELLA LISTA DEI PRODOTTI CON POSSIBILITà DI FILTRAGGIO
"""


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)
        self.setWindowTitle("Lista Prodotti")
        self.setObjectName("Lista Prodotti")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        #---------------topWidget------------------
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
        #barra di ricerca
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
        #----------FILTRI COMBOBOX--------------
        #taglia
        self.taglia = QtWidgets.QComboBox(self.topWidget)
        self.taglia.setObjectName("taglia")
        self.taglia.addItem("")
        self.gridLayout_3.addWidget(self.taglia, 3, 7, 1, 1)
        #genere
        self.genere = QtWidgets.QComboBox(self.topWidget)
        self.genere.setObjectName("genere")
        self.genere.addItem("")
        self.genere.addItem("")
        self.genere.addItem("")
        self.genere.addItem("")
        self.gridLayout_3.addWidget(self.genere, 3, 6, 1, 1)
        #tipo
        self.tipo = QtWidgets.QComboBox(self.topWidget)
        self.tipo.setObjectName("tipo")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.gridLayout_3.addWidget(self.tipo, 3, 5, 1, 1)
        #collezione
        self.collezione = QtWidgets.QComboBox(self.topWidget)
        self.collezione.setObjectName("collezione")
        self.collezione.addItem("")
        self.collezione.addItem("")
        self.gridLayout_3.addWidget(self.collezione, 3, 8, 1, 1)
        #marca
        self.marca = QtWidgets.QComboBox(self.topWidget)
        self.marca.setPlaceholderText("")
        self.marca.setObjectName("marca")
        self.marca.addItem("")
        self.marca.addItem("")
        self.gridLayout_3.addWidget(self.marca, 3, 4, 1, 1)
        #spacer
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
        #in_arrivo button
        self.in_arrivo = QtWidgets.QPushButton(self.topWidget)
        self.in_arrivo.setObjectName("in_arrivo")
        self.gridLayout_3.addWidget(self.in_arrivo, 1, 0, 1, 1)
        #in_negozio button
        self.in_negozio = QtWidgets.QPushButton(self.topWidget)
        self.in_negozio.setObjectName("in_negozio")
        self.gridLayout_3.addWidget(self.in_negozio, 1, 1, 1, 1)
        #venduto button
        self.venduto = QtWidgets.QPushButton(self.topWidget)
        self.venduto.setObjectName("venduto")
        self.gridLayout_3.addWidget(self.venduto, 1, 2, 1, 1)
        # reso button
        self.reso = QtWidgets.QPushButton(self.topWidget)
        self.reso.setObjectName("reso")
        self.gridLayout_3.addWidget(self.reso, 1, 3, 1, 1)

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

        #-------------centralWidget---------------
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
        #primo blocco    (da iterare con un for?)
        self.prima_colonna = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prima_colonna.sizePolicy().hasHeightForWidth())
        self.prima_colonna.setSizePolicy(sizePolicy)
        self.prima_colonna.setMinimumSize(QtCore.QSize(200, 400))
        self.prima_colonna.setObjectName("prima_colonna")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.prima_colonna)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.immagine = QtWidgets.QLabel(self.prima_colonna)
        self.immagine.setObjectName("immagine")
        pixmap = QPixmap('listaprodotti/data/images/' + str(self.cod_prodotto()) + '.jpg')
        self.immagine.setPixmap(pixmap)
        self.verticalLayout_2.addWidget(self.immagine)
        self.nome_marca = QtWidgets.QLabel(self.prima_colonna)
        self.nome_marca.setObjectName("nome_marca")
        self.verticalLayout_2.addWidget(self.nome_marca)
        self.prezzo = QtWidgets.QLabel(self.prima_colonna)
        self.prezzo.setObjectName("prezzo")
        self.verticalLayout_2.addWidget(self.prezzo)
        self.gridLayout_2.addWidget(self.prima_colonna, 0, 0, 1, 1)
        # terzo blocco
        self.terza_colonna = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terza_colonna.sizePolicy().hasHeightForWidth())
        self.terza_colonna.setSizePolicy(sizePolicy)
        self.terza_colonna.setMinimumSize(QtCore.QSize(200, 400))
        self.terza_colonna.setObjectName("terza_colonna")
        self.gridLayout_2.addWidget(self.terza_colonna, 0, 4, 1, 1)

        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 400))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(200, 400))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2.addWidget(self.widget_5, 2, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 0, 3, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 2, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 2, 3, 1, 1)
        self.seconda_colonna = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seconda_colonna.sizePolicy().hasHeightForWidth())
        self.seconda_colonna.setSizePolicy(sizePolicy)
        self.seconda_colonna.setMinimumSize(QtCore.QSize(200, 400))
        self.seconda_colonna.setObjectName("seconda_colonna")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.seconda_colonna)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.immagine_2 = QtWidgets.QLabel(self.seconda_colonna)
        self.immagine_2.setObjectName("immagine_2")
        self.verticalLayout_3.addWidget(self.immagine_2)
        self.nome_marca_2 = QtWidgets.QLabel(self.seconda_colonna)
        self.nome_marca_2.setObjectName("nome_marca_2")
        self.verticalLayout_3.addWidget(self.nome_marca_2)
        self.prezzo_2 = QtWidgets.QLabel(self.seconda_colonna)
        self.prezzo_2.setObjectName("prezzo_2")
        self.verticalLayout_3.addWidget(self.prezzo_2)
        self.gridLayout_2.addWidget(self.seconda_colonna, 0, 2, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(200, 400))
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_2.addWidget(self.widget_6, 2, 4, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        #QtWidgets.QMainWindow.setCentralWidget(self.centralwidget)     NON RIESCO A METTERLA A TUTTO SCHERMO

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.taglia.setItemText(0, _translate("MainWindow", "Taglia"))
        self.genere.setItemText(0, _translate("MainWindow", "Uomo"))
        self.genere.setItemText(1, _translate("MainWindow", "Donna"))
        self.genere.setItemText(2, _translate("MainWindow", "Bambino"))
        self.genere.setItemText(3, _translate("MainWindow", "Bambina"))
        self.in_arrivo.setText(_translate("MainWindow", "IN ARRIVO"))
        self.tipo.setItemText(0, _translate("MainWindow", "Eleganti"))
        self.tipo.setItemText(1, _translate("MainWindow", "Sneakers"))
        self.tipo.setItemText(2, _translate("MainWindow", "Sportive"))
        self.tipo.setItemText(3, _translate("MainWindow", "Trekking"))
        self.in_negozio.setText(_translate("MainWindow", "IN NEGOZIO"))
        self.marca.setCurrentText(_translate("MainWindow", "Armani"))
        self.marca.setItemText(0, _translate("MainWindow", "Armani"))
        self.marca.setItemText(1, _translate("MainWindow", "Pier One"))
        self.collezione.setItemText(0, _translate("MainWindow", "Primavera/Estate"))
        self.collezione.setItemText(1, _translate("MainWindow", "Autunno/Inverno"))
        self.venduto.setText(_translate("MainWindow", "VENDUTO"))
        self.indietro.setText(_translate("MainWindow", "< Indietro"))
        self.reso.setText(_translate("MainWindow", "RESO"))
        self.nome_marca.setText(_translate("MainWindow", "Marca - Nome prodotto"))
        self.prezzo.setText(_translate("MainWindow", "Prezzo"))
        self.immagine_2.setText(_translate("MainWindow", "TextLabel"))
        self.nome_marca_2.setText(_translate("MainWindow", "Marca - Nome prodotto"))
        self.prezzo_2.setText(_translate("MainWindow", "Prezzo"))

    # class VistaListaProdotti(QWidget):
    #     def __init__(self, parent=None):
    #         super(VistaListaProdotti, self).__init__(parent)
    #         self.controller = ControllerListaProdotti()
    #
    #         """
    #             SEZIONE FILTRAGGIO
    #         """
    #
    #
    #
    #         """
    #             SEZIONE VISUALIZZAZIONE DEI PRODOTTI
    #         """
    #         h_layout = QHBoxLayout()
    #         self.list_view = QListView()
    #         self.update_ui()
    #         h_layout.addWidget(self.list_view)
    #
    #         buttons_layout = QVBoxLayout()
    #         open_button = QPushButton('Vedi dettagli')
    #         open_button.clicked.connect(self.show_prodotto)
    #         buttons_layout.addWidget(open_button)
    #         new_button = QPushButton("Inserisci prodotto")
    #         new_button.clicked.connect(self.show_inserici_prodotto)
    #         buttons_layout.addWidget(new_button)
    #         home_button = QPushButton("Torna alla HOME")
    #         home_button.clicked.connect(self.show_home)
    #         buttons_layout.addWidget(home_button)
    #         buttons_layout.addStretch()
    #         h_layout.addLayout(buttons_layout)
    #
    #         self.setLayout(h_layout)
    #         #self.resize(600, 300)
    #         self.setWindowTitle('Area Prodotti')
    #
    #     def update_ui(self):
    #         self.listview_model = QStandardItemModel(self.list_view)
    #         for prodotto in self.controller.get_lista_prodotti():
    #             item = QStandardItem()
    #             image = QLabel()
    #             pixmap = QPixmap('listaprodotti/data/images/' + prodotto.cod_prodotto + '.jpg')
    #             image.setPixmap(pixmap)
    #             item.setText("      Marca: " + str(prodotto.marca) + "      Nome: " + str(prodotto.marca) + "      Taglia: "
    #                          + str(prodotto.taglia) + "         Quantità: " + str(prodotto.quantita) + "         Stato: " + str(prodotto.stato))
    #             item.setEditable(False)
    #             font = item.font()
    #             font.setPointSize(18)
    #             item.setFont(font)
    #             self.listview_model.appendColumn(image)
    #             self.listview_model.appendRow(item)
    #         self.list_view.setModel(self.listview_model)

    # def show_prodotto(self):
    #     if len(self.list_view.selectedIndexes()) > 0:
    #         selected = self.list_view.selectedIndexes()[0].row()
    #         prodotto_selezionato = self.controller.get_prodotto(selected)
    #         self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_codice,
    #                                             ControllerProdotto.modifica_prodotto_by_codice, self.update_ui)
    #         self.vista_prodotto.showMaximized()
    #         time.sleep(0.3)
    #         self.close()

    def show_inserici_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.update_ui)
        self.vista_inserisci_prodotto.show()

    def show_home(self):
        self.vista_home = home.view.VistaHome.VistaHome()
        self.vista_home.showMaximized()
        time.sleep(0.3)
        self.close()

    # crea l'elenco dei codici dei prodotti da visualizzare basati sui filtri
    def cod_prodotto(self):
        return 'S01'

    def show_in_arrivo(self):
        pass

    def show_in_negozio(self):
        pass

    def show_venduto(self):
        pass

    def show_reso(self):
        pass

    def closeEvent(self, event):
        pass
        #self.controller.save_data()
