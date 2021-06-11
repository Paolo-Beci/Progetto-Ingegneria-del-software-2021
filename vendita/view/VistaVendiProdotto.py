from PyQt5.QtWidgets import QWidget

from prodotto.controller.ControllerProdotto import ControllerProdotto


class VistaVendiProdotto(QWidget):
    def __init__(self, prodotto, parent=None):
        super(VistaVendiProdotto, self).__init__(parent)
        self.controller = ControllerProdotto(prodotto)

        self.controller.set_venduto()

