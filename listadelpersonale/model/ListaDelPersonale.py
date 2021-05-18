import json
import os
import pickle

from utente.model.Utente import Utente


class ListaDelPersonale:

    def __init__(self):
        super(ListaDelPersonale, self).__init__()
        self.lista_del_personale = []
        if os.path.isfile('listadelpersonale/data/DatabaseDelPersonale.pickle'):
            with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'rb') as f:
                try:
                    self.lista_del_personale = pickle.load(f)
                except EOFError:
                    return None


    def filtra_utenti(self):
        pass

    def inserisci_utente(self, utente):
        self.lista_del_personale.append(utente)

    def get_lista_del_personale(self):
        return self.lista_del_personale

    def elimina_utente_by_codice(self, codice_utente):
        def is_selected_utente(utente):
            if utente.codice_utente == codice_utente:
                return True
            return False
        self.lista_del_personale.remove(list(filter(is_selected_utente, self.lista_del_personale))[0])

    def get_utente_by_index(self, index):
        return self.lista_del_personale[index]

    def save_data(self):
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'wb') as handle:
            pickle.dump(self.lista_del_personale, handle, pickle.HIGHEST_PROTOCOL)

    # def aggiungi_utente_da_database(self, utente):
    #   self.lista_del_personale.append(utente)
