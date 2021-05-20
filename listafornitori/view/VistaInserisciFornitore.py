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
        self.add_info_text("email", "Email")
        self.add_info_text("rappresentante", "Rappresentante")
        self.add_info_text("data_affiliazione", "Data di affiliazione (dd/MM/yyyy)")
        self.add_info_text("codice_fornitore", "Codice Fornitore")
        self.add_info_text("stato", "Stato (Standard/Premium")


        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_utente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Fornitore")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        current_text.setText("testodiprovazi")
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def inserisci_utente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return


        self.controller.inserisci_fornitore(Fornitore(
             self.qlines["nome"].text(),
             self.qlines["indirizzo"].text(),
             self.qlines["partita_iva"].text(),
             self.qlines["telefono"].text(),
             self.qlines["email"].text(),
             self.qlines["rappresentante"].text(),
             self.qlines["data_affiliazione"].text(),
             self.qlines["codice_fornitore"].text(),
             self.qlines["stato"].text()))
        self.update_ui()
        self.close()

