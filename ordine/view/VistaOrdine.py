import time
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from ordine.controller.ControllerOrdine import ControllerOrdine
from ordine.model import Ordine


class VistaOrdine(QWidget):
    def __init__(self, c_prodotto, elimina_prodotto, modifica_prodotto, update_ui, parent=None):
        super(VistaOrdine, self).__init__(parent)
        # self.prodotto = self.controller.get_prodotto(c_prodotto)
        self.controller = ControllerOrdine(c_prodotto)
        self.elimina_ordine = elimina_prodotto
        self.modifica_ordine = modifica_prodotto
        self.update_ui = update_ui

        v_layout = QVBoxLayout()

        label_nome = QLabel(str(self.controller.get_cod_prodotto()) + " " + str(self.controller.get_taglia()))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # LOAD IMMAGINE
        #label = QLabel(self)
        #pixmap = QPixmap('listaprodotti/data/images/immagine_prova.jpg')
        #label.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())

        #self.photo = QtWidgets.QLabel(self.centralwidget)
        #self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        #self.photo.setText("")
        #self.photo.setPixmap(QtGui.QPixmap("cat.jpg"))
        #self.photo.setScaledContents(True)
        #self.photo.setObjectName("photo")

        v_layout.addWidget(self.get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        v_layout.addWidget(self.get_info("Codice fornitore: {}".format(self.controller.get_cod_fornitore())))
        v_layout.addWidget(self.get_info("Data ordine: {}".format(self.controller.get_data_ordine())))
        v_layout.addWidget(self.get_info("Codice prodotto: {}".format(self.controller.get_cod_prodotto())))
        v_layout.addWidget(self.get_info("Marca: {}".format(self.controller.get_marca())))
        v_layout.addWidget(self.get_info("Nome: {}".format(self.controller.get_nome())))
        v_layout.addWidget(self.get_info("Tipo: {}".format(self.controller.get_tipo())))
        v_layout.addWidget(self.get_info("Genere: {}".format(self.controller.get_genere())))
        v_layout.addWidget(self.get_info("Materiale: {}".format(self.controller.get_materiale())))
        v_layout.addWidget(self.get_info("Colore: {}".format(self.controller.get_colore())))
        v_layout.addWidget(self.get_info("Taglia: {}".format(self.controller.get_taglia())))
        v_layout.addWidget(self.get_info("Quantita: {}".format(self.controller.get_quantita())))
        v_layout.addWidget(self.get_info("Prezzo di acquisto: {}".format(self.controller.get_prezzo_acquisto())))
        v_layout.addWidget(self.get_info("Prezzo di vendita: {}".format(self.controller.get_prezzo_vendita())))
        v_layout.addWidget(self.get_info("Stagione: {}".format(self.controller.get_stagione())))
        v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))
        v_layout.addWidget(self.get_info("Sconto consigliato: {}".format(self.controller.get_sconto_consigliato())))
        v_layout.addWidget(self.get_info("Sconto applicato: {}".format(self.controller.get_sconto())))
        v_layout.addWidget(self.get_info("Data di vendita: {}".format(self.controller.get_data_vendita())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_prodotto_click)
        v_layout.addWidget(btn_elimina)

        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_prodotto_click)
        v_layout.addWidget(btn_modifica)

        btn_back = QPushButton("Torna indietro")
        btn_back.clicked.connect(self.show_back_click)
        v_layout.addWidget(btn_back)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_cod_prodotto())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    """
        Eventi trigger click dei bottoni
    """
    def elimina_ordine_click(self):
        self.elimina_prodotto_by_codice(self.controller.get_cod_prodotto())
        self.update_ui()
        self.close()

    def modifica_ordine_click(self):
        self.showMaximized(Ordine.view.VistaModificaOrdine.VistaModificaOrdine(self.controller.get_cod_prodotto()))
        self.update_ui()
        self.close()

    def show_back_click(self, listaOrdine=None):
        self.vista_back = listaOrdine.view.VistaListaOrdine.VistaListaOrdini()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()
