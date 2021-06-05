import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
import time

from listaordini.view.VistaListaOrdini import VistaListaOrdini
from listadelpersonale.view.VistaListaDelPersonale import VistaListaDelPersonale
from listaprodotti.view.VistaListaProdotti import VistaListaProdotti
from listafornitori.view.VistaListaFornitori import VistaListaFornitori
from listastatistiche.view.VistaListaStatistiche import VistaListaStatistiche
from prodotto.view.VistaModificaProdotto import VistaModificaProdotto

"""
    VISTA HOME
"""


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Area Statistiche <<beta>>", self.go_lista_statistiche), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Area Prodotti <<beta>>", self.go_lista_prodotti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Area Fornitori <<beta>>", self.go_lista_fornitori), 0, 2)
        grid_layout.addWidget(self.get_generic_button("Area Ordini <<beta>>", self.go_lista_ordini), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Area Vendita <<beta>>", self.go_vista_vendita), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Area del Personale <<beta>>", self.go_lista_del_personale), 1, 2)

        self.setLayout(grid_layout)
        self.setWindowTitle("Gestore negozio di calzature")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_statistiche(self):
        self.vista_lista_statistiche = VistaListaStatistiche()
        self.vista_lista_statistiche.showMaximized()
        time.sleep(0.3)
        self.close()

    def go_lista_prodotti(self):
        self.vista_lista_prodotti = VistaListaProdotti()
        self.vista_lista_prodotti.showMaximized()
        time.sleep(0.3)
        self.close()

    def go_lista_fornitori(self):
        self.vista_lista_fornitori = VistaListaFornitori()
        self.vista_lista_fornitori.show()

    def go_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.showMaximized()
        time.sleep(0.3)
        self.close()

    def go_vista_vendita(self):
        pass

    def go_lista_del_personale(self):
        self.vista_lista_del_personale = VistaListaDelPersonale()
        self.vista_lista_del_personale.show()
