from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox

from utente.model.Utente import Utente


class VistaInserisciUtente(QWidget):
    def __init__(self, controller, update_ui):
        super(VistaInserisciUtente, self).__init__()
        self.controller = controller
        self.update_ui = update_ui

        #self.setMinimumHeight(700)
        self.setMinimumSize(250, 700)
        #self.setFixedHeight(700)
        #self.setFixedWidth(250)

        self.v_layout = QVBoxLayout()

        #oggetto: "campo", "valore"
        self.qlines = {}

        self.add_info_text("codice_utente", "Codice utente")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")

        self.label_data_nascita = QLabel("Data di nascita")
        self.v_layout.addWidget(self.label_data_nascita)
        self.dateEdit_data_nascita = QtWidgets.QDateEdit(self)
        self.v_layout.addWidget(self.dateEdit_data_nascita)

        self.add_info_text("luogo_n", "Luogo di nascita")
        self.add_info_text("cf", "Codice fiscale")

        self.label_data_inizio_contratto = QLabel("Data inizio contratto")
        self.v_layout.addWidget(self.label_data_inizio_contratto)
        self.dateEdit_data_inizio_contratto = QtWidgets.QDateEdit(self)
        self.v_layout.addWidget(self.dateEdit_data_inizio_contratto)

        self.label_data_scadenza_contratto = QLabel("Data scadenza contratto")
        self.v_layout.addWidget(self.label_data_scadenza_contratto)
        self.dateEdit_data_scadenza_contratto = QtWidgets.QDateEdit(self)
        self.v_layout.addWidget(self.dateEdit_data_scadenza_contratto)

        self.label_ruolo = QLabel("Ruolo")
        self.v_layout.addWidget(self.label_ruolo)
        self.combo_box_ruolo= QtWidgets.QComboBox(self)
        self.combo_box_ruolo.addItem("Dipendente")
        self.combo_box_ruolo.addItem("Amministratore")
        self.combo_box_ruolo.setCurrentIndex(0)
        self.v_layout.addWidget(self.combo_box_ruolo)

        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("stipendio", "Stipendio")

        self.combo_box_ruolo.currentIndexChanged.connect(self.retranslate_ui)

        self.spacer= QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.v_layout.addItem(self.spacer)

        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.inserisci_utente)
        self.v_layout.addWidget(self.btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Utente")

    def retranslate_ui(self):
        if self.combo_box_ruolo.currentText()=="Amministratore":
            self.v_layout.removeItem(self.spacer)
            self.btn_ok.setParent(None)
            self.label_username= QLabel("Username")
            self.lineEdit_username= QLineEdit(self)
            self.label_password= QLabel("Password")
            self.lineEdit_password= QLineEdit(self)
            self.v_layout.addWidget(self.label_username)
            self.v_layout.addWidget(self.lineEdit_username)
            self.v_layout.addWidget(self.label_password)
            self.v_layout.addWidget(self.lineEdit_password)
            self.v_layout.addItem(self.spacer)
            self.v_layout.addWidget(self.btn_ok)
        else:
            self.label_username.setParent(None)
            self.lineEdit_username.setParent(None)
            self.label_password.setParent(None)
            self.lineEdit_password.setParent(None)

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

        gg_n = str(self.dateEdit_data_nascita.date().day())
        mm_n = str(self.dateEdit_data_nascita.date().month())
        aaaa_n = str(self.dateEdit_data_nascita.date().year())
        data_nascita = gg_n + "/" + mm_n + "/" + aaaa_n

        gg_i = str(self.dateEdit_data_inizio_contratto.date().day())
        mm_i = str(self.dateEdit_data_inizio_contratto.date().month())
        aaaa_i = str(self.dateEdit_data_inizio_contratto.date().year())
        data_inizio_contratto = gg_i + "/" + mm_i + "/" + aaaa_i

        gg_s = str(self.dateEdit_data_scadenza_contratto.date().day())
        mm_s = str(self.dateEdit_data_scadenza_contratto.date().month())
        aaaa_s = str(self.dateEdit_data_scadenza_contratto.date().year())
        data_scadenza_contratto = gg_s + "/" + mm_s + "/" + aaaa_s

        if str(self.combo_box_ruolo.currentText()) == "Dipendente":
            ruolo= "D"
            username= None
            password= None
        else:
            ruolo= "A"
            username= self.lineEdit_username.text()
            password= self.lineEdit_password.text()

        self.controller.inserisci_utente(Utente(
            self.qlines["codice_utente"].text(),
             self.qlines["nome"].text(),
             self.qlines["cognome"].text(),
             data_nascita,
             self.qlines["luogo_n"].text(),
             self.qlines["cf"].text(),
             data_inizio_contratto,
             data_scadenza_contratto,
             ruolo,
             self.qlines["indirizzo"].text(),
             self.qlines["telefono"].text(),
             self.qlines["stipendio"].text(),
             username,
             password))

        self.update_ui()
        self.close()
