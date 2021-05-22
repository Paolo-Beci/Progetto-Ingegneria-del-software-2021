from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from utente.controller.ControllerUtente import ControllerUtente


class VistaUtente(QWidget):
    def __init__(self, utente, elimina_utente_by_codice, update_ui, parent=None):
        super(VistaUtente, self).__init__(parent)
        self.controller= ControllerUtente(utente)
        self.elimina_utente_by_codice= elimina_utente_by_codice
        self.update_ui= update_ui

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Nome e Cognome: {}".format(self.controller.get_nome()+""+self.controller.get_cognome())))
        v_layout.addWidget(self.get_info("Data di nascita: {}".format(self.controller.get_data_nascita())))
        v_layout.addWidget(self.get_info("Luogo di nascita: {}".format(self.controller.get_luogo_nascita())))
        v_layout.addWidget(self.get_info("Età: {}".format(self.controller.get_eta())))
        v_layout.addWidget(self.get_info("Codice fiscale: {}".format(self.controller.get_cf())))
        v_layout.addWidget(self.get_info("Codice utente: {}".format(self.controller.get_codice_utente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono())))
        v_layout.addWidget(self.get_info("Ruolo: {}".format(self.controller.get_ruolo())))
        v_layout.addWidget(self.get_info("Stipendio: {}".format(self.controller.get_stipendio())))
        v_layout.addWidget(self.get_info("Data scadenza contratto: {}".format(self.controller.get_data_scadenza_contratto())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_utente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome()+""+self.controller.get_cognome())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_utente_click(self):
        self.elimina_utente_by_codice(self.controller.get_codice_utente())
        self.update_ui()
        self.close()