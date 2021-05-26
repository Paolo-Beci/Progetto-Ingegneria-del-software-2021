import json
from datetime import datetime

class ControllerStatistica():
    def __init__(self, statistica):
        self.model = statistica

    def get_statistica(self, index):
        return self.model.get_statistica(index)

    # Metodi GET
    def get_nome(self):
        return self.model.nome

    def get_quantita(self):
        return self.model.quantita

    def get_contenuto(self):
        return self.model.contenuto

    # Metodi SET
    def set_nome(self, nome):
        self.model.nome = nome

    def set_quantita(self, quantita):
        self.model.quantita = quantita

    def set_contenuto(self, contenuto):
        self.model.contenuto = contenuto

    # Metodo per richiamare la statistica da calcolare in base alla scelta effettuata
    def smistatore_statistica(self, smistatore):
        if smistatore == 0:
            self.ordinamento_decrescente_prod(self.costruzione_dizionario())
        elif smistatore == 1:
            self.ordinamento_crescente_prod(self.costruzione_dizionario())
        elif smistatore == 2:
            self.ordinamento_decrescente_prod(self.prod_piu_redditizi())
        elif smistatore == 3:
            self.ordinamento_decrescente_forn(self.forn_piu_pagati())
        elif smistatore == 4:
            self.ordinamento_decrescente_forn(self.forn_da_cui_acquistiamo_di_piu())
        elif smistatore == 5:
            self.ordinamento_crescente_forn(self.forn_piu_rapidi_nella_consegna())

    # Metodo per costruire un dizionario contentente il codice del prodotto associato al numero di prodotti venduti
    def costruzione_dizionario(self):
        with open('listaprodotti/data/database_prodotti.json') as f:
            lista_prodotti = json.load(f)
            dizionario = {}

            for prodotto in lista_prodotti:
                if prodotto["cod_prodotto"] not in dizionario.keys() and prodotto["stato"] != "In arrivo":
                    dizionario[prodotto["cod_prodotto"]] = 0

            for prodotto in lista_prodotti:
                if prodotto["data_vendita"] is not None and "," in prodotto["data_vendita"]:
                    dizionario[prodotto["cod_prodotto"]] += 2
                elif prodotto["data_vendita"] is not None and "," not in prodotto["data_vendita"]:
                    dizionario[prodotto["cod_prodotto"]] += 1

        return dizionario

    # Metodo che ordina in modo decresente il dizionario passato in base ai valori
    def ordinamento_decrescente_prod(self, dizionario):
        lista_codici_ordinati = [(k, dizionario[k]) for k in
                                 sorted(dizionario, key=lambda x: dizionario[x], reverse=True)][:10]

        return lista_codici_ordinati

    # Metodo che ordina in modo cresente il dizionario passato in base ai valori
    def ordinamento_crescente_prod(self, dizionario):
        lista_codici_ordinati = [(k, dizionario[k]) for k in
                                 sorted(dizionario, key=lambda x: dizionario[x])][:10]

        return lista_codici_ordinati

    # Metodo per calcolare i prodotti più redditizi
    def prod_piu_redditizi(self):
        with open('listaprodotti/data/database_prodotti.json') as f:
            lista_prodotti = json.load(f)
            dizionario = {}

            for prodotto in lista_prodotti:
                if prodotto["cod_prodotto"] not in dizionario.keys() and prodotto["stato"] != "In arrivo":
                    dizionario[prodotto["cod_prodotto"]] = prodotto["prezzo_vendita"] - prodotto["prezzo_acquisto"]

            return dizionario

    # Metodo che ordina in modo decresente il dizionario passato in base ai valori
    def ordinamento_decrescente_forn(self, dizionario):
        lista_codici_ordinati = [(k, dizionario[k]) for k in
                                 sorted(dizionario, key=lambda x: dizionario[x], reverse=True)][:3]

        return lista_codici_ordinati

    # Metodo che ordina in modo decresente il dizionario passato in base ai valori
    def ordinamento_crescente_forn(self, dizionario):
        lista_codici_ordinati = [(k, dizionario[k]) for k in
                                 sorted(dizionario, key=lambda x: dizionario[x])][:3]

        return lista_codici_ordinati

    # Metodo per calcolare i fornitori più pagati
    def forn_piu_pagati(self):
        with open('listaordini/data/DatabaseOrdine.json') as f:
            lista_ordini = json.load(f)
            dizionario = {}

        for ordine in lista_ordini:
            if ordine["cod_fornitore"] not in dizionario.keys():
                dizionario[ordine["cod_fornitore"]] = 0

        for ordine in lista_ordini:
            dizionario[ordine["cod_fornitore"]] += ordine["importo_totale"]

        return dizionario

    # Metodo per calcolare i fornitori da cui acquistiamo di più
    def forn_da_cui_acquistiamo_di_piu(self):
        with open('listaordini/data/DatabaseOrdine.json') as f:
            lista_ordini = json.load(f)
            dizionario = {}

        for ordine in lista_ordini:
            if ordine["cod_fornitore"] not in dizionario.keys():
                dizionario[ordine["cod_fornitore"]] = 0

        for ordine in lista_ordini:
            dizionario[ordine["cod_fornitore"]] += ordine["calzature_totali"]

        return dizionario

    # Metodo per calcolare i fornitori più rapidi nella consegna
    def forn_piu_rapidi_nella_consegna(self):
        with open('listaordini/data/DatabaseOrdine.json') as f:
            lista_ordini = json.load(f)
            dizionario = {}

        for ordine in lista_ordini:
            if ordine["cod_fornitore"] not in dizionario.keys():
                dizionario[ordine["cod_fornitore"]] = 0

        for ordine in lista_ordini:
            d1 = datetime.strptime(ordine["data_arrivo_prevista"], "%Y-%m-%d")
            d2 = datetime.strptime(ordine["data_arrivo_effettiva"], "%Y-%m-%d")
            dizionario[ordine["cod_fornitore"]] = abs((d2 - d1).days)

        return dizionario
