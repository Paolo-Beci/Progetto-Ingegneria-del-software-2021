import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from utente.controller.ControllerUtente import ControllerUtente
from utente.view.VistaModificaUtente import VistaModificaUtente


class VistaUtente(QWidget):
    def __init__(self, utente, elimina_utente_by_codice, update_ui, controller, lista_dinamica, parent=None):
        super(VistaUtente, self).__init__(parent)
        self.utente_selezionato= utente
        self.controller= ControllerUtente(utente)


        self.controller_lista= controller
        self.elimina_utente_by_codice= elimina_utente_by_codice
        self.update_ui= update_ui
        self.lista_dinamica= lista_dinamica

        self.end1 = False
        # istanzio un vertical layout
        self.v_layout = QVBoxLayout()
        # istanzio due Label, una per il nome e una per il body (gli altri campi)
        self.label_nome_cognome = QLabel()
        self.label_data_nascita = QLabel()
        self.label_luogo_nascita = QLabel()
        self.label_cf = QLabel()
        self.label_codice = QLabel()
        self.label_telefono = QLabel()
        self.label_indirizzo= QLabel()
        self.label_ruolo = QLabel()
        self.label_stipendio = QLabel()
        self.label_data_inizio_contratto = QLabel()
        self.label_data_scadenza_contratto = QLabel()
        # chiamo le parti dinamiche, cioè che si modificano: update_ui per aggiornare la lista fornitori e update_ui_fornitore per aggiornare i campi
        self.update_ui()
        self.update_ui_utente()
        # imposto un carattere più grande al nome
        font_nome_cognome = self.label_nome_cognome.font()
        font_nome_cognome.setPointSize(30)
        self.label_nome_cognome.setFont(font_nome_cognome)

        # imposto un carattere minore per il body (i campi)
        font_data_nascita = self.label_data_nascita.font()
        font_data_nascita.setPointSize(15)
        self.label_data_nascita.setFont(font_data_nascita)

        font_luogo_nascita = self.label_luogo_nascita.font()
        font_luogo_nascita.setPointSize(15)
        self.label_luogo_nascita.setFont(font_luogo_nascita)

        font_cf = self.label_cf.font()
        font_cf.setPointSize(15)
        self.label_cf.setFont(font_cf)

        font_codice = self.label_codice.font()
        font_codice.setPointSize(15)
        self.label_codice.setFont(font_codice)

        font_telefono = self.label_telefono.font()
        font_telefono.setPointSize(15)
        self.label_telefono.setFont(font_telefono)

        font_indirizzo = self.label_indirizzo.font()
        font_indirizzo.setPointSize(15)
        self.label_indirizzo.setFont(font_indirizzo)

        font_ruolo = self.label_ruolo.font()
        font_ruolo.setPointSize(15)
        self.label_ruolo.setFont(font_ruolo)

        font_stipendio = self.label_stipendio.font()
        font_stipendio.setPointSize(15)
        self.label_stipendio.setFont(font_stipendio)

        font_data_inizio_contratto = self.label_data_inizio_contratto.font()
        font_data_inizio_contratto.setPointSize(15)
        self.label_data_inizio_contratto.setFont(font_data_inizio_contratto)

        font_data_scadenza_contratto = self.label_data_scadenza_contratto.font()
        font_data_scadenza_contratto.setPointSize(15)
        self.label_data_scadenza_contratto.setFont(font_data_scadenza_contratto)

        # aggiungo il nome al widget, cioè al mio contenitore
        self.v_layout.addWidget(self.label_nome_cognome)
        # aggiungo i campi del body al widget
        self.v_layout.addWidget(self.label_data_nascita)
        self.v_layout.addWidget(self.label_luogo_nascita)
        self.v_layout.addWidget(self.label_cf)
        self.v_layout.addWidget(self.label_codice)
        self.v_layout.addWidget(self.label_indirizzo)
        self.v_layout.addWidget(self.label_telefono)
        self.v_layout.addWidget(self.label_ruolo)
        self.v_layout.addWidget(self.label_stipendio)
        self.v_layout.addWidget(self.label_data_inizio_contratto)
        self.v_layout.addWidget(self.label_data_scadenza_contratto)

        # creo i bottoni elimina e modifica
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_utente_click)
        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_utente_click)
        # li aggiungo al widget
        self.v_layout.addWidget(btn_elimina)
        self.v_layout.addWidget(btn_modifica)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Utente")

    def update_ui_utente(self):
        self.label_nome_cognome.setText(self.controller.get_nome()+" "+self.controller.get_cognome())
        self.label_data_nascita.setText("Data nascita: {}".format(self.controller.get_data_nascita()))
        self.label_luogo_nascita.setText("Luogo nascita: {}".format(self.controller.get_luogo_nascita()))
        self.label_cf.setText("Codice fiscale: {}".format(self.controller.get_cf()))
        self.label_codice.setText("Codice: {}".format(self.controller.get_cod_utente()))
        self.label_indirizzo.setText("Indirizzo: {}".format(self.controller.get_indirizzo()))
        self.label_telefono.setText("Telefono: {}".format(self.controller.get_telefono()))
        self.label_ruolo.setText("Ruolo: {}".format(self.controller.get_ruolo()))
        self.label_stipendio.setText("Stipendio: {}".format(self.controller.get_stipendio()))
        self.label_data_inizio_contratto.setText("Data inizio contratto: {}".format(self.controller.get_data_inizio_contratto()))
        self.label_data_scadenza_contratto.setText("Data scadenza contratto: {}".format(self.controller.get_data_scadenza_contratto()))
        self.update_ui()

    def elimina_utente_click(self):
        self.end1 = True
        #self.elimina_utente_by_codice(self.controller.get_cod_utente())
        #self.update_ui()
        # chiude la finestra corrente
        self.close()
        self.end1 = False

    def modifica_utente_click(self):
        self.vista_modifica_utente = VistaModificaUtente(self.utente_selezionato,self.controller, self.controller_lista, self.update_ui_utente)
        self.vista_modifica_utente.show()
        self.update_ui()

    def closeEvent(self, event):
        if self.end1==True:
            reply = QMessageBox.question(self, 'Eliminare?',
                                         "Sicuro di voler eliminare l'utente selezionato?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if not type(event) == bool:   #SI
                    event.accept()
                    self.elimina_utente_by_codice(self.controller.get_cod_utente(), self.lista_dinamica)
                    self.update_ui()
                else:
                    sys.exit()
            else:
                if not type(event) == bool:    #NO
                    event.ignore()