import time, os

import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidgetItem, QMessageBox

from fornitore.model.Fornitore import Fornitore
from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.model.Prodotto import Prodotto
from statistica.contorller.ControllerStatistica import ControllerStatistica
import listastatistiche.view.VistaListaStatistiche


class VistaStatistica(QWidget):
    def __init__(self, statistica, selected, anno, stagione, parent=None):
        super(VistaStatistica, self).__init__(parent)
        self.selected = selected
        self.anno = anno
        self.stagione = stagione
        self.controller_stat = ControllerStatistica(statistica)
        self.controller_prod = ControllerListaProdotti()
        self.controller_forn = ControllerListaFornitori()

        self.setGeometry(200, 150, 400, 0)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.v_layout = QVBoxLayout()

        if self.controller_stat.get_quantita() is not None and self.anno != "":
            label_nome = QLabel(
                "TOP " + str(self.controller_stat.get_quantita()) + ": " + self.controller_stat.get_nome()
                + " - " + str(self.convertitore_stagione()) + " " + str(self.anno))
            label_nome.setAlignment(QtCore.Qt.AlignCenter)
        elif self.controller_stat.get_quantita() is not None:
            label_nome = QLabel(
                "TOP " + str(self.controller_stat.get_quantita()) + ": " + self.controller_stat.get_nome()
                + " - " + str(self.convertitore_stagione()))
            label_nome.setAlignment(QtCore.Qt.AlignCenter)
        else:
            label_nome = QLabel(self.controller_stat.get_nome() + ": " + str(self.convertitore_stagione()) + " " + str(self.anno))
            label_nome.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        self.v_layout.addWidget(label_nome)

        self.smistatore_viste()

        self.setLayout(self.v_layout)
        self.setWindowTitle(statistica.nome)


    # Metodo che consente di visualizzare la lista degli elementi passata con ulteriori informazioni
    def update_ui_stat(self, lista_ordinata):
        self._translate = QtCore.QCoreApplication.translate

        if not lista_ordinata:
            self.nessun_elem = QLabel()
            self.nessun_elem.setText("Nessun dato disponibile...")
            font = self.nessun_elem.font()
            font.setPointSize(18)
            self.nessun_elem.setFont(font)
            self.setGeometry(100, 150, 0, 0)
            self.v_layout.addWidget(self.nessun_elem)
        else:
            self.tableWidget = QtWidgets.QTableWidget(self)
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(4)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, item)
            self.setFixedWidth(1010)
            self.v_layout.addWidget(self.tableWidget)

            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText(self._translate("Form", "Codice"))

            if self.selected == 0:
                self.tableWidget.setColumnWidth(0, 240)
                self.tableWidget.setColumnWidth(1, 240)
                self.tableWidget.setColumnWidth(2, 240)
                self.tableWidget.setColumnWidth(3, 240)
                self.creazione_ct("Marca", "Nome", "Quantità vendute")
            elif self.selected == 1:
                self.tableWidget.setColumnWidth(0, 240)
                self.tableWidget.setColumnWidth(1, 240)
                self.tableWidget.setColumnWidth(2, 240)
                self.tableWidget.setColumnWidth(3, 240)
                self.creazione_ct("Marca", "Nome", "Quantità vendute")
            elif self.selected == 2:
                self.tableWidget.setColumnWidth(0, 240)
                self.tableWidget.setColumnWidth(1, 240)
                self.tableWidget.setColumnWidth(2, 240)
                self.tableWidget.setColumnWidth(3, 240)
                self.creazione_ct("Marca", "Nome", "Guadagno (in €)")
            elif self.selected == 3:
                self.tableWidget.setColumnWidth(0, 240)
                self.tableWidget.setColumnWidth(1, 240)
                self.tableWidget.setColumnWidth(2, 240)
                self.tableWidget.setColumnWidth(3, 242)
                self.creazione_ct("Nome", "Stato", "Importo totale (in €)")
            elif self.selected == 4:
                self.tableWidget.setColumnWidth(0, 290)
                self.tableWidget.setColumnWidth(1, 290)
                self.tableWidget.setColumnWidth(2, 290)
                self.tableWidget.setColumnWidth(3, 290)
                self.setFixedWidth(1200)
                self.setGeometry(100, 150, 0, 0)
                self.creazione_ct("Nome", "Stato", "Calzature totali")
            elif self.selected == 5:
                self.tableWidget.setColumnWidth(0, 290)
                self.tableWidget.setColumnWidth(1, 290)
                self.tableWidget.setColumnWidth(2, 290)
                self.tableWidget.setColumnWidth(3, 290)
                self.setFixedWidth(1200)
                self.setGeometry(100, 150, 0, 0)
                self.creazione_ct("Nome", "Stato", "Giorni di ritardo")

            row = 0
            self.tableWidget.setRowCount(len(lista_ordinata))
            for (codice, valore) in lista_ordinata:
                if self.selected == 0 or self.selected == 1 or self.selected == 2:
                    self.tableWidget.setMinimumHeight(330)
                    self.setFixedHeight(400)
                    prodotto = self.controller_prod.get_prodotto_by_code(codice)
                    self.tableWidget.setColumnCount(4)
                    self.riempimento_tabella(prodotto, codice, str(valore), row)
                elif self.selected == 3 or self.selected == 4 or self.selected == 5:
                    self.tableWidget.setMinimumHeight(120)
                    self.setFixedHeight(190)
                    fornitore = self.controller_forn.get_fornitore_by_code(codice)
                    self.tableWidget.setColumnCount(4)
                    self.riempimento_tabella(fornitore, codice, str(valore), row)
                row += 1

    #Metodo dedicato alla creazione delle colonne della tabella
    def creazione_ct(self, nome1, nome2, nome3):
        self.item = self.tableWidget.horizontalHeaderItem(1)
        self.item.setText(self._translate("Form", nome1))
        self.item = self.tableWidget.horizontalHeaderItem(2)
        self.item.setText(self._translate("Form", nome2))
        self.item = self.tableWidget.horizontalHeaderItem(3)
        self.item.setText(self._translate("Form", nome3))

    #Metodo dedicato al riempimento della tabella
    def riempimento_tabella(self, oggetto, codice, valore, row):
        if isinstance(oggetto, Prodotto):
            nome = self.controller_prod.get_nome_prodotto_by_code(codice)

            self.item = QTableWidgetItem(oggetto.cod_prodotto)
            self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(oggetto.marca))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(nome))
            self.item = QTableWidgetItem(valore)
            self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(self.item))


        elif isinstance(oggetto, Fornitore):
            stato = self.controller_forn.get_stato_fornitore_by_code(codice)

            self.item = QTableWidgetItem(oggetto.cod_fornitore)
            self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(oggetto.nome))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(stato))
            self.item = QTableWidgetItem(valore)
            self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(self.item))


    #Metodo dedicato alla creazione del grafico contenente l'andamento finanziario
    def update_ui_af(self, dizionario_af):
        plt.rcParams['figure.figsize'] = [12, 4.5]
        colors = ["red", "blue", "orange", "green"]
        print(dizionario_af)
        index = np.arange(len(dizionario_af.keys()))
        plt.bar(index, dizionario_af.values(), color=colors)
        plt.xticks(index, dizionario_af.keys(), size=10)
        #plt.show()

        plt.savefig("listastatistiche/data/grafico.png")

    #Metodo che consente la visualizzazione dell'andamento finanziario
    def andamento_finanziario(self, dizionario_af):
        cont = 0
        for valore in dizionario_af.values():
            if valore == 0:
                cont += 1
        if cont == 4:
             self.nessun_elem = QLabel()
             self.nessun_elem.setText("Nessun dato disponibile...")
             font = self.nessun_elem.font()
             font.setPointSize(18)
             self.nessun_elem.setFont(font)
             self.v_layout.addWidget(self.nessun_elem)
        else:
            self.setGeometry(125, 100, 0, 0)
            self.setFixedWidth(1100)
            self.setFixedHeight(500)
            self.update_ui_af(dizionario_af)
            self.immagine = QtWidgets.QLabel()
            self.immagine.setObjectName("immagine")
            self.immagine.setAlignment(QtCore.Qt.AlignCenter)
            pixmap = QPixmap("listastatistiche/data/grafico.png")
            self.immagine.setPixmap(pixmap)
            self.v_layout.addWidget(self.immagine)
            #os.remove("listastatistiche/data/grafico.png")

    # Metodo che in base alla statistica scelta mostra una vista differente
    def smistatore_viste(self):
        if self.selected == 0:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 1:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 2:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 3:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 4:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 5:
            self.update_ui_stat(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))
        elif self.selected == 6:
            self.andamento_finanziario(self.controller_stat.smistatore_statistica(self.selected, self.anno, self.stagione))

    # Metodo che consente di tornare alla shermata precedente
    def show_back_click(self):
        self.vista_back = listastatistiche.view.VistaListaStatistiche.VistaListaStatistiche()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()

    # Metodo che ritorna il nome della stagione competo
    def convertitore_stagione(self):
        if self.stagione == "P/E":
            return "Primavera/Estate"
        elif self.stagione == "A/I":
            return "Autunno/Inverno"

