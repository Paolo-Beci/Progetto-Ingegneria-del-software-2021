from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox

from utente.model.Utente import Utente


class VistaInserisciUtente(QWidget):
    def __init__(self, controller, update_ui):
        super(VistaInserisciUtente, self).__init__()
        self.controller = controller
        self.update_ui = update_ui

        self.v_layout = QVBoxLayout()

        #oggetto: "campo", "valore"
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("data_n", "Data di nascita (dd/MM/yyyy)")
        self.add_info_text("luogo_n", "Luofo di nascita")
        self.add_info_text("eta", "Età")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("codice_utente", "Codice utente")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("ruolo", "Ruolo (Amministratore/Dipendente")
        self.add_info_text("stipendio", "Stipendio")
        self.add_info_text("data_scad_contratto", "Data di scadenza del contratto (dd/MM/yyyy)")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_utente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Utente")

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


        self.controller.inserisci_utente(Utente(
             self.qlines["nome"].text(),
             self.qlines["cognome"].text(),
             self.qlines["data_n"].text(),
             self.qlines["luogo_n"].text(),
             self.qlines["eta"].text(),
             self.qlines["cf"].text(),
             self.qlines["codice_utente"].text(),
             self.qlines["telefono"].text(),
             self.qlines["ruolo"].text(),
             self.qlines["stipendio"].text(),
             self.qlines["data_scad_contratto"].text()))
        self.update_ui()
        self.close()

