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
        else:
            with open('listadelpersonale/data/DatabaseDelPersonale.json') as f:
                lista_del_personale_json= json.load(f)
                for utente_da_caricare in lista_del_personale_json:
                    self.lista_del_personale.append(Utente(utente_da_caricare["cod_utente"],
                                                           utente_da_caricare["nome"],
                                                           utente_da_caricare["cognome"],
                                                           utente_da_caricare["data_nascita"],
                                                           utente_da_caricare["luogo_nascita"],
                                                           utente_da_caricare["cod_fiscale"],
                                                           utente_da_caricare["inizio_lavoro"],
                                                           utente_da_caricare["scad_contratto"],
                                                           utente_da_caricare["ruolo"],
                                                           utente_da_caricare["indirizzo_residenza"],
                                                           utente_da_caricare["n_telefonico"],
                                                           utente_da_caricare["stipendio"],
                                                           utente_da_caricare["username"],
                                                           utente_da_caricare["password"]))

    def filtra_utenti(self):
        pass

    def inserisci_utente(self, utente):
        self.lista_del_personale.append(utente)

    def get_lista_del_personale(self):
        return self.lista_del_personale

    def elimina_utente_by_codice(self, codice_utente):
        def is_selected_utente(utente):
            if utente.cod_utente == codice_utente:
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
