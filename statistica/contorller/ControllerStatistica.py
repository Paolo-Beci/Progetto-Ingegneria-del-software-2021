import json


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
            self.ordinamento_decrescente(self.costruzione_dizionario())
        elif smistatore == 1:
            self.ordinamento_crescente(self.costruzione_dizionario())
        elif smistatore == 2:
            self.ordinamento_decrescente(self.prod_piu_redditizi())
        elif smistatore == 3:
            pass
        elif smistatore == 4:
            pass
        elif smistatore == 5:
            pass

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

    # Metodo che calcola i prodotti più venduti
    def ordinamento_decrescente(self, dizionario):
        lista_codici_ordinati = [(k, dizionario[k]) for k in
                                 sorted(dizionario, key=lambda x: dizionario[x], reverse=True)][:10]

        return lista_codici_ordinati

    # Metodo che calcola i prodotti più venduti
    def ordinamento_crescente(self, dizionario):
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
