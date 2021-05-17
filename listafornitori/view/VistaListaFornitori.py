from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listafornitori.view.VistaInserisciFornitore import VistaInserisciFornitore


class VistaListaFornitori(QWidget):
    def __init__(self, parent=None):
        super(VistaListaFornitori, self).__init__()

        self.controller = ControllerListaFornitori()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        # open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.inserisci_fornitore)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Area Fornitori')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for fornitore in self.controller.get_lista_fornitori():
            item = QStandardItem()
            item.setText(fornitore.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()

    def inserisci_fornitore(self):
        self.vista_inserisci_fornitore= VistaInserisciFornitore(self.controller, self.update_ui)
        self.vista_inserisci_fornitore.show()


