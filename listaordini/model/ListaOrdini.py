import json
import os.path
import pickle

from ordine.model.Ordine import Ordine


class ListaOrdini:

    def __init__(self):
        super(ListaOrdini, self).__init__()
        self.lista_ordini = []
        if os.path.isfile('listaordini/data/DatabaseOrdini.pickle'):
            with open('listaordini/data/DatabaseOrdini.pickle', 'rb') as f:
                try:
                    self.lista_ordini = pickle.load(f)
                except EOFError:
                    return None
        # else:
        #     with open('listaordini/data/DatabaseOrdini.json') as f:
        #         lista_ordine_json = json.load(f)
        #         for ordine_da_caricare in lista_ordine_json:
        #             self.aggiungi_prodotti_da_database(
        #                 ordine(ordine_da_caricare["cod_fattura"], ordine_da_caricare["cod_fornitore"],
        #                          ordine_da_caricare["data_ordine"], ordine_da_caricare["stato"],
        #                          ordine_da_caricare["stagione"], ordine_da_caricare["data_arrivo_prevista"]))

    def filtra_ordine(self, cod_fattura):
        return self.lista_ordini[cod_fattura]

    def aggiungi_ordine(self, ordine):
        self.lista_ordini.append(ordine)

    def get_lista_ordini(self):
        return self.lista_ordini

    def save_data(self):
        with open('listaordini/data/lista_ordine_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)