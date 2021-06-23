import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from fornitore.controller.ControllerFornitore import ControllerFornitore
from fornitore.view.VistaModificaFornitore import VistaModificaFornitore

class VistaFornitore(QWidget):
    def __init__(self, fornitore, update_ui, controller, lista_dinamica, parent=None):
        super(VistaFornitore, self).__init__(parent)
        self.controller_fornitore= ControllerFornitore(fornitore)
        self.controller_lista_fornitori= controller
        self.update_ui= update_ui
        self.fornitore_selezionato= fornitore
        self.lista_dinamica = lista_dinamica

        # boolean che permette di eseguire due eventi diversi in caso di chiusura della finestra
        self.end1 = False

        ###################################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        #Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
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
        btn_modifica.clicked.connect(self.show_modifica_fornitore)
        #li aggiungo al widget
        self.v_layout.addWidget(btn_elimina)
        btn_elimina.setStyleSheet("QPushButton {\n"
                                              "   background-color: red;\n"
                                              "   border-width: 2px;\n"
                                              "   border-radius: 10px;\n"
                                              "   font: bold 12px;\n"
                                              "   padding: 6px;\n"
                                              "   color: white;\n"
                                              "}")
        self.v_layout.addWidget(btn_modifica)
        btn_modifica.setStyleSheet("QPushButton {\n"
                                               "   background-color: rgb(26, 108, 218);\n"
                                               "   border-width: 2px;\n"
                                               "   border-radius: 10px;\n"
                                               "   font: bold 12px;\n"
                                               "   padding: 6px;\n"
                                               "   color: white;\n"
                                               "}")
        self.setLayout(self.v_layout)
        self.setWindowTitle("Fornitore")

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def update_ui_fornitore(self):
        self.label_nome.setText(self.controller_fornitore.get_nome())
        self.label_indirizzo.setText("Indirizzo: {}".format(self.controller_fornitore.get_indirizzo()))
        self.label_partita_iva.setText("Partita iva: {}".format(self.controller_fornitore.get_partita_iva()))
        self.label_telefono.setText("Telefono: {}".format(self.controller_fornitore.get_telefono()))
        self.label_sito_web.setText("Sito Web: {}".format(self.controller_fornitore.get_sito_web()))
        self.label_rappresentante.setText("Rappresentante: {}".format(self.controller_fornitore.get_rappresentante()))
        self.label_data_affiliazione.setText("Data affiliazione: {}".format(self.controller_fornitore.get_data_affiliazione()))
        self.label_codice.setText("Codice fornitore: {}".format(self.controller_fornitore.get_cod_fornitore()))
        self.label_stato.setText("Stato: {}".format(self.controller_fornitore.get_stato()))
        self.update_ui()

    def elimina_fornitore_click(self):
        self.end1 = True
        #chiude la finestra corrente
        self.close()
        self.end1 = False

    def show_modifica_fornitore(self):
        self.vista_modifica_fornitore= VistaModificaFornitore(self.fornitore_selezionato, self.controller_fornitore, self.controller_lista_fornitori, self.update_ui_fornitore)
        self.vista_modifica_fornitore.show()
        self.update_ui()

    def closeEvent(self, event):
        if self.end1==True:
            reply = QMessageBox.question(self, 'Eliminare?',
                                         "Sicuro di voler eliminare l'utente selezionato?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if not type(event) == bool:   #SI
                    event.accept()
                    self.controller_lista_fornitori.elimina_fornitore_by_codice(self.controller_fornitore.get_cod_fornitore(), self.lista_dinamica)
                    self.update_ui()
                else:
                    sys.exit()
            else:
                if not type(event) == bool:    #NO
                    event.ignore()