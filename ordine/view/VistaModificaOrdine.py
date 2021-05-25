from PyQt5.QtWidgets import QComboBox, QLabel, QStyleFactory, QApplication, QCheckBox, QHBoxLayout, QGridLayout, \
    QGroupBox, QWidget, QHBoxLayout


# prende in input un prodotto e ne permette di modificare i campi visualizzando i vecchi
class VistaModificaOrdine(QWidget):
    def __init__(self, cod_prodotto, parent=None):
        super(VistaModificaOrdine, self).__init__(parent)
        self.cod_prodotto = cod_prodotto

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        #self.createProgressBar()

        styleComboBox.activated[str].connect(self.changeStyle)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Modifica ordine")
        self.changeStyle('Windows')

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QGroupBox("Group 3")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 4")
