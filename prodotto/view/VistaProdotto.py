import time

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QHBoxLayout, \
    QGridLayout, QGroupBox, QLineEdit, QDateEdit
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets

from prodotto.view.VistaModificaProdotto import VistaModificaProdotto
from prodotto.controller.ControllerProdotto import ControllerProdotto
import listaprodotti.view.VistaListaProdotti

"""
    VISUALIZZAZIONE DEI PARAMETRI DEL PRODOTTO
    Da fare: UI
"""


class VistaProdotto(QWidget):
    def __init__(self, c_prodotto, elimina_prodotto, modifica_prodotto, update_ui, parent=None):
        super(VistaProdotto, self).__init__(parent)
        self.controller = ControllerProdotto(c_prodotto)
        self.elimina_prodotto = elimina_prodotto
        self.modifica_prodotto = modifica_prodotto
        self.update_ui = update_ui

        """
            SEZIONE SUPERIORE INTERFACCIA (topLayout)
        """
        topLayout = QGridLayout()
        topLayout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        btn_back = QPushButton("Torna indietro")
        btn_back.clicked.connect(self.show_back_click)
        topLayout.addWidget(btn_back)
        topLayout.addLayout(topLayout, 0, 0, 1, 2)
        topLayout.setColumnStretch(0, 1)
        topLayout.setColumnStretch(1, 1)
        topLayout.setColumnStretch(2, 1)
        topLayout.setColumnStretch(3, 1)
        topLayout.setColumnStretch(4, 1)
        topLayout.setColumnStretch(5, 1)
        topLayout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        """
            SEZIONE CENTRALE INTERFACCIA (centerLayout)
        """
        # inizializzazione blocchi interfaccia
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftGroupBox()
        self.createBottomRightGroupBox()

        # posizionamento interfaccia
        centerLayout = QGridLayout()
        centerLayout.addWidget(self.topLeftGroupBox, 1, 0)
        centerLayout.addWidget(self.topRightGroupBox, 1, 1)
        centerLayout.addWidget(self.bottomLeftGroupBox, 2, 0)
        centerLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        centerLayout.setRowStretch(1, 1)
        centerLayout.setRowStretch(2, 1)
        centerLayout.setColumnStretch(0, 1)
        centerLayout.setColumnStretch(1, 1)

        # v_layout.addWidget(self.get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        # v_layout.addWidget(self.get_info("Codice fornitore: {}".format(self.controller.get_cod_fornitore())))
        # v_layout.addWidget(self.get_info("Data ordine: {}".format(self.controller.get_data_ordine())))
        # v_layout.addWidget(self.get_info("Codice prodotto: {}".format(self.controller.get_cod_prodotto())))
        # v_layout.addWidget(self.get_info("Marca: {}".format(self.controller.get_marca())))
        # v_layout.addWidget(self.get_info("Nome: {}".format(self.controller.get_nome())))
        # v_layout.addWidget(self.get_info("Tipo: {}".format(self.controller.get_tipo())))
        # v_layout.addWidget(self.get_info("Genere: {}".format(self.controller.get_genere())))
        # v_layout.addWidget(self.get_info("Materiale: {}".format(self.controller.get_materiale())))
        # v_layout.addWidget(self.get_info("Colore: {}".format(self.controller.get_colore())))
        # v_layout.addWidget(self.get_info("Taglia: {}".format(self.controller.get_taglia())))
        # v_layout.addWidget(self.get_info("Quantita: {}".format(self.controller.get_quantita())))
        # v_layout.addWidget(self.get_info("Prezzo di acquisto: {}".format(self.controller.get_prezzo_acquisto())))
        # v_layout.addWidget(self.get_info("Prezzo di vendita: {}".format(self.controller.get_prezzo_vendita())))
        # v_layout.addWidget(self.get_info("Stagione: {}".format(self.controller.get_stagione())))
        # v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))
        # v_layout.addWidget(self.get_info("Sconto consigliato: {}".format(self.controller.get_sconto_consigliato())))
        # v_layout.addWidget(self.get_info("Sconto applicato: {}".format(self.controller.get_sconto())))
        # v_layout.addWidget(self.get_info("Data di vendita: {}".format(self.controller.get_data_vendita())))

        centerLayout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        """
            SEZIONE INFERIORE INTERFACCIA (bottomLayout)
        """
        bottomLayout = QGridLayout()

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_prodotto_click)

        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_prodotto_click)

        bottomLayout.setColumnStretch(1, 1)
        bottomLayout.setColumnStretch(2, 1)
        bottomLayout.setColumnStretch(3, 1)
        bottomLayout.addWidget(btn_modifica, 1, 3)
        bottomLayout.addWidget(btn_elimina, 1, 5)

        # Allocazione interfaccia generale
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addLayout(centerLayout, 1, 0, 1, 2)
        mainLayout.addLayout(bottomLayout, 2, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle(self.controller.get_cod_prodotto())
        # self.setWindowIcon('path')

    """
        Dettagli comuni per le label
    """

    def get_info_label(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

        # CREAZIONE DEI COMPONENTI

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("IMMAGINE")

        # INSERIMENTO IMMAGINE
        label = QLabel(self.topLeftGroupBox)
        pixmap = QPixmap('listaprodotti/data/images/' + self.controller.get_cod_prodotto() + '.jpg')
        # pixmap.scaled(100, 100)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        label.move(100, 50)
        #   come faccio il resize dell'immagine per farla entrare nel box?

        layout = QGridLayout()
        layout.addWidget(label, 0, 0, 2, 4)

        layout.setRowStretch(5, 1)
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("CODICI PRODOTTO E DETTAGLI ORDINE")

        label_nome = QLabel(self.topRightGroupBox)
        label_nome.setText("Codice fattura")

        layout = QGridLayout()
        layout.addWidget(label_nome, 0, 0, 1, 2)
        layout.setRowStretch(4, 1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftGroupBox(self):
        self.bottomLeftGroupBox = QGroupBox("DESCRIZIONE PRODOTTO")

        label_nome = QLabel(self.bottomLeftGroupBox)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        label_nome.setText("Codice fattura")

        dateEdit = QDateEdit(self.bottomLeftGroupBox)
        dateEdit.setDate(QDate.currentDate())

        layout = QGridLayout()
        layout.addWidget(dateEdit, 0, 0, 1, 2)
        layout.addWidget(label_nome, 1, 0, 1, 2)
        layout.setRowStretch(4, 1)
        self.bottomLeftGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("STATO E SCONTI APPLICABLI")

    """
        Eventi trigger click dei bottoni
    """

    def elimina_prodotto_click(self):
        self.elimina_prodotto_by_codice(self.controller.get_cod_prodotto())
        self.update_ui()
        self.close()

    def modifica_prodotto_click(self):
        self.vista_modifica_prodotto = VistaModificaProdotto(self.controller, self.update_ui)
        self.vista_modifica_prodotto.showMaximized()
        self.update_ui()

    def show_back_click(self):
        self.vista_back = listaprodotti.view.VistaListaProdotti.VistaListaProdotti()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()
