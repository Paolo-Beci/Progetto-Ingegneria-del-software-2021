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
                                 prodotto_da_caricare["marca"], prodotto_da_caricare["nome"],
                                 prodotto_da_caricare["tipo"], prodotto_da_caricare["genere"],
                                 prodotto_da_caricare["materiale"], prodotto_da_caricare["colore"],
                                 prodotto_da_caricare["taglia"], prodotto_da_caricare["quantita"],
                                 prodotto_da_caricare["prezzo_acquisto"], prodotto_da_caricare["prezzo_vendita"],
                                 prodotto_da_caricare["stagione"], prodotto_da_caricare["stato"],
                                 prodotto_da_caricare["sconto_consigliato"],
                                 prodotto_da_caricare["sconto"], prodotto_da_caricare["data_vendita"]))

    def filtra_prodotti(self):
        pass

    def aggiungi_prodotto(self, prodotto):
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

    def get_dimensione_lista_marche(self):
        return len(self.lista_marche)

    def get_prodotto_by_code(self, code):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == code:
                return prodotto

    # Giuseppe
    def get_anno_prodotto_by_code(self, codice):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == codice and prodotto.data_ordine is not None:
                splitted_date = prodotto.data_ordine.split("/")
                anno = splitted_date[2]
                return anno

    # Giuseppe
    def get_nome_prodotto_by_code(self, codice):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == codice and prodotto.nome is not None:
                return prodotto.nome
            elif prodotto.cod_prodotto == codice and prodotto.nome is None:
                return "Nessun nome"

    def get_prezzo_prodotto_by_code(self, codice):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == codice:
                return prodotto.prezzo_vendita

    def get_marca_prodotto_by_code(self, codice):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_prodotto == codice:
                return prodotto.marca

    def elimina_prodotto(self, codice_prodotto):
        def is_selected_prodotto(utente):
            if utente.cod_prodotto == codice_prodotto:
                return True
            return False

        self.lista_prodotti.remove(list(filter(is_selected_prodotto, self.lista_prodotti))[0])

    def aggiungi_prodotto_da_database(self, prodotto):
        self.lista_prodotti.append(prodotto)

    def save_data(self):
        with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)
