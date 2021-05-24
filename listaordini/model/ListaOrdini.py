import json
import os.path
import pickle

from ordine.model.Ordine import Ordine


class ListaOrdini:

    def __init__(self):
        super(ListaOrdini, self).__init__()
        self.Lista_ordine = []
        if os.path.isfile('listaordini/data/lista_ordine_salvata.pickle'):
            with open('listaordini/data/lista_ordine_salvata.pickle', 'rb') as f:
                self.lista_ordine = pickle.load(f)
        else:
            with open('listaordini/data/database_ordine.json') as f:
                lista_ordine_json = json.load(f)
                for ordine_da_caricare in lista_ordine_json:
                    self.aggiungi_prodotti_da_database(
                        ordine(ordine_da_caricare["cod_fattura"], ordine_da_caricare["cod_fornitore"],
                                 ordine_da_caricare["data_ordine"], ordine_da_caricare["stato"],
                                 ordine_da_caricare["stagione"], ordine_da_caricare["data_arrivo_prevista"]))

    def filtra_ordine(self,cod_fattura):
        return self.lista_ordine[cod_fattura]

    def aggiungi_ordine(self, ordine):
        self.lista_ordine.append(ordine)

    def get_lista_ordine(self):
        return self.lista_ordine



    def save_data(self):
        with open('listaordini/data/lista_ordine_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordine, handle, pickle.HIGHEST_PROTOCOL)