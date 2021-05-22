from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
import time

import home.view.VistaHome
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.view.VistaProdotto import VistaProdotto
from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.controller.ControllerProdotto import ControllerProdotto


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)

        self.controller = ControllerListaProdotti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Vedi dettagli')
        open_button.clicked.connect(self.show_prodotto)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Inserisci prodotto")
        new_button.clicked.connect(self.show_inserici_prodotto)
        buttons_layout.addWidget(new_button)
        home_button = QPushButton("Torna alla HOME")
        home_button.clicked.connect(self.show_home)
        buttons_layout.addWidget(home_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        #self.resize(600, 300)
        self.setWindowTitle('Area Prodotti')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in self.controller.get_lista_prodotti():
            item = QStandardItem()
            item.setText("      Marca: " + str(prodotto.marca) + "      Nome: " + str(prodotto.marca) + "      Taglia: "
                         + str(prodotto.taglia) + "         Quantità: " + str(prodotto.quantita) + "         Stato: " + str(prodotto.stato))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_prodotto(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto(selected)
            self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_codice,
                                                ControllerProdotto.modifica_prodotto_by_codice, self.update_ui)
            self.vista_prodotto.showMaximized()

    def show_inserici_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.update_ui)
        self.vista_inserisci_prodotto.show()

    def show_home(self):
        self.vista_home = home.view.VistaHome.VistaHome()
        self.vista_home.showMaximized()
        time.sleep(0.3)
        self.close()

    def closeEvent(self, event):
        self.controller.save_data()
