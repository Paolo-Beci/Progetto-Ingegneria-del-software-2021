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
                self.lista_del_personale = pickle.load(f)

    def filtra_prodotti(self):
        pass

    def inserisci_utente(self, utente):
        self.lista_del_personale.append(utente)
        print("ciao")

    def get_lista_del_personale(self):
        return self.lista_del_personale

    def save_data(self):
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'wb') as handle:
            pickle.dump(self.lista_del_personale, handle, pickle.HIGHEST_PROTOCOL)

    def aggiungi_utente_da_database(self, utente):
        self.lista_del_personale.append(utente)
