from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QListView

from statistica.contorller.ControllerStatistica import ControllerStatistica


class VistaStatistica(QWidget):
    def __init__(self, statistica, selected, parent=None):
        super(VistaStatistica, self).__init__(parent)
        self.controller = ControllerStatistica(statistica)

        self.controller.smistatore(selected)

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label_nome = QLabel("TOP " + str(self.controller.get_quantita()) + ": " + self.controller.get_nome())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        h_layout.addLayout(v_layout)
        self.setLayout(h_layout)
        self.setWindowTitle(statistica.nome)



        '''
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in self.controller.get_contenuto():
            item = QStandardItem()
            item.setText(prodotto.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)
        '''