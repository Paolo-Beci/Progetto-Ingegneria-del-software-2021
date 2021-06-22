from datetime import datetime
import time
from tkinter.tix import Form

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QMessageBox
from PyQt5 import QtCore

from listastatistiche.controller.ControllerListaStatistiche import ControllerListaStatistiche
from statistica.view.VistaStatistica import VistaStatistica


class VistaListaStatistiche(QWidget):
    def __init__(self, parent=None):
        super(VistaListaStatistiche, self).__init__(parent)
        self.controller = ControllerListaStatistiche()

        #################################################
        '''COSTRUZIONE INTERFACCIA'''
        self.setObjectName("Form")
        self.setEnabled(True)
        self.resize(701, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        # Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.forn_button = QtWidgets.QPushButton(self)
        self.forn_button.setObjectName("forn_button")
        self.forn_button.clicked.connect(self.show_fornitori)
        self.gridLayout_3.addWidget(self.forn_button, 0, 2, 1, 1)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout_3.addItem(spacerItem, 1, 11, 1, 1)

        self.anno_line = QtWidgets.QLineEdit(self)
        self.anno_line.setMaximumSize(QtCore.QSize(150, 16777215))
        self.anno_line.setObjectName("anno_line")
        self.anno_line.setPlaceholderText("Inserisci l'anno da filtrare")
        self.anno_line.returnPressed.connect(self.filter_button_click)
        self.gridLayout_3.addWidget(self.anno_line, 0, 10, 1, 1)

        self.prod_button = QtWidgets.QPushButton(self)
        self.prod_button.setObjectName("prod_button")
        self.prod_button.clicked.connect(self.show_prodotti)
        self.gridLayout_3.addWidget(self.prod_button, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 0, 11, 1, 1)

        self.af_button = QtWidgets.QPushButton(self)
        self.af_button.setObjectName("af_button")
        self.af_button.clicked.connect(self.show_statistica)
        self.gridLayout_3.addWidget(self.af_button, 0, 3, 1, 1)

        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        self.listview_model.setObjectName("listItems")
        self.show_lista_stat()
        self.list_view.setModel(self.listview_model)
        self.gridLayout_3.addWidget(self.list_view, 1, 1, 1, 10)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 4, 1, 5)
        # spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)

        self.combo = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo.sizePolicy().hasHeightForWidth())
        self.combo.setSizePolicy(sizePolicy)
        self.combo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.combo.setIconSize(QtCore.QSize(25, 16))
        self.combo.setObjectName("Stagione")
        self.combo.addItems(["", ""])
        self.gridLayout_3.addWidget(self.combo, 0, 9, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 2, 11, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 2, 0, 1, 1)

        self.open_button = QtWidgets.QPushButton(self)
        self.open_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.open_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.open_button.setIconSize(QtCore.QSize(16, 16))
        self.open_button.setObjectName("open_button")
        self.open_button.clicked.connect(self.filter_button_click)
        self.gridLayout_3.addWidget(self.open_button, 2, 4, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(550, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 8, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 2, 1, 1, 3)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 3, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(425, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setMinimumSize(QtCore.QSize(200, 0))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.png')
        self.label_logo.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_logo, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 0, 1, 5)

        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.close)
        self.gridLayout.addWidget(self.back_button, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.back_button.setMaximumWidth(100)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # imposto il testo degli oggetti dell'interfaccia
        self.setWindowTitle(_translate("Form", "Area Statistiche"))
        self.forn_button.setText(_translate("Form", "Fornitori"))
        self.prod_button.setText(_translate("Form", "Prodotti"))
        self.af_button.setText(_translate("Form", "Andamento Finanziario"))
        self.combo.setItemText(0, _translate("Form", "Primavera/Estate"))
        self.combo.setItemText(1, _translate("Form", "Autunno/Inverno"))
        self.open_button.setText(_translate("Form", "Apri"))
        self.back_button.setText(_translate("Form", "<- Indietro"))

    # Metodo che consente di visualizzare la statistica selezionato
    def show_statistica(self, anno, stagione):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            statistica_selezionata = self.controller.get_statistica_by_index(selected)
            self.vista_statistica = VistaStatistica(statistica_selezionata, selected, anno, stagione)
            self.vista_statistica.show()

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
        anno = self.anno_line.text()
        #try:
        if anno == "":
            anno = datetime.today().year
        if int(anno) and 2050 > int(anno) > 1950:
            if self.combo.currentIndex() == 0:
                self.show_statistica(str(anno), "P/E")
            elif self.combo.currentIndex() == 1:
                self.show_statistica(str(anno), "A/I")
        else:
            self.popup_error_data()
        #except:
            #self.popup_error_formato_data()

    # Metodo che informa l'utente dell'errato inserimento dell'anno. Viene lanciato quando l'utente inseisce una stringa.
    def popup_error_formato_data(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Hai inserito l'anno in modo errato!!! \n Per favore inseriscilo correttamente nel seguente formato YYYY.")
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
        pass
        #self.controller.save_data()
