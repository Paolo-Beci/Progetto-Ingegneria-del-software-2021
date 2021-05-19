from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from prodotto.controller.ControllerProdotto import ControllerProdotto
from listaprodotti.model.ListaProdotti import ListaProdotti


class VistaProdotto(QWidget):
    def __init__(self, c_prodotto, elimina_prodotto, update_ui, parent=None):
        super(VistaProdotto, self).__init__(parent)
        # self.prodotto = self.controller.get_prodotto(c_prodotto)
        self.controller = ControllerProdotto(c_prodotto)
        self.elimina_prodotto = elimina_prodotto
        #self.modifica_prodotto = modifica_prodotto
        self.update_ui = update_ui

        v_layout = QVBoxLayout()

        label_nome = QLabel(str(self.controller.get_cod_prodotto()) + " " + str(self.controller.get_taglia()))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        # LOAD IMMAGINE
        #label = QLabel(self)
        #pixmap = QPixmap('listaprodotti/data/images/immagine_prova.jpg')
        #label.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        v_layout.addWidget(self.get_info("Codice fornitore: {}".format(self.controller.get_cod_fornitore())))
        v_layout.addWidget(self.get_info("Data ordine: {}".format(self.controller.get_data_ordine())))
        v_layout.addWidget(self.get_info("Codice prodotto: {}".format(self.controller.get_cod_prodotto())))
        v_layout.addWidget(self.get_info("Genere: {}".format(self.controller.get_genere())))
        v_layout.addWidget(self.get_info("Marca: {}".format(self.controller.get_marca())))
        v_layout.addWidget(self.get_info("Nome: {}".format(self.controller.get_nome())))
        v_layout.addWidget(self.get_info("Materiale: {}".format(self.controller.get_materiale())))
        v_layout.addWidget(self.get_info("Colore: {}".format(self.controller.get_colore())))
        v_layout.addWidget(self.get_info("Taglia: {}".format(self.controller.get_taglia())))
        v_layout.addWidget(self.get_info("Quantita: {}".format(self.controller.get_quantita())))
        v_layout.addWidget(self.get_info("Prezzo di acquisto: {}".format(self.controller.get_prezzo_acquisto())))
        v_layout.addWidget(self.get_info("Prezzo di vendita: {}".format(self.controller.get_prezzo_vendita())))
        v_layout.addWidget(self.get_info("Stagione: {}".format(self.controller.get_stagione())))
        v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))
        v_layout.addWidget(self.get_info("Data di vendita: {}".format(self.controller.get_data_vendita())))
        v_layout.addWidget(self.get_info("Sconto consigliato: {}".format(self.controller.get_sconto_consigliato())))
        v_layout.addWidget(self.get_info("Sconto applicato: {}".format(self.controller.get_sconto())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_prodotto_click)
        v_layout.addWidget(btn_elimina)

        #btn_modifica = QPushButton("Modifica")
        #btn_modifica.clicked.connect(self.modifica_prodotto_click)
        #v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_cod_prodotto())

    def elimina_prodotto_click(self):
        self.elimina_prodotto(self.controller.get_cod_prodotto())
        self.update_prodotti()
        self.close()

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    #def modifica_prodotto_click(self):
    #    self.modifica_prodotto(self.controller.get_cod_prodotto())
    #    self.update_prodotti()
    #    self.close()
