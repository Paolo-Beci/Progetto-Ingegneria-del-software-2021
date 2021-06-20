import json
import os
import pickle

from fornitore.model.Fornitore import Fornitore


class ListaFornitori:
    def __init__(self):
        super(ListaFornitori, self).__init__()
        self.lista_fornitori = []
        self.refresh_data()

    def inserisci_fornitore(self, fornitore):
        self.lista_fornitori.append(fornitore)

    def get_lista_fornitori(self):
        return self.lista_fornitori

    def elimina_fornitore_by_codice(self, codice_fornitore, lista_dinamica):
        for fornitore in self.lista_fornitori:
            if fornitore.cod_fornitore == codice_fornitore:
                self.lista_fornitori.remove(fornitore)
                lista_dinamica.remove(fornitore)

    # Giuseppe
    def get_fornitore_by_code(self, codice):
        for fornitore in self.lista_fornitori:
            if fornitore.cod_fornitore == codice:
                return fornitore

    # Giuseppe
    def get_stato_fornitore_by_code(self, codice):
        for fornitore in self.lista_fornitori:
            if fornitore.cod_fornitore == codice and fornitore.stato == 'P':
                return "Premium"
            elif fornitore.cod_fornitore == codice and fornitore.stato == 'S':
                return "Standard"

    # Metodo: ricarica in lista i dati da file pickle, se esistente e non vuoto, o dal file json
    def refresh_data(self):
        if os.path.isfile('listafornitori/data/DatabaseFornitori.pickle') and os.stat('listafornitori/data/DatabaseFornitori.pickle').st_size != 0:
            with open('listafornitori/data/DatabaseFornitori.pickle', 'rb') as f:
                try:
                    self.lista_fornitori = pickle.load(f)
                except EOFError:
                    return
        else:
             with open('listafornitori/data/DatabaseFornitori.json') as f:
                 lista_fornitori_json = json.load(f)
                 for fornitore_da_caricare in lista_fornitori_json:
                     self.lista_fornitori.append(
                         Fornitore(fornitore_da_caricare["cod_fornitore"], fornitore_da_caricare["nome"],
                                   fornitore_da_caricare["indirizzo"], fornitore_da_caricare["telefono"],
                                   fornitore_da_caricare["partita_iva"], fornitore_da_caricare["sito_web"],
                                   fornitore_da_caricare["rappresentante"], fornitore_da_caricare["data_affiliazione"],
                                   fornitore_da_caricare["stato"]))

    # Metodo: salva il contenuto della lista su file pickle
    def save_data(self):
        with open('listafornitori/data/DatabaseFornitori.pickle', 'wb') as handle:
            pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)