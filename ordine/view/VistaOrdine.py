from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from ordine.controller.ControllerOrdine import ControllerOrdine


def get_info(text):
    label = QLabel(text)
    font = label.font()
    font.setPointSize(17)
    label.setFont(font)
    return label


class VistaOrdine(QWidget):
    def __init__(self, c_ordine):
        super(VistaOrdine, self).__init__(c_ordine)
        self.controller = ControllerOrdine(c_ordine)
        self.elimina_ordine = self.elimina_ordine
        self.modifica_ordine = self.modifica_ordine
        self.update_ordine = self.update_ordine

        v_layout = QVBoxLayout()

        label_nome = QLabel(c_ordinesf                                                                                                                                   + " " + self.controller.get_taglia())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)



        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        v_layout.addWidget(get_info("Codice fornitore: {}".format(self.controller.get_cod_fornitore())))
        v_layout.addWidget(get_info("Data listaordine: {}".format(self.controller.get_data_ordine())))
        v_layout.addWidget(get_info("Codice prodotto: {}".format(self.controller.get_cod_prodotto())))
        v_layout.addWidget(get_info("Materiale: {}".format(self.controller.get_materiale())))
        v_layout.addWidget(get_info("Colore: {}".format(self.controller.get_colore())))
        v_layout.addWidget(get_info("Taglia: {}".format(self.controller.get_taglia())))
        v_layout.addWidget(get_info("Quantita: {}".format(self.controller.get_quantita())))
        v_layout.addWidget(get_info("Prezzo di vendita: {}".format(self.controller.get_prezzo_vendita())))
        v_layout.addWidget(get_info("Stagione: {}".format(self.controller.get_stagione())))
        v_layout.addWidget(get_info("Stato: {}".format(self.controller.get_stato())))
        v_layout.addWidget(get_info("Data di vendita: {}".format(self.controller.get_data_vendita())))


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_ordine_click)
        v_layout.addWidget(btn_elimina)

        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_ordine_click)
        v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_cod_ordine())

    def elimina_ordine_click(self):
        self.elimina_ordine(self.controller.get_cod_ordine())
        self.update_ordine()
        self.close()

    def modifica_ordine_click(self):
        self.modifica_ordine(self.controller.get_cod_ordine())
        self.update_ordine()
        self.close()
