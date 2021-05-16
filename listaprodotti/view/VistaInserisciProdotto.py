from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prodotto.model.Prodotto import Prodotto


class VistaInserisciProdotto(QWidget):
    def __init__(self, controller):
        # callback ??
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        # self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")
        self.get_form_entry("Email")
        self.get_form_entry("Telefono")
        self.get_form_entry("Età")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_prodotto)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserisci prodotto")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def inserisci_prodotto(self):   # DA FARE
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        cf = self.info["Codice Fiscale"].text()
        indirizzo = self.info["Indirizzo"].text()
        email = self.info["Email"].text()
        telefono = self.info["Telefono"].text()
        eta = self.info["Età"].text()
        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" or eta == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prodotto(Prodotto((nome+cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, eta))
            self.callback()
            self.close()
