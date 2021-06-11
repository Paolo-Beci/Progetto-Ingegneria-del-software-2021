from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from listadelpersonale.view.VistaInserisciUtente import VistaInserisciUtente
from utente.view.VistaUtente import VistaUtente


class VistaListaDelPersonale(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDelPersonale, self).__init__()

        self.controller = ControllerListaDelPersonale()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_utente)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_inserisci_utente)
        buttons_layout.addWidget(new_button)
        home_button = QPushButton('Torna alla HOME')
        home_button.clicked.connect(self.close)
        buttons_layout.addWidget(home_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Area del personale')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for utente in self.controller.get_lista_del_personale():
            item = QStandardItem()
            item.setText(utente.nome + " " + utente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def closeEvent(self, event):
        self.controller.save_data()

    def show_inserisci_utente(self):
        self.vista_inserisci_utente= VistaInserisciUtente(self.controller, self.update_ui)
        self.vista_inserisci_utente.show()

    def show_utente(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            utente_selezionato = self.controller.get_utente_by_index(selected)
            self.vista_utente = VistaUtente(utente_selezionato, self.controller.elimina_utente_by_codice, self.update_ui, self.controller)
            self.vista_utente.show()



