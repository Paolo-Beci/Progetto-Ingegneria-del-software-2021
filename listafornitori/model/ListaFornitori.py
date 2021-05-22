import json
import os
import pickle

from fornitore.model.Fornitore import Fornitore


class ListaFornitori:

    def __init__(self):
        super(ListaFornitori, self).__init__()
        self.lista_fornitori = []
        if os.path.isfile('listafornitori/data/DatabaseFornitori.pickle'):
            with open('listafornitori/data/DatabaseFornitori.pickle', 'rb') as f:
                try:
                    self.lista_fornitori= pickle.load(f)
                except EOFError:
                    return None

        # else:
        #     with open('listafornitori/data/DatabaseFornitori.json') as f:
        #         lista_fornitori_json = json.load(f)
        #         for fornitore_da_caricare in lista_fornitori_json:
        #             self.aggiungi_fornitore_da_database(
        #                 Fornitore(fornitore_da_caricare["nome"], fornitore_da_caricare["indirizzo"],
        #                          fornitore_da_caricare["partita_iva"], fornitore_da_caricare["telefono"],
        #                          fornitore_da_caricare["email"], fornitore_da_caricare["rappresentante"],
        #                          fornitore_da_caricare["data_affiliazione"], fornitore_da_caricare["codice_fornitore"],
        #                          fornitore_da_caricare["stato"]))

    def inserisci_fornitore(self, fornitore):
        self.lista_fornitori.append(fornitore)

    def filtra_fornitori(self):
        return None

    def get_lista_fornitori(self):
        return self.lista_fornitori

    def elimina_fornitore_by_codice(self, codice_fornitore):
        def is_selected_fornitore(fornitore):
            if fornitore.codice_fornitore == codice_fornitore:
                return True
            return False
        self.lista_fornitori.remove(list(filter(is_selected_fornitore, self.lista_fornitori))[0])

    def get_fornitore_by_index(self, index):
        return self.lista_fornitori[index]

    def save_data(self):
        with open('listafornitori/data/DatabaseFornitori.pickle', 'wb') as handle:
            pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)

    # def aggiungi_fornitore_da_database(self, fornitore):
    #     self.lista_fornitori.append(fornitore)