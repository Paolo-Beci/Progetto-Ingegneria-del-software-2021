from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaordine.controller.ControllerListaOrdine import ControllerListaOrdine
from prodotto.view.VistaProdotto import VistaProdotto
from listaordine.view.VistaInserisciOrdine import VistaInserisciOrdine
from ordine.controller.ControllerOrdine import ControllerOrdine


class VistaListaOrdine(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOrdine, self).__init__(parent)

        self.controller = ControllerListaOrdine()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Vedi dettagli')
        open_button.clicked.connect(self.show_dettagli_ordine)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Inserisci ordine")
        new_button.clicked.connect(self.show_inserici_ordine)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        #self.resize(600, 300)
        self.setWindowTitle('Area Prodotti')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in self.controller.get_lista_prodotti():
            item = QStandardItem()
            item.setText("codice: " + ordine.codice_fattura + "    stagione: " + str(ordine.stagione) + "    stato: " + str(ordine.quantita))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_dettagli_ordine(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            ordine_selezionato = self.controller.get_cod_orddine(selected)
            self.vista_ordine = VistaOrdine(ordine_selezionato)
            self.vista_ordine.show()

    def show_inserici_ordine(self):
        self.vista_inserisci_ordine = VistaInserisciOrdine(self.controller)
        self.vista_inserisci_ordine.show()

    def closeEvent(self, event):
        self.controller.save_data()
