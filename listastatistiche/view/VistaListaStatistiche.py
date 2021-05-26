import time
import home.view.VistaHome
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listastatistiche.controller.ControllerListaStatistiche import ControllerListaStatistiche
from statistica.view.VistaStatistica import VistaStatistica


class VistaListaStatistiche(QWidget):
    def __init__(self, parent=None):
        super(VistaListaStatistiche, self).__init__(parent)
        self.controller = ControllerListaStatistiche()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for statistica in self.controller.get_lista_statistiche():
            item = QStandardItem()
            item.setText(statistica.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")

        open_button.clicked.connect(self.show_statistica)


        buttons_layout.addWidget(open_button)
        home_button = QPushButton("Torna alla HOME")
        home_button.clicked.connect(self.show_home)
        buttons_layout.addWidget(home_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Statistiche')

    #Metodo che consente di visualizzare la statistica selezionata
    def show_statistica(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            statistica_selezionata = self.controller.get_statistica_by_index(selected)
            self.vista_statistica = VistaStatistica(statistica_selezionata, selected)
            self.vista_statistica.showMaximized()
            time.sleep(0.3)
            self.close()

    #Metodo che consente di tornare alla schermata home
    def show_home(self):
        self.vista_home = home.view.VistaHome.VistaHome()
        self.vista_home.showMaximized()
        time.sleep(0.3)
        self.close()

    #Metodo che consente di effettuare il salvataggio al termine di un evento
    def closeEvent(self, event):
        self.controller.save_data()
