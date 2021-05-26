import time

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QHBoxLayout, QPushButton

from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from statistica.contorller.ControllerStatistica import ControllerStatistica
import listastatistiche.view.VistaListaStatistiche


class VistaStatistica(QWidget):
    def __init__(self, statistica, selected, parent=None):
        super(VistaStatistica, self).__init__(parent)
        self.controller_stat = ControllerStatistica(statistica)
        self.controller_prod = ControllerListaProdotti()
        self.controller_forn = ControllerListaFornitori()
        self.controller_stat.smistatore_statistica(selected)

        v_layout = QVBoxLayout()

        label_nome = QLabel("TOP " + str(self.controller_stat.get_quantita()) + ": " + self.controller_stat.get_nome())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        self.list_view = QListView()
        self.smistatore_viste(selected)
        v_layout.addWidget(self.list_view)

        v_layout.addItem(QSpacerItem(250, 250, QSizePolicy.Minimum, QSizePolicy.Minimum))

        back_button = QPushButton("Torna indietro")
        back_button.clicked.connect(self.show_back_click)
        v_layout.addWidget(back_button)

        self.setLayout(v_layout)
        self.setWindowTitle(statistica.nome)

    #Metodo che consente di visualizzare la lista degli elementi passata con ulteriori informazioni
    def update_ui(self, lista_ordinata, indice):
        self.listview_model = QStandardItemModel(self.list_view)
        for (index, (codice, valore)) in enumerate(lista_ordinata):
            item = QStandardItem()
            if indice == 0 or indice == 1:
                marca = self.controller_prod.get_marca_prodotto_by_code(codice)
                nome = self.controller_prod.get_nome_prodotto_by_code(codice)
                item.setText(str(index + 1) + ") Cod. Prodotto: " + str(codice) + "      Marca: " + str(marca)
                             + "      Nome: " + str(nome) + "      Quantità vendute: " + str(valore))
            elif indice == 2:
                marca = self.controller_prod.get_marca_prodotto_by_code(codice)
                nome = self.controller_prod.get_nome_prodotto_by_code(codice)
                item.setText(str(index + 1) + ") Cod. Prodotto: " + str(codice) + "      Marca: " + str(marca)
                             + "      Nome: " + str(nome) + "      Guadagno: " + str(valore) + " €")

            elif indice == 3:
                nome = self.controller_forn.get_nome_fornitore_by_code(codice)
                stato = self.controller_forn.get_stato_fornitore_by_code(codice)
                item.setText(str(index + 1) + ") Cod. Fornitore: " + str(codice) + "      Nome: " + str(nome)
                             + "      Stato: " + str(stato) + "      Importo totale: " + str(valore) + " €")

            elif indice == 4:
                nome = self.controller_forn.get_nome_fornitore_by_code(codice)
                stato = self.controller_forn.get_stato_fornitore_by_code(codice)
                item.setText(str(index + 1) + ") Cod. Fornitore: " + str(codice) + "      Nome: " + str(nome)
                             + "      Stato: " + str(stato) + "      Calzature totali: " + str(valore))

            elif indice == 5:
                nome = self.controller_forn.get_nome_fornitore_by_code(codice)
                stato = self.controller_forn.get_stato_fornitore_by_code(codice)
                item.setText(str(index + 1) + ") Cod. Fornitore: " + str(codice) + "      Nome: " + str(nome)
                             + "      Stato: " + str(stato) + "      Giorni di ritardo: " + str(valore))

            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    #Metodo che in base alla statistica scelta mostra una vista differente
    def smistatore_viste(self, smistatore):
        if smistatore == 0:
            self.update_ui(
                self.controller_stat.ordinamento_decrescente_prod(self.controller_stat.costruzione_dizionario()),
                smistatore)
        elif smistatore == 1:
            self.update_ui(
                self.controller_stat.ordinamento_crescente_prod(self.controller_stat.costruzione_dizionario()),
                smistatore)
        elif smistatore == 2:
            self.update_ui(self.controller_stat.ordinamento_decrescente_prod(self.controller_stat.prod_piu_redditizi()),
                           smistatore)
        elif smistatore == 3:
            self.update_ui(self.controller_stat.ordinamento_decrescente_forn(self.controller_stat.forn_piu_pagati()),
                           smistatore)
        elif smistatore == 4:
            self.update_ui(self.controller_stat.ordinamento_decrescente_forn(
                self.controller_stat.forn_da_cui_acquistiamo_di_piu()), smistatore)
        elif smistatore == 5:
            self.update_ui(self.controller_stat.ordinamento_crescente_forn(
                self.controller_stat.forn_piu_rapidi_nella_consegna()), smistatore)

    # Metodo che consente di tornare alla shermata precedente
    def show_back_click(self):
        self.vista_back = listastatistiche.view.VistaListaStatistiche.VistaListaStatistiche()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()
