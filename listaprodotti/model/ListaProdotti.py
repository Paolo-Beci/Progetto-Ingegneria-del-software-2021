import json
import os.path
import pickle

from prodotto.model.Prodotto import Prodotto



class ListaProdotti:

    def __init__(self):
        super(ListaProdotti, self).__init__()
        self.lista_prodotti = []
        if os.path.isfile('listaprodotti/data/lista_prodotti_salvata.pickle'):
            with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'rb') as f:
                self.lista_prodotti = pickle.load(f)
        else:
            with open('listaprodotti/data/database_prodotti.json') as f:
                lista_prodotti_json = json.load(f)
                for prodotto_da_caricare in lista_prodotti_json:
                    self.aggiungi_prodotto_da_database(
                        Prodotto(prodotto_da_caricare["cod_fattura"], prodotto_da_caricare["cod_fornitore"],
                                 prodotto_da_caricare["data_ordine"], prodotto_da_caricare["cod_prodotto"],
                                 prodotto_da_caricare["materiale"], prodotto_da_caricare["colore"],
                                 prodotto_da_caricare["taglia"], prodotto_da_caricare["quantita"],
                                 prodotto_da_caricare["prezzo_acquisto"], prodotto_da_caricare["prezzo_vendita"],
                                 prodotto_da_caricare["stagione"], prodotto_da_caricare["stato"],
                                 prodotto_da_caricare["data_vendita"], prodotto_da_caricare["sconto_consigliato"],
                                 prodotto_da_caricare["sconto"], prodotto_da_caricare["cod_immagine"]))

    def filtra_prodotti(self):
        pass

    def aggiungi_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)

    def get_lista_prodotti(self):
        return self.lista_prodotti

    def get_prodotto(self, cod):
        return self.lista_prodotti[cod]

    def aggiungi_prodotto_da_database(self, prodotto):
        self.lista_prodotti.append(prodotto)

    def save_data(self):
        with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)