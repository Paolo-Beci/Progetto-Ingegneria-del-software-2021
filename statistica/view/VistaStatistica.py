import time

# import numpy as np
# import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QPushButton

from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from statistica.contorller.ControllerStatistica import ControllerStatistica
import listastatistiche.view.VistaListaStatistiche


class VistaStatistica(QWidget):
    def __init__(self, statistica, selected, anno, stagione, parent=None):
        super(VistaStatistica, self).__init__(parent)
        self.selected = selected
        self.anno = anno
        self.stagione = stagione
        self.controller_stat = ControllerStatistica(statistica)
        self.controller_prod = ControllerListaProdotti()
        self.controller_forn = ControllerListaFornitori()

        self.v_layout = QVBoxLayout()

        if self.controller_stat.get_quantita() is not None and self.anno != "":
            label_nome = QLabel(
                "TOP " + str(self.controller_stat.get_quantita()) + ": " + self.controller_stat.get_nome()
                + " - " + str(self.convertitore_stagione()) + " " + str(self.anno))
        elif self.controller_stat.get_quantita() is not None:
            label_nome = QLabel(
                "TOP " + str(self.controller_stat.get_quantita()) + ": " + self.controller_stat.get_nome()
                + " - " + str(self.convertitore_stagione()))
        else:
            label_nome = QLabel(self.controller_stat.get_nome())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        self.v_layout.addWidget(label_nome)

        self.list_view = QListView()
        self.smistatore_viste()
        self.v_layout.addWidget(self.list_view)

        self.v_layout.addItem(QSpacerItem(200, 200, QSizePolicy.Minimum, QSizePolicy.Minimum))

        back_button = QPushButton("Torna indietro")
        back_button.clicked.connect(self.show_back_click)
        self.v_layout.addWidget(back_button)

        self.setLayout(self.v_layout)
        self.setWindowTitle(statistica.nome)

    # Metodo che consente di visualizzare la lista degli elementi passata con ulteriori informazioni
    def update_ui_stat(self, lista_ordinata):
        self.listview_model = QStandardItemModel(self.list_view)

        if not lista_ordinata:
            item = QStandardItem()
            item.setText("Nessun dato disponibile")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        else:
            for (index, (codice, valore)) in enumerate(lista_ordinata):
                item = QStandardItem()
                if self.selected == 0 or self.selected == 1:
                    prodotto = self.controller_prod.get_prodotto_by_code(codice)
                    nome = self.controller_prod.get_nome_prodotto_by_code(codice)
                    item.setText(
                        str(index + 1) + ") Cod. Prodotto: " + str(prodotto.cod_prodotto)
                                       + "      Marca: " + str(prodotto.marca)
                                       + "      Nome: " + str(nome)
                                       + "      Quantità vendute: " + str(valore))
                elif self.selected == 2:
                    prodotto = self.controller_prod.get_prodotto_by_code(codice)
                    nome = self.controller_prod.get_nome_prodotto_by_code(codice)
                    item.setText(
                        str(index + 1) + ") Cod. Prodotto: " + str(prodotto.cod_prodotto)
                                       + "      Marca: " + str(prodotto.marca)
                                       + "      Nome: " + str(nome)
                                       + "      Guadagno: " + str(valore) + " €")

                elif self.selected == 3:
                    fornitore = self.controller_forn.get_fornitore_by_code(codice)
                    stato = self.controller_forn.get_stato_fornitore_by_code(codice)
                    item.setText(
                        str(index + 1) + ") Cod. Fornitore: " + str(fornitore.cod_fornitore)
                                       + "      Nome: " + str(fornitore.nome)
                                       + "      Stato: " + str(stato)
                                       + "      Importo totale: " + str(valore) + " €")

                elif self.selected == 4:
                    fornitore = self.controller_forn.get_fornitore_by_code(codice)
                    stato = self.controller_forn.get_stato_fornitore_by_code(codice)
                    item.setText(
                        str(index + 1) + ") Cod. Fornitore: " + str(fornitore.cod_fornitore)
                                       + "      Nome: " + str(fornitore.nome)
                                       + "      Stato: " + str(stato)
                                       + "      Calzature totali: " + str(valore))

                elif self.selected == 5:
                    fornitore = self.controller_forn.get_fornitore_by_code(codice)
                    stato = self.controller_forn.get_stato_fornitore_by_code(codice)
                    item.setText(
                        str(index + 1) + ") Cod. Fornitore: " + str(fornitore.cod_fornitore)
                                       + "      Nome: " + str(fornitore.nome)
                                       + "      Stato: " + str(stato)
                                       + "      Giorni di ritardo: " + str(valore))

                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    #Metodo dedicato alla creazione del grafico contenente l'andamento finanziario
    def update_ui_af(self, dizionario_af):
        plt.rcParams['figure.figsize'] = [12, 8]

        index = np.arange(len(dizionario_af.keys()))
        plt.bar(index, dizionario_af.values())
        plt.xticks(index, dizionario_af.keys(), size=12)
        plt.title("Andamento Finanziario")

        plt.show()
        plt.savefig("listastatistiche/data/grafico.png")

    #Metodo che consente la visualizzazione dell'andamento finanziario
    def andamento_finanziario(self, dizionario_af):
        self.update_ui_af(dizionario_af)
        self.immagine = QtWidgets.QLabel()
        self.immagine.setObjectName("immagine")
        #self.immagine.setAlignment(QtCore.Qt.AlignCenter)
        pixmap = QPixmap("listastatistiche/data/grafico.png")
        self.immagine.setPixmap(pixmap)
        self.v_layout.addWidget(self.immagine)


    # Metodo che in base alla statistica scelta mostra una vista differente
    def smistatore_viste(self):
        if self.selected == 0:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 1:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 2:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 3:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 4:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 5:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 6:
            self.andamento_finanziario(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))

    # Metodo che consente di tornare alla shermata precedente
    def show_back_click(self):
        self.vista_back = listastatistiche.view.VistaListaStatistiche.VistaListaStatistiche()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()

    # Metodo che ritorna il nome della stagione competo
    def convertitore_stagione(self):
        if self.stagione == "P/E":
            return "Primavera/Estate"
        elif self.stagione == "A/I":
            return "Autunno/Inverno"
