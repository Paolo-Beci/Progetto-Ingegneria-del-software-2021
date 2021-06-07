from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from fornitore.controller.ControllerFornitore import ControllerFornitore
from fornitore.view.VistaModificaFornitore import VistaModificaFornitore

class VistaFornitore(QWidget):
    def __init__(self, fornitore, elimina_fornitore_by_codice, update_ui, controller,parent=None):
        super(VistaFornitore, self).__init__(parent)
        self.controller= ControllerFornitore(fornitore)
        self.controller_lista= controller
        self.elimina_fornitore_by_codice= elimina_fornitore_by_codice
        self.update_ui= update_ui

        #istanzio un vertical layout
        self.v_layout = QVBoxLayout()
        #istanzio due Label, una per il nome e una per il body (gli altri campi)
        self.label_nome= QLabel()
        self.label_indirizzo= QLabel()
        self.label_partita_iva= QLabel()
        self.label_telefono= QLabel()
        self.label_sito_web= QLabel()
        self.label_rappresentante= QLabel()
        self.label_data_affiliazione= QLabel()
        self.label_codice= QLabel()
        self.label_stato= QLabel()
        # chiamo le parti dinamiche, cioè che si modificano: update_ui per aggiornare la lista fornitori e update_ui_fornitore per aggiornare i campi
        self.update_ui()
        self.update_ui_fornitore()
        #imposto un carattere più grande al nome
        font_nome= self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)

        #imposto un carattere minore per il body (i campi)
        font_indirizzo= self.label_indirizzo.font()
        font_indirizzo.setPointSize(15)
        self.label_indirizzo.setFont(font_indirizzo)

        font_partita_iva = self.label_partita_iva.font()
        font_partita_iva.setPointSize(15)
        self.label_partita_iva.setFont(font_partita_iva)

        font_telefono = self.label_telefono.font()
        font_telefono.setPointSize(15)
        self.label_telefono.setFont(font_telefono)

        font_sito_web = self.label_sito_web.font()
        font_sito_web.setPointSize(15)
        self.label_sito_web.setFont(font_sito_web)

        font_rappresentante = self.label_rappresentante.font()
        font_rappresentante.setPointSize(15)
        self.label_rappresentante.setFont(font_rappresentante)

        font_data_affiliazione = self.label_data_affiliazione.font()
        font_data_affiliazione.setPointSize(15)
        self.label_data_affiliazione.setFont(font_data_affiliazione)

        font_codice = self.label_codice.font()
        font_codice.setPointSize(15)
        self.label_codice.setFont(font_codice)

        font_stato = self.label_stato.font()
        font_stato.setPointSize(15)
        self.label_stato.setFont(font_stato)

        #aggiungo il nome al widget, cioè al mio contenitore
        self.v_layout.addWidget(self.label_nome)
        #aggiungo i campi del body al widget
        self.v_layout.addWidget(self.label_indirizzo)
        self.v_layout.addWidget(self.label_partita_iva)
        self.v_layout.addWidget(self.label_telefono)
        self.v_layout.addWidget(self.label_sito_web)
        self.v_layout.addWidget(self.label_rappresentante)
        self.v_layout.addWidget(self.label_data_affiliazione)
        self.v_layout.addWidget(self.label_codice)
        self.v_layout.addWidget(self.label_stato)

        #creo i bottoni elimina e modifica
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_fornitore_click)
        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_fornitore_click)
        #li aggiungo al widget
        self.v_layout.addWidget(btn_elimina)
        self.v_layout.addWidget(btn_modifica)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Fornitore")

    def update_ui_fornitore(self):
        self.label_nome.setText(self.controller.get_nome())
        self.label_indirizzo.setText("Indirizzo: {}".format(self.controller.get_indirizzo()))
        self.label_partita_iva.setText("Partita iva: {}".format(self.controller.get_partita_iva()))
        self.label_telefono.setText("Telefono: {}".format(self.controller.get_telefono()))
        self.label_sito_web.setText("Sito Web: {}".format(self.controller.get_sito_web()))
        self.label_rappresentante.setText("Rappresentante: {}".format(self.controller.get_rappresentante()))
        self.label_data_affiliazione.setText("Data affiliazione: {}".format(self.controller.get_data_affiliazione()))
        self.label_codice.setText("Codice fornitore: {}".format(self.controller.get_cod_fornitore()))
        self.label_stato.setText("Stato: {}".format(self.controller.get_stato()))
        self.update_ui()

    def elimina_fornitore_click(self):
        self.elimina_fornitore_by_codice(self.controller.get_cod_fornitore())
        self.update_ui()
        #chiude la finestra corrente
        self.close()

    def modifica_fornitore_click(self):
        self.vista_modifica_fornitore= VistaModificaFornitore(self.controller, self.controller_lista, self.update_ui_fornitore)
        self.vista_modifica_fornitore.show()
        self.update_ui()