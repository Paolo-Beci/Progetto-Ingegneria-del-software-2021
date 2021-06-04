import time

import home.view.VistaHome
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QFormLayout, \
    QComboBox, QMessageBox

from listastatistiche.controller.ControllerListaStatistiche import ControllerListaStatistiche
from statistica.view.VistaStatistica import VistaStatistica


class VistaListaStatistiche(QWidget):
    def __init__(self, parent=None):
        super(VistaListaStatistiche, self).__init__(parent)
        self.controller = ControllerListaStatistiche()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)

        self.show_lista_stat()

        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.filter_button_click)
        buttons_layout.addWidget(open_button)

        home_button = QPushButton("Torna alla HOME")
        home_button.clicked.connect(self.show_home)
        buttons_layout.addWidget(home_button)

        lista_stat_button = QPushButton("Prodotti e Fornitori")
        lista_stat_button.clicked.connect(self.show_lista_stat)
        buttons_layout.addWidget(lista_stat_button)

        prod_button = QPushButton("Prodotti")
        prod_button.clicked.connect(self.show_prodotti)
        buttons_layout.addWidget(prod_button)

        forn_button = QPushButton("Fornitori")
        forn_button.clicked.connect(self.show_fornitori)
        buttons_layout.addWidget(forn_button)

        self.combo = QComboBox(self)
        self.combo.addItems(["Primavera/Estate", "Autunno/Inverno"])
        buttons_layout.addWidget(self.combo)

        self.anno_button = QLineEdit()
        self.anno_button.setObjectName("Bottone")
        self.anno_button.setPlaceholderText("Inserisci l'anno da filtrare")
        buttons_layout.addWidget(self.anno_button)

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Statistiche')

    # Metodo che consente di visualizzare la statistica selezionato
    def show_statistica(self, anno, stagione):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            statistica_selezionata = self.controller.get_statistica_by_index(selected)
            self.vista_statistica = VistaStatistica(statistica_selezionata, selected, anno, stagione)
            self.vista_statistica.showMaximized()
            time.sleep(0.3)
            self.close()

    # Metodo che consente di tornare alla schermata home
    def show_home(self):
        self.vista_home = home.view.VistaHome.VistaHome()
        self.vista_home.showMaximized()
        time.sleep(0.3)
        self.close()

    # Metodo che consente di visualizare la lista di tutte le statistiche
    def show_lista_stat(self):
        self.listview_model.clear()
        for statistica in self.controller.get_lista_statistiche():
            self.item = QStandardItem()
            self.item.setText(statistica.nome)
            self.item.setEditable(False)
            font = self.item.font()
            font.setPointSize(18)
            self.item.setFont(font)
            self.listview_model.appendRow(self.item)

    # Metodo che consente di visualizzare la lista delle statistiche dei soli prodotti
    def show_prodotti(self):
        self.listview_model.clear()
        for statistica in self.controller.get_lista_statistiche()[:3]:
            self.item = QStandardItem()
            self.item.setText(statistica.nome)
            self.item.setEditable(False)
            font = self.item.font()
            font.setPointSize(18)
            self.item.setFont(font)
            self.listview_model.appendRow(self.item)

    # Metodo che consente di visualizzare la lista delle statistiche dei soli fornitori
    def show_fornitori(self):
        self.listview_model.clear()
        for statistica in self.controller.get_lista_statistiche()[3:6]:
            self.item = QStandardItem()
            self.item.setText(statistica.nome)
            self.item.setEditable(False)
            font = self.item.font()
            font.setPointSize(18)
            self.item.setFont(font)
            self.listview_model.appendRow(self.item)

    # Metodo per avviare il filtraggio, dopo aver cliccato il bottone "Filtra"
    def filter_button_click(self):
        try:
            if self.anno_button.text() == "" or (int(self.anno_button.text()) and 2050 > int(self.anno_button.text()) > 1950):
                anno = str(self.anno_button.text())
                if self.combo.currentIndex() == 0:
                    self.show_statistica(anno, "P/E")
                elif self.combo.currentIndex() == 1:
                    self.show_statistica(anno, "A/I")
            else:
                self.popup_error_data()
        except:
            self.popup_error_formato_data()

    # Metodo che informa l'utente dell'errato inserimento dell'anno. Viene lanciato quando l'utente inseisce una stringa.
    def popup_error_formato_data(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Hai inserito l'anno in modo errato!!! \n Per favore inseriscilo correttamente nella seguente forma YYYY.")
        msg.setIcon(QMessageBox.Warning)
        time.sleep(0.3)
        msg.exec_()

    # Metodo che informa l'utente dell'errato inserimento dell'anno. Viene lanciato quando l'utente inseisce una stringa.
    def popup_error_data(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Hai inserito un anno non consentito!!!")
        msg.setIcon(QMessageBox.Warning)
        time.sleep(0.3)
        msg.exec_()

    # Metodo che consente di effettuare il salvataggio al termine di un evento
    def closeEvent(self, event):
        self.controller.save_data()
