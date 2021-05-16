from PyQt5.QtWidgets import QWidget

from fornitore.controller import ControllerFornitore


class VistaFornitore(QWidget):
    def __init__(self, elimina_fornitore, update_ui, parent=None):
        super(VistaFornitore, self).__init__(parent)
        self.controller= ControllerFornitore
        self.elimina_fornitore= elimina_fornitore
        self.update_ui= update_ui