import time
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from ordine.controller.ControllerOrdine import ControllerOrdine
from ordine.model import Ordine


class VistaOrdine(QWidget):
    def __init__(self, ordine, elimina_ordine_by_codice, update_ui, controller, lista_dinamica, parent=None):
        super(VistaOrdine, self).__init__(parent)
        self.ordine_selezionato = ordine
        self.controller = ControllerOrdine(ordine)
        self.controller_lista= controller
        self.elimina_ordine_by_codice = elimina_ordine_by_codice
        self.update_ui = update_ui
        self.lista_dinamica= lista_dinamica

        #######################################
        self.setObjectName("Form")
        self.resize(1091, 545)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 2, 2, 9, 3)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 11, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 5)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle("Visualizza ordine")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice prodotto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Marca"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tipo"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Genere"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Taglia"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Prezzo d\'acquisto"))
        self.label_5.setText(_translate("Form", "Data ordine:"))
        self.label_8.setText(_translate("Form", "Importo totale:"))
        self.pushButton.setText(_translate("Form", "Modifica"))
        self.pushButton_2.setText(_translate("Form", "Elimina"))
        self.label_2.setText(_translate("Form", "Stato:"))
        self.label_10.setText(_translate("Form", "Lista prodotti ordine:"))
        self.label.setText(_translate("Form", "Codice fattura:"))
        self.pushButton_3.setText(_translate("Form", "Apri"))
        self.label_6.setText(_translate("Form", "Data arrivo prevista:"))
        self.label_9.setText(_translate("Form", "Calzature totali:"))
        self.label_3.setText(_translate("Form", "Stagione:"))
        self.label_7.setText(_translate("Form", "Data arrivo effettiva:"))
        self.label_4.setText(_translate("Form", "Codice fornitore:"))
        self.label_11.setText(_translate("Form", "Dati ordine:"))

        #######################################

        # v_layout = QVBoxLayout()
        #
        # label_nome = QLabel(str(self.controller.get_cod_fattura()) + " " + str(self.controller.get_data_ordine()))
        # font_nome = label_nome.font()
        # font_nome.setPointSize(30)
        # label_nome.setFont(font_nome)
        # v_layout.addWidget(label_nome)
        #
        # v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        #
        # # LOAD IMMAGINE
        # #label = QLabel(self)
        # #pixmap = QPixmap('listaprodotti/data/images/immagine_prova.jpg')
        # #label.setPixmap(pixmap)
        # #self.resize(pixmap.width(), pixmap.height())
        #
        # #self.photo = QtWidgets.QLabel(self.centralwidget)
        # #self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        # #self.photo.setText("")
        # #self.photo.setPixmap(QtGui.QPixmap("cat.jpg"))
        # #self.photo.setScaledContents(True)
        # #self.photo.setObjectName("photo")
        #
        # v_layout.addWidget(self.get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        # v_layout.addWidget(self.get_info("Codice fornitore: {}".format(self.controller.get_cod_fornitore())))
        # v_layout.addWidget(self.get_info("Data ordine: {}".format(self.controller.get_data_ordine())))
        # v_layout.addWidget(self.get_info("data arrivo prevista: {}".format(self.controller.get_data())))
        # v_layout.addWidget(self.get_info("data arrivo effettiva: {}".format(self.controller.get_data())))
        # v_layout.addWidget(self.get_info("importo totale : {}".format(self.controller.get_importo_totale())))
        # v_layout.addWidget(self.get_info("Stagione: {}".format(self.controller.get_stagione())))
        # v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))
        # v_layout.addWidget(self.get_info("calzature_totali: {}".format(self.controller.get_())))
        #
        # v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        #
        # btn_elimina = QPushButton("Elimina")
        # btn_elimina.clicked.connect(self.elimina_ordine_click)
        # v_layout.addWidget(btn_elimina)
        #
        # btn_modifica = QPushButton("Modifica")
        # btn_modifica.clicked.connect(self.modifica_prodotto_click)
        # v_layout.addWidget(btn_modifica)
        #
        # btn_back = QPushButton("Torna indietro")
        # btn_back.clicked.connect(self.show_back_click)
        # v_layout.addWidget(btn_back)
        #
        #
        # self.setLayout(v_layout)
        # self.setWindowTitle(self.controller.get_cod_fornitore())

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
        self.elimina_ordine_by_codice(self.controller.get_cod_fattura())
        self.update_ui()
        self.close()

    def modifica_ordine_click(self):
        self.showMaximized(Ordine.view.VistaModificaOrdine.VistaModificaOrdine(self.controller.get_cod_fattura()))
        self.update_ui()
        self.close()

    def show_back_click(self, listaOrdine=None):
        self.vista_back = listaOrdine.view.VistaListaOrdine.VistaListaOrdini()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()
