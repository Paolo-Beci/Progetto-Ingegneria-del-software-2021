import json


class ControllerStatistica():
    def __init__(self, statistica):
        self.model = statistica

    def get_statistica(self, index):
        return self.model.get_statistica(index)

    #Metodi GET
    def get_nome(self):
        return self.model.nome

    def get_quantita(self):
        return self.model.quantita

    def get_contenuto(self):
        return self.model.contenuto

    #Metodi SET
    def set_nome(self, nome):
        self.model.nome = nome

    def set_quantita(self, quantita):
        self.model.quantita = quantita

    def set_contenuto(self, contenuto):
        self.model.contenuto = contenuto

    #Metodo smistatore (valori da 0 5)
    def smistatore(self, smistatore):
        #print(smistatore)
        self.costruzione_dizionario()
        if smistatore == 0:
            pass

        elif smistatore == 2:
            pass
        else:
            pass

    # Metodo per costruire un dizionario contentente il codice del prodotto associato al numero di prodotti venduti
    def costruzione_dizionario(self):
        with open('listaprodotti/data/database_prodotti.json') as f:
            lista_prodotti = json.load(f)
            lista_codici = []
            dizionario = {}

            for prodotto in lista_prodotti:
                if prodotto["cod_prodotto"] not in dizionario.keys():
                    dizionario[prodotto["cod_prodotto"]] = 0

            for prodotto in lista_prodotti:
                if prodotto["data_vendita"] is not None and "," in prodotto["data_vendita"]:
                    dizionario[prodotto["cod_prodotto"]] += 2
                elif prodotto["data_vendita"] is not None and "," not in prodotto["data_vendita"]:
                    dizionario[prodotto["cod_prodotto"]] += 1

            print(dizionario)

        return dizionario

    #Metodo che calcola i prodotti più venduti