from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, \
    QPushButton

from fornitore.controller.ControllerFornitore import ControllerFornitore
from fornitore.view.VistaModificaFornitore import VistaModificaFornitore

#serve un update_ui
class VistaFornitore(QWidget):
    def __init__(self, fornitore, elimina_fornitore_by_codice, update_ui, parent=None):
        super(VistaFornitore, self).__init__(parent)
        self.controller= ControllerFornitore(fornitore)
        self.elimina_fornitore_by_codice= elimina_fornitore_by_codice
        self.update_ui= update_ui

        self.v_layout = QVBoxLayout()

        #istanzio due Label, una per il nome e una per il body (gli altri campi)
        self.label_nome = QLabel()
        self.label_body = QLabel()
        #chiamo le parti dinamiche, cioè che si modificano: update_ui per aggiornare la lista fornitori e update_ui_fornitore per aggiornare i campi
        self.update_ui()
        self.update_ui_fornitore()

        #imposto un font più grande per il nome
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)
        #aggiungo il nome al widget, cioè al mio contenitore
        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #imposto un carattere minore per il body (i campi)
        self.v_layout.addWidget(self.label_body)
        font_body= self.label_body.font()
        font_body.setPointSize(15)
        self.label_body.setFont(font_body)
        #aggiungo il body al widget
        self.v_layout.addWidget(self.label_body)
        #inserisco uno spazio nel widget
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        #creo i bottoni elimina e modifica
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_fornitore_click)
        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_fornitore_click)
        #li aggiungo al widget
        self.v_layout.addWidget(btn_elimina)
        self.v_layout.addWidget(btn_modifica)

        self.setLayout(self.v_layout)

    def update_ui_fornitore(self):
        self.label_nome.setText(self.controller.get_nome())
        self.label_body.setText("Indirizzo: {}".format(self.controller.get_indirizzo())+"\n"+
                                "Partita iva: {}".format(self.controller.get_partita_iva())+"\n"+
                                "Telefono: {}".format(self.controller.get_telefono())+"\n"+
                                "Email: {}".format(self.controller.get_email())+"\n"+
                                "Rappresentante: {}".format(self.controller.get_rappresentante())+"\n"+
                                "Data affiliazione: {}".format(self.controller.get_data_affiliazione())+"\n"+
                                "Codice fornitore: {}".format(self.controller.get_codice_fornitore())+"\n"+
                                "Stato: {}".format(self.controller.get_stato()))

    def elimina_fornitore_click(self):
        self.elimina_fornitore_by_codice(self.controller.get_codice_fornitore())
        self.update_ui()
        #chiude la finestra corrente
        self.close()

    def modifica_fornitore_click(self):
        self.vista_modifica_fornitore= VistaModificaFornitore(self.controller, self.update_ui_fornitore)
        self.vista_modifica_fornitore.show()
        self.update_ui()