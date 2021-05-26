import time

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QHBoxLayout, QPushButton

from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from statistica.contorller.ControllerStatistica import ControllerStatistica
import listastatistiche.view.VistaListaStatistiche


class VistaStatistica(QWidget):
    def __init__(self, statistica, selected, parent=None):
        super(VistaStatistica, self).__init__(parent)
        self.controller_stat = ControllerStatistica(statistica)
        self.controller_prod = ControllerListaProdotti()
        self.controller_stat.smistatore_statistica(selected)

        v_layout = QVBoxLayout()

        label_nome = QLabel("TOP " + str(self.controller_stat.get_quantita()) + ": " + self.controller_stat.get_nome())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        self.list_view = QListView()
        self.smistatore_viste(selected)
        v_layout.addWidget(self.list_view)

        v_layout.addItem(QSpacerItem(250, 250, QSizePolicy.Minimum, QSizePolicy.Minimum))

        back_button = QPushButton("Torna indietro")
        back_button.clicked.connect(self.show_back_click)
        v_layout.addWidget(back_button)

        self.setLayout(v_layout)
        self.setWindowTitle(statistica.nome)

    #Metodo che consente di visualizzare la lista dei prodotti di cui si è calcolato statistica
    def update_ui_prod(self, lista_ordinata, indice):
        self.listview_model = QStandardItemModel(self.list_view)
        for (index, (codice, valore)) in enumerate(lista_ordinata):
            marca = self.controller_prod.get_marca_prodotto_by_code(codice)
            nome = self.controller_prod.get_nome_prodotto_by_code(codice)
            item = QStandardItem()
            if indice == 0 or indice == 1:
                item.setText(str(index + 1) + ") Cod. Prodotto: " + str(codice) + "      Marca: " + str(marca)
                             + "      Nome: " + str(nome) + "      Quantità vendute: " + str(valore))
            elif indice == 2:
                item.setText(str(index + 1) + ") Cod. Prodotto: " + str(codice) + "      Marca: " + str(marca)
                             + "      Nome: " + str(nome) + "      Guadagno: " + str(valore) + " €")

            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    #Metodo che in base alla statistica scelta mostra una vista differente
    def smistatore_viste(self, smistatore):
        if smistatore == 0:
            self.update_ui_prod(self.controller_stat.ordinamento_decrescente(self.controller_stat.costruzione_dizionario()), smistatore)
        elif smistatore == 1:
            self.update_ui_prod(self.controller_stat.ordinamento_crescente(self.controller_stat.costruzione_dizionario()), smistatore)
        elif smistatore == 2:
            self.update_ui_prod(self.controller_stat.ordinamento_decrescente(self.controller_stat.prod_piu_redditizi()), smistatore)
        elif smistatore == 3:
            pass
        elif smistatore == 4:
            pass
        elif smistatore == 5:
            pass

    # Metodo che consente di tornare alla shermata precedente
    def show_back_click(self):
        self.vista_back = listastatistiche.view.VistaListaStatistiche.VistaListaStatistiche()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()
