from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from listaprodotti.view.VistaListaProdotti import VistaListaProdotti
from prodotto.view import VistaProdotto


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        self.vista_lista_prodotti = VistaListaProdotti()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Area Prodotti <<beta>>", self.go_lista_prodotti), 0, 0)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore negozio di calzature")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_prodotti(self):
        self.vista_lista_prodotti.showMaximized()
        #self.vista_lista_prodotti.showFullScreen()     Per tutto schermo senza comandi win10
        self.close()
