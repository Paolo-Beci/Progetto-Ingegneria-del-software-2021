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
    def smistatore_statistica(self, smistatore, anno, stagione):
        if smistatore == 0:
            return self.ordinamento_decrescente_prod(self.costruzione_dizionario(anno, stagione))
        elif smistatore == 1:
            return self.ordinamento_crescente_prod(self.costruzione_dizionario(anno, stagione))
        elif smistatore == 2:
            return self.ordinamento_decrescente_prod(self.prod_piu_redditizi(anno, stagione))
        elif smistatore == 3:
            return self.ordinamento_decrescente_forn(self.forn_piu_pagati(anno, stagione))
        elif smistatore == 4:
            return self.ordinamento_decrescente_forn(self.forn_da_cui_acquistiamo_di_piu(anno, stagione))
        elif smistatore == 5:
            return self.ordinamento_crescente_forn(self.forn_piu_rapidi_nella_consegna(anno, stagione))
        elif smistatore == 6:
            pass

    # Metodo per costruire un dizionario contentente il codice del prodotto associato al numero di prodotti venduti
    def costruzione_dizionario(self, anno, stagione):
        with open('listaprodotti/data/database_prodotti.json') as f:
            lista_prodotti = json.load(f)
            dizionario = {}

            for prodotto in lista_prodotti:
                if prodotto["cod_prodotto"] not in dizionario.keys() and prodotto["stato"] != "In arrivo" \
                        and prodotto["stagione"] == stagione:
                    if anno is None:
                        dizionario[prodotto["cod_prodotto"]] = 0
                    elif anno in prodotto["data_ordine"]:
                        dizionario[prodotto["cod_prodotto"]] = 0

            for prodotto in lista_prodotti:
                if prodotto["stagione"] == stagione and anno is None:
                    if prodotto["data_vendita"] is not None and "," in prodotto["data_vendita"]:
                        dizionario[prodotto["cod_prodotto"]] += 2
                    elif prodotto["data_vendita"] is not None and "," not in prodotto["data_vendita"]:
                        dizionario[prodotto["cod_prodotto"]] += 1
                elif prodotto["stagione"] == stagione and anno in prodotto["data_ordine"]:
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
    def prod_piu_redditizi(self, anno, stagione):
        with open('listaprodotti/data/database_prodotti.json') as f:
            lista_prodotti = json.load(f)
            dizionario = {}

        for prodotto in lista_prodotti:
            if prodotto["cod_prodotto"] not in dizionario.keys() and prodotto["stato"] != "In arrivo" \
                    and prodotto["stagione"] == stagione:
                if anno is None:
                    dizionario[prodotto["cod_prodotto"]] = prodotto["prezzo_vendita"] - prodotto["prezzo_acquisto"]
                elif anno in prodotto["data_ordine"]:
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
    def forn_piu_pagati(self, anno, stagione):
        with open('listaordini/data/DatabaseOrdine.json') as f:
            lista_ordini = json.load(f)
            dizionario = {}

        for ordine in lista_ordini:
            if ordine["cod_fornitore"] not in dizionario.keys() and ordine["stagione"] == stagione:
                if anno is None:
                    dizionario[ordine["cod_fornitore"]] = 0
                elif anno in ordine["data_ordine"]:
                    dizionario[ordine["cod_fornitore"]] = 0

        for ordine in lista_ordini:
            if ordine["stagione"] == stagione:
                if anno is None:
                    dizionario[ordine["cod_fornitore"]] += ordine["importo_totale"]
                elif anno in ordine["data_ordine"]:
                    dizionario[ordine["cod_fornitore"]] += ordine["importo_totale"]

        return dizionario

    # Metodo per calcolare i fornitori da cui acquistiamo di più
    def forn_da_cui_acquistiamo_di_piu(self, anno, stagione):
        with open('listaordini/data/DatabaseOrdine.json') as f:
            lista_ordini = json.load(f)
            dizionario = {}

        for ordine in lista_ordini:
            if ordine["cod_fornitore"] not in dizionario.keys() and ordine["stagione"] == stagione:
                if anno == "":
                    dizionario[ordine["cod_fornitore"]] = 0
                elif anno in ordine["data_ordine"]:
                    dizionario[ordine["cod_fornitore"]] = 0

        for ordine in lista_ordini:
            if ordine["stagione"] == stagione:
                if anno == "":
                    dizionario[ordine["cod_fornitore"]] += ordine["calzature_totali"]
                elif anno in ordine["data_ordine"]:
                    dizionario[ordine["cod_fornitore"]] += ordine["calzature_totali"]

        return dizionario

    # Metodo per calcolare i fornitori più rapidi nella consegna
    def forn_piu_rapidi_nella_consegna(self, anno, stagione):
        with open('listaordini/data/DatabaseOrdine.json') as f:
            lista_ordini = json.load(f)
            dizionario = {}

        for ordine in lista_ordini:
            if ordine["cod_fornitore"] not in dizionario.keys() and ordine["data_arrivo_effettiva"] is not None \
                    and ordine["stagione"] == stagione:
                if anno is None:
                    dizionario[ordine["cod_fornitore"]] = 0
                elif anno in ordine["data_ordine"]:
                    dizionario[ordine["cod_fornitore"]] = 0

        for ordine in lista_ordini:
            if ordine["data_arrivo_effettiva"] is not None and ordine["stagione"] == stagione:
                if anno is None:
                    d1 = datetime.strptime(ordine["data_arrivo_prevista"], "%Y-%m-%d")
                    d2 = datetime.strptime(ordine["data_arrivo_effettiva"], "%Y-%m-%d")
                    dizionario[ordine["cod_fornitore"]] = abs((d2 - d1).days)
                elif anno in ordine["data_ordine"]:
                    d1 = datetime.strptime(ordine["data_arrivo_prevista"], "%Y-%m-%d")
                    d2 = datetime.strptime(ordine["data_arrivo_effettiva"], "%Y-%m-%d")
                    dizionario[ordine["cod_fornitore"]] = abs((d2 - d1).days)

        return dizionario
