import json
import os.path
import pickle

from prodotto.model.Prodotto import Prodotto

"""
    CARICAMENTO E GESTIONE DEI DATI CHE RIGUARDANO I PRODOTTI
"""


class ListaProdotti:

    def __init__(self):
        super(ListaProdotti, self).__init__()
        self.lista_prodotti = []
        self.lista_marche = []
        self.refresh_data()

    def inserisci_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)
        self.save_data()

    def get_lista_prodotti(self):
        return self.lista_prodotti

    def get_lista_marche(self):
        for prodotto in self.lista_prodotti:
            if prodotto.marca in self.lista_marche:
                pass
            else:
                self.lista_marche.append(prodotto.marca)
        return self.lista_marche

    def get_dimensione_lista(self):
        return len(self.lista_prodotti)

    def get_prodotto_by_code(self, code):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == code:
                return prodotto

    # Giuseppe
    def get_nome_prodotto_by_code(self, codice):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == codice and prodotto.nome is not None:
                return prodotto.nome
            elif prodotto.cod_prodotto == codice and prodotto.nome is None:
                return "Nessun nome"

    def elimina_prodotto(self, codice_prodotto, lista_prodotti_filtrata):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == codice_prodotto:
                self.lista_prodotti.remove(prodotto)
        for prodotto in lista_prodotti_filtrata:
            if prodotto.cod_prodotto == codice_prodotto:
                lista_prodotti_filtrata.remove(prodotto)

    # Metodo: ricarica in lista i dati da file pickle, se esistente e non vuoto, o dal file json
    def refresh_data(self):
        if os.path.isfile('listaprodotti/data/DatabaseProdotti.pickle') and os.stat('listaprodotti/data/DatabaseProdotti.pickle').st_size!=0:
            with open('listaprodotti/data/DatabaseProdotti.pickle', 'rb') as f:
                try:
                    self.lista_prodotti = pickle.load(f)
                except EOFError:
                    return
        else:
            with open('listaprodotti/data/DatabaseProdotti.json') as f:
                lista_prodotti_json = json.load(f)
                for prodotto_da_caricare in lista_prodotti_json:
                    self.lista_prodotti.append(
                        Prodotto(prodotto_da_caricare["cod_fattura"], prodotto_da_caricare["cod_fornitore"],
                                 prodotto_da_caricare["data_ordine"], prodotto_da_caricare["cod_prodotto"],
                                 prodotto_da_caricare["marca"], prodotto_da_caricare["nome"],
                                 prodotto_da_caricare["tipo"], prodotto_da_caricare["genere"],
                                 prodotto_da_caricare["materiale"], prodotto_da_caricare["colore"],
                                 prodotto_da_caricare["taglia"], prodotto_da_caricare["quantita"],
                                 prodotto_da_caricare["prezzo_acquisto"], prodotto_da_caricare["prezzo_vendita"],
                                 prodotto_da_caricare["stagione"], prodotto_da_caricare["stato"],
                                 prodotto_da_caricare["sconto_consigliato"],
                                 prodotto_da_caricare["sconto"], prodotto_da_caricare["data_vendita"]))

    # Metodo: salva il contenuto della lista su file pickle
    def save_data(self):
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)

    # Metodo: salvo il contenuto di una lista in particolare su file pickle
    def save_data_specialized(self, lista_prodotti):
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)
