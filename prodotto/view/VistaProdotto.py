import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QHBoxLayout, \
    QGridLayout, QGroupBox, QLineEdit, QDateEdit, QMessageBox, QApplication
from PyQt5.QtGui import QIcon, QPixmap, QPainter

from prodotto.view.VistaModificaProdotto import VistaModificaProdotto
from prodotto.controller.ControllerProdotto import ControllerProdotto
import listaprodotti.view.VistaListaProdotti

"""
    VISUALIZZAZIONE DEI PARAMETRI DEL PRODOTTO
    Da fare: UI
"""


class VistaProdotto(QWidget):
    def __init__(self, c_prodotto, elimina_prodotto, update_ui, parent=None):
        super(VistaProdotto, self).__init__(parent)
        self.controller = ControllerProdotto(c_prodotto)
        self.elimina_prodotto = elimina_prodotto
        # self.modifica_prodotto = modifica_prodotto    serve???
        self.update_ui = update_ui
        self.setObjectName("MainWindow")
        self.resize(1173, 700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_dettagli_prodotto = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_dettagli_prodotto.setObjectName("groupBox_dettagli_prodotto")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_dettagli_prodotto)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_data_ordine = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_data_ordine.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_ordine.setObjectName("label_data_ordine")
        self.gridLayout_3.addWidget(self.label_data_ordine, 0, 0, 1, 1)
        self.label_marca = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.label_marca.setObjectName("label_marca")
        self.gridLayout_3.addWidget(self.label_marca, 0, 1, 1, 1)
        self.label_nome = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout_3.addWidget(self.label_nome, 1, 0, 1, 1)
        self.label_tipo = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_tipo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipo.setObjectName("label_tipo")
        self.gridLayout_3.addWidget(self.label_tipo, 1, 1, 1, 1)
        self.label_genere = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_genere.setAlignment(QtCore.Qt.AlignCenter)
        self.label_genere.setObjectName("label_genere")
        self.gridLayout_3.addWidget(self.label_genere, 2, 0, 1, 1)
        self.label_materiale = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_materiale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_materiale.setObjectName("label_materiale")
        self.gridLayout_3.addWidget(self.label_materiale, 2, 1, 1, 1)
        self.label_colore = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_colore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_colore.setObjectName("label_colore")
        self.gridLayout_3.addWidget(self.label_colore, 3, 0, 1, 1)
        self.label_taglia = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_taglia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_taglia.setObjectName("label_taglia")
        self.gridLayout_3.addWidget(self.label_taglia, 3, 1, 1, 1)
        self.label_quantita = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_quantita.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quantita.setObjectName("label_quantita")
        self.gridLayout_3.addWidget(self.label_quantita, 4, 0, 1, 1)
        self.label_stagione = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_stagione.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stagione.setObjectName("label_stagione")
        self.gridLayout_3.addWidget(self.label_stagione, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_dettagli_prodotto, 2, 1, 2, 2)
        self.pushButton_annulla = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_annulla.setObjectName("pushButton_annulla")
        self.gridLayout.addWidget(self.pushButton_annulla, 5, 2, 1, 1)
        self.pushButton_indietro = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.gridLayout.addWidget(self.pushButton_indietro, 0, 0, 1, 1)
        self.groupBox_prezzi_sconti = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_prezzi_sconti.setObjectName("groupBox_prezzi_sconti")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_prezzi_sconti)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_prezzo_acquisto = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_prezzo_acquisto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prezzo_acquisto.setObjectName("label_prezzo_acquisto")
        self.gridLayout_4.addWidget(self.label_prezzo_acquisto, 0, 0, 1, 1)
        self.label_prezzo_vendita = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_prezzo_vendita.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.gridLayout_4.addWidget(self.label_prezzo_vendita, 0, 1, 1, 1)
        self.label_sconto = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_sconto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sconto.setObjectName("label_sconto")
        self.gridLayout_4.addWidget(self.label_sconto, 1, 0, 1, 1)
        self.label_sconto_consigliato = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_sconto_consigliato.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sconto_consigliato.setObjectName("label_sconto_consigliato")
        self.gridLayout_4.addWidget(self.label_sconto_consigliato, 1, 1, 1, 1)
        self.label_stato = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_stato.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stato.setObjectName("label_stato")
        self.gridLayout_4.addWidget(self.label_stato, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_prezzi_sconti, 4, 1, 1, 2)
        self.pushButton_elimina = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_elimina.setObjectName("pushButton_elimina")
        self.gridLayout.addWidget(self.pushButton_elimina, 5, 1, 1, 1)
        self.groupBox_codici_prodotto = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_codici_prodotto.setObjectName("groupBox_codici_prodotto")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_codici_prodotto)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_cod_fattura = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_fattura.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_fattura.setObjectName("label_cod_fattura")
        self.gridLayout_2.addWidget(self.label_cod_fattura, 0, 0, 1, 1)
        self.label_cod_fornitore = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_fornitore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_fornitore.setObjectName("label_cod_fornitore")
        self.gridLayout_2.addWidget(self.label_cod_fornitore, 0, 1, 1, 1)
        self.label_cod_ordine = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_ordine.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_ordine.setObjectName("label_cod_ordine")
        self.gridLayout_2.addWidget(self.label_cod_ordine, 1, 0, 1, 1)
        self.label_cod_prodotto = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_prodotto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_prodotto.setObjectName("label_cod_prodotto")
        self.gridLayout_2.addWidget(self.label_cod_prodotto, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_codici_prodotto, 1, 1, 1, 2)
        self.immagine = QtWidgets.QWidget(self.widget_2)
        self.immagine.setObjectName("immagine")
        self.gridLayout.addWidget(self.immagine, 1, 0, 4, 1)
        self.verticalLayout.addWidget(self.widget_2)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_dettagli_prodotto.setTitle(_translate("MainWindow", "Dettagli prodotto"))
        self.label_data_ordine.setText(_translate("MainWindow", "Data dell\'ordine: " + str(self.controller.get_data_ordine())))
        self.label_marca.setText(_translate("MainWindow", "Marca: " + str(self.controller.get_marca())))
        self.label_nome.setText(_translate("MainWindow", "Nome: " + str(self.controller.get_nome())))
        self.label_tipo.setText(_translate("MainWindow", "Tipo: " + str(self.controller.get_tipo())))
        self.label_genere.setText(_translate("MainWindow", "Genere: " + str(self.controller.get_genere())))
        self.label_materiale.setText(_translate("MainWindow", "Materiale: " + str(self.controller.get_materiale())))
        self.label_colore.setText(_translate("MainWindow", "Colore: " + str(self.controller.get_colore())))
        self.label_taglia.setText(_translate("MainWindow", "Taglia/e: " + str(self.controller.get_taglia())))
        self.label_quantita.setText(_translate("MainWindow", "Quantità: " + str(self.controller.get_quantita())))
        self.label_stagione.setText(_translate("MainWindow", "Stagione:"))
        self.pushButton_annulla.setText(_translate("MainWindow", "Modifica"))
        self.pushButton_indietro.setText(_translate("MainWindow", "< Indietro"))
        self.groupBox_prezzi_sconti.setTitle(_translate("MainWindow", "Prezzi e sconti"))
        self.label_prezzo_acquisto.setText(_translate("MainWindow", "Prezzo di acquisto:"))
        self.label_prezzo_vendita.setText(_translate("MainWindow", "Prezzo di vendita:"))
        self.label_sconto.setText(_translate("MainWindow", "Sconto:"))
        self.label_sconto_consigliato.setText(_translate("MainWindow", "Sconto cosigliato:"))
        self.label_stato.setText(_translate("MainWindow", "Stato:"))
        self.pushButton_elimina.setText(_translate("MainWindow", "Elimina"))
        self.groupBox_codici_prodotto.setTitle(_translate("MainWindow", "Codici prodotto"))
        self.label_cod_fattura.setText(_translate("MainWindow", "Codice fattura:"))
        self.label_cod_fornitore.setText(_translate("MainWindow", "Codice fornitore:"))
        self.label_cod_ordine.setText(_translate("MainWindow", "Codice ordine:"))
        self.label_cod_prodotto.setText(_translate("MainWindow", "Codice prodotto:"))

    """
        Eventi trigger click dei bottoni
    """

    def popup_elimina(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Sei sicuro di voler eliminare il prodotto selezionato? \n\nil prodotto eliminato non sarà ripristinabile")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()
        msg.buttonClicked.connect(self.elimina_prodotto_click)

    def elimina_prodotto_click(self):
        self.elimina_prodotto_by_codice(self.controller.get_cod_prodotto())
        self.update_ui()
        self.close()

    def modifica_prodotto_click(self):
        self.vista_modifica_prodotto = VistaModificaProdotto(self.controller, self.update_ui)
        self.vista_modifica_prodotto.show()
        # self.update_ui()

    def show_back_click(self):
        self.vista_back = listaprodotti.view.VistaListaProdotti.VistaListaProdotti()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()
