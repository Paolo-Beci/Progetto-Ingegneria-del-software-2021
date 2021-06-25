import sys, time
from datetime import datetime

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QWidget, QListView, QMessageBox
from PyQt5 import QtCore

from listastatistiche.controller.ControllerListaStatistiche import ControllerListaStatistiche
from statistica.view.VistaStatistica import VistaStatistica


class VistaListaStatistiche(QWidget):
    def __init__(self, parent=None):
        super(VistaListaStatistiche, self).__init__(parent)
        self.controller = ControllerListaStatistiche()

        #################################################
        '''
           Costruzione parte statica dell'interfaccia  
        '''
        self.setObjectName("Form")
        self.setEnabled(True)
        self.resize(1046, 676)
        self.setStyleSheet("background-color: white;")
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setMinimumSize(QtCore.QSize(200, 0))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.png')
        self.label_logo.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_logo, 0, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.prod_button = QtWidgets.QPushButton(self)
        self.prod_button.setObjectName("prod_button")
        self.prod_button.clicked.connect(self.filter_prodotti)
        self.gridLayout_3.addWidget(self.prod_button, 0, 0, 1, 1)
        self.prod_button.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.combo = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo.sizePolicy().hasHeightForWidth())
        self.combo.setSizePolicy(sizePolicy)
        self.combo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.combo.setIconSize(QtCore.QSize(25, 16))
        self.combo.setObjectName("combo")
        self.combo.addItem("")
        self.combo.addItem("")
        self.gridLayout_3.addWidget(self.combo, 0, 5, 1, 1)
        self.combo.setStyleSheet("QComboBox {\n"
                                 "   background-color:rgb(26, 108, 218);\n"
                                 "   border-width: 2px;\n"
                                 "   font: 12px;\n"
                                 "   padding: 3px;\n"
                                 "   color: white;\n"
                                 "}")

        self.forn_button = QtWidgets.QPushButton(self)
        self.forn_button.setObjectName("forn_button")
        self.forn_button.clicked.connect(self.filter_fornitori)
        self.gridLayout_3.addWidget(self.forn_button, 0, 1, 1, 1)
        self.forn_button.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")

        self.anno_line = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anno_line.sizePolicy().hasHeightForWidth())
        self.anno_line.setSizePolicy(sizePolicy)
        self.anno_line.setMaximumSize(QtCore.QSize(100, 16777215))
        self.anno_line.setObjectName("anno_line")
        self.anno_line.setPlaceholderText("Inserisci l'anno da filtrare")
        self.anno_line.returnPressed.connect(self.filter_button_click)
        self.gridLayout_3.addWidget(self.anno_line, 0, 6, 1, 1)
        self.anno_line.setStyleSheet("QLineEdit {\n"
                                 "   border-width: 2px;\n"
                                 "   border-radius: 10px;\n"
                                 "   border: 2px solid gray;\n"
                                 "   font: 12px;\n"
                                 "   padding: 6px;\n"
                                 "min-width: 170px;\n"
                                 "}")
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        self.listview_model.setObjectName("listItems")
        self.filter_all()
        self.list_view.setModel(self.listview_model)
        self.gridLayout_3.addWidget(self.list_view, 1, 0, 1, 7)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 2)

        self.all_button = QtWidgets.QPushButton(self)
        self.all_button.setObjectName("all_button")
        self.all_button.clicked.connect(self.filter_all)
        self.gridLayout_3.addWidget(self.all_button, 0, 2, 1, 1)
        self.all_button.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 5)

        self.back_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setObjectName("back_button")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_home.png'))
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(50, 50))
        self.back_button.clicked.connect(self.close)
        self.gridLayout.addWidget(self.back_button, 0, 0, 1, 1)
        self.back_button.setStyleSheet("QPushButton {\n"
                                    "   background-color:white;\n"
                                    "   border-width: 2px;\n"
                                    "   border-radius: 10px;\n"
                                    "   padding: 6px;\n"
                                    "}")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.open_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())

        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName("open_button")
        self.open_button.clicked.connect(self.filter_button_click)
        self.gridLayout_4.addWidget(self.open_button, 0, 1, 1, 1)
        self.open_button.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 15px;\n""   padding: 6px;\n""   color: white;\n""}")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # imposto il testo degli oggetti dell'interfaccia
        self.setWindowTitle(_translate("Form", "Area Statistiche"))
        self.forn_button.setText(_translate("Form", "Fornitori"))
        self.prod_button.setText(_translate("Form", "Prodotti"))
        self.all_button.setText(_translate("Form", "All"))
        self.combo.setItemText(0, _translate("Form", "Primavera/Estate"))
        self.combo.setItemText(1, _translate("Form", "Autunno/Inverno"))
        self.open_button.setText(_translate("Form", "Apri"))

    # Metodo che consente di visualizzare la statistica selezionato
    def show_statistica(self, anno, stagione):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            statistica_selezionata = self.controller.get_statistica_by_index(selected)
            print("QUI"+sys.executable)
            self.vista_statistica = VistaStatistica(statistica_selezionata, selected, anno, stagione)
            self.vista_statistica.show()

    # Metodo che consente di visualizare la lista di tutte le statistiche
    def filter_all(self):
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
    def filter_prodotti(self):
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
    def filter_fornitori(self):
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
        try:
            if anno == "":
                anno = datetime.today().year
            if int(anno) and 2050 > int(anno) > 1950:
                if self.combo.currentIndex() == 0:
                    self.show_statistica(str(anno), "P/E")
                elif self.combo.currentIndex() == 1:
                    self.show_statistica(str(anno), "A/I")
            else:
                self.popup_error_data()
        except:
            self.popup_error_formato_data()

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
