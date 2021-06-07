from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
import time

import home.view.VistaHome
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from listaordini.view.VistaInserisciOrdine import VistaInserisciOrdine
from ordine.controller.ControllerOrdine import ControllerOrdine
from ordine.view.VistaOrdine import VistaOrdine
from listaordini.view.VistaInserisciOrdine import VistaInserisciOrdine

class VistaListaOrdini(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)

        self.controller= ControllerListaOrdini()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Vedi dettagli')
        #ici jai juste appliquer le bouton
        open_button.clicked.connect(self.show_ordine)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Inserisci ordine")
        new_button.clicked.connect(self.show_inserici_ordine)
        buttons_layout.addWidget(new_button)
        home_button = QPushButton("Torna alla HOME")
        #home_button.clicked.connect(s
        home_button.clicked.connect(self.close)
        buttons_layout.addWidget(home_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        #self.resize(600, 300)
        self.setWindowTitle('Area Ordini')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for ordine in self.controller.get_lista_ordini():
            item = QStandardItem()
            item.setText("      Marca: " + str(ordine.marca) + "      Nome: " + str(ordine.marca) + "      Taglia: "
                         + str(ordine.taglia) + "         Quantità: " + str(
                ordine.quantita) + "         Stato: " + str(ordine.stato))
           # item.setText("Marca: " + self.controller.get_lista_ordini())
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)



    def show_ordine(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            ordine_selezionato = self.controller.get_ordine(selected)
            self.vista_ordine = VistaOrdine(ordine_selezionato, self.controller.elimina_ordine_by_codice,
                                                ControllerOrdine.modifica_ordine_by_codice, self.update_ui)
            self.vista_ordine.showMaximized()
            time.sleep(0.3)
            self.close()

    def show_inserici_ordine(self):
        self.vista_inserisci_ordine = VistaInserisciOrdine(self.controller, self.update_ui)
        self.vista_inserisci_ordine.show()

    def closeEvent(self, event):
        self.controller.save_data()
