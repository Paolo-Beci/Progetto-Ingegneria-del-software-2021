from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QComboBox, QLabel, QStyleFactory, QApplication, QCheckBox, QHBoxLayout, QGridLayout, \
    QGroupBox, QWidget, QHBoxLayout, QDateEdit, QDateTimeEdit, QPushButton

"""
    MODIFICA DEI PARAMETRI DEL PRODOTTO
    prende in input un prodotto e ne permette di modificare i campi (visualizzandone i vecchi?)
"""


class VistaModificaProdotto(QWidget):
    def __init__(self, controller, update_ui, parent=None):
        super(VistaModificaProdotto, self).__init__(parent)
        self.controller = controller
        self.update_ui = update_ui

        self.originalPalette = QApplication.palette()

        styleLabel = QLabel("Modifica il prodotto:")

        # inizializzazione blocchi interfaccia
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftGroupBox()
        self.createBottomRightGroupBox()

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)

        # posizionamento interfaccia
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        btn_salva = QPushButton("Salva")
        btn_salva.clicked.connect(self.salva_modifiche_click)
        btn_salva.addWidget(btn_salva)

        self.setWindowTitle("Modifica prodotto")

    # CREAZIONE DEI COMPONENTI
    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("CODICI PRODOTTO E DETTAGLI ORDINE")

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("IMMAGINE")

        # INSERIMENTO IMMAGINE
        label = QLabel(self)
        pixmap = QPixmap('listaprodotti/data/images/immagine_prova.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        label.move(1000, 50)
        self.show()

    def createBottomLeftGroupBox(self):
        self.bottomLeftGroupBox = QGroupBox("DESCRIZIONE PRODOTTO")
        dateTimeEdit = QDateEdit(self.bottomLeftGroupBox)
        dateTimeEdit.setDate(QDate.currentDate())

        layout = QGridLayout()
        layout.addWidget(dateTimeEdit, 0, 0, 1, 2)
        layout.setRowStretch(5, 1)
        self.bottomLeftGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("STATO E SCONTI APPLICABLI")

    def salva_modifiche_click(self):
        campo1 = self.lineEdit_9.text()
        self.controller.set_nome_fornitore(campo1)
        self.update_ui()
        self.close()
