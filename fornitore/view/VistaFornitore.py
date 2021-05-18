from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton

from fornitore.controller.ControllerFornitore import ControllerFornitore


class VistaFornitore(QWidget):
    def __init__(self, fornitore, elimina_fornitore_by_codice, update_ui, parent=None):
        super(VistaFornitore, self).__init__(parent)
        self.controller= ControllerFornitore(fornitore)
        self.elimina_fornitore_by_codice= elimina_fornitore_by_codice
        self.update_ui= update_ui

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Indirizzo: {}".format(self.controller.get_indirizzo())))
        v_layout.addWidget(self.get_info("Partita iva: {}".format(self.controller.get_partita_iva())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono())))
        v_layout.addWidget(self.get_info("Email: {}".format(self.controller.get_email())))
        v_layout.addWidget(self.get_info("Rappresentante: {}".format(self.controller.get_rappresentante())))
        v_layout.addWidget(self.get_info("Data affiliazione: {}".format(self.controller.get_data_affiliazione())))
        v_layout.addWidget(self.get_info("Codice fornitore: {}".format(self.controller.get_codice_fornitore())))
        v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_fornitore_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_fornitore_click(self):
        self.elimina_fornitore_by_codice(self.controller.get_codice_fornitore())
        self.update_ui()
        self.close()