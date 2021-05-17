from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from Ordine.controller.Controller0rdine import ControllerOrdine


class VistaOrdine(QWidget):
    def __init__(self, Ordine, parent=None):
        super(VistaOrdine, self).__init__(parent)
        self.controller = ControllerOrdine(Ordine)

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label_fattura = QLabel(self.controller.get_codice_fattura())
        font_fattura = label_fattura.font()
        font_fattura.setPointSize(30)
        label_fattura.setFont(font_fattura)
        v_layout.addWidget(label_fattura)

        label_fornitore = QLabel("Tipo: {}".format(self.controller.get_codice_dornitore()))
        font_fornitore = label_fornitore.font()
        font_fornitore.setPointSize(17)
        label_fornitore.setFont(font_fornitore)
        v_layout.addWidget(label_fornitore)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        label_stagione = QLabel("stagione: {}".format(self.controller.get_stagione()))
        font_stagione = label_stagione.font()
        font_stagione.setPointSize(17)
        label_stagione.setFont(font_stagione)
        v_layout.addWidget(label_stagione)
        h_layout.addLayout(v_layout)

        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()
        label_stato = QLabel("stato: {}".format(self.controller.get_prezzo_servizio()))
        font_stato = label_prezzo.font()
        font_stato.setPointSize(25)
        label_stato.setFont(font_stato)
        v_layout2.addWidget(label_stato)

        label_data_arrivo = QLabel(self.controller.get_data_di_arrivo())
        font_data_arrivo = label_disponibile.font()
        font_data_arrivo.setPointSize(25)
        label_data_arrivo.setFont(font_data_arrivo)
        v_layout2.addWidget(label_data_arrivo)

        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.setWindowTitle(Ordine.nome)