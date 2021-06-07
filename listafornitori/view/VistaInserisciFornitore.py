from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox

from fornitore.model.Fornitore import Fornitore


class VistaInserisciFornitore(QWidget):
    def __init__(self, controller, update_ui):
        super(VistaInserisciFornitore, self).__init__()
        self.controller = controller
        self.update_ui = update_ui

        self.v_layout = QVBoxLayout()

        #oggetto: "campo", "valore"
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("partita_iva", "Partita iva")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("sito_web", "Sito web")
        self.add_info_text("rappresentante", "Rappresentante")
        self.label_data_affiliazione= QLabel("Data affiliazione")
        self.v_layout.addWidget(self.label_data_affiliazione)
        self.dateEdit_data_affiliazione= QtWidgets.QDateEdit(self)
        self.v_layout.addWidget(self.dateEdit_data_affiliazione)
        self.add_info_text("codice_fornitore", "Codice Fornitore")
        self.label_stato = QLabel("Stato")
        self.v_layout.addWidget(self.label_stato)
        self.combo_box_stato= QtWidgets.QComboBox(self)
        self.combo_box_stato.addItem("Standard")
        self.combo_box_stato.addItem("Premium")
        self.combo_box_stato.setCurrentIndex(0)
        self.v_layout.addWidget(self.combo_box_stato)


        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_utente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Fornitore")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def inserisci_utente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        for fornitore in self.controller.get_lista_fornitori():
            if fornitore.partita_iva == self.qlines["partita_iva"].text():
                QMessageBox.critical(self, 'Errore', 'Fornitore già presente in lista!', QMessageBox.Ok, QMessageBox.Ok)
                return

        gg= str(self.dateEdit_data_affiliazione.date().day())
        mm= str(self.dateEdit_data_affiliazione.date().month())
        aaaa= str(self.dateEdit_data_affiliazione.date().year())
        data_affiliazione= gg + "/" + mm + "/" + aaaa
        if str(self.combo_box_stato.currentText()) == "Standard":
            stato= "S"
        else:
            stato= "P"

        self.controller.inserisci_fornitore(Fornitore(
             self.qlines["codice_fornitore"].text(),
             self.qlines["nome"].text(),
             self.qlines["indirizzo"].text(),
             self.qlines["telefono"].text(),
             self.qlines["partita_iva"].text(),
             self.qlines["sito_web"].text(),
             self.qlines["rappresentante"].text(),
             data_affiliazione,
             stato))
        self.update_ui()
        self.close()

