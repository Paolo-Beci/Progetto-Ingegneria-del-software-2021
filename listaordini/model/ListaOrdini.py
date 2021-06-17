import json
import os.path
import pickle

from ordine.model.Ordine import Ordine


class ListaOrdini:

    def __init__(self):
        super(ListaOrdini, self).__init__()
        self.lista_ordini = []
        self.refresh_data()

    def filtra_ordine(self, cod_fattura):
        return self.lista_ordini[cod_fattura]

    def aggiungi_ordine(self, ordine):
        self.lista_ordini.append(ordine)

    def get_lista_ordini(self):
        return self.lista_ordini

    def get_ordine_by_index(self, index):
        return self.lista_ordini[index]

    def refresh_data(self):
        if os.path.isfile('listaordini/data/DatabaseOrdini.pickle') and os.stat('listaordini/data/DatabaseOrdini.pickle').st_size!=0:
            with open('listaordini/data/DatabaseOrdini.pickle', 'rb') as f:
                try:
                    self.lista_ordini = pickle.load(f)
                except EOFError:
                    return
        else:
            with open('listaordini/data/DatabaseOrdini.json') as f:
                lista_ordine_json = json.load(f)
                for ordine_da_caricare in lista_ordine_json:
                    self.lista_ordini.append(Ordine(ordine_da_caricare["cod_fattura"], ordine_da_caricare["cod_fornitore"],
                                 ordine_da_caricare["stagione"], ordine_da_caricare["stato"],
                                 ordine_da_caricare["data_ordine"], ordine_da_caricare["data_arrivo_prevista"],
                                 ordine_da_caricare["data_arrivo_effettiva"], ordine_da_caricare["importo_totale"],
                                 ordine_da_caricare["calzature_totali"]))

    def save_data(self):
        with open('listaordini/data/DatabaseOrdini.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

    def elimina_ordine_by_codice(self, codice_ordine, lista_dinamica):
        for ordine in self.lista_ordini:
            if ordine.cod_fattura == codice_ordine:
                self.lista_ordini.remove(ordine)
                lista_dinamica.remove(ordine)
