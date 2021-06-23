from datetime import datetime

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti


class ControllerStatistica():
    def __init__(self, statistica):
        self.controller_listaprodotti = ControllerListaProdotti()
        self.controller_listaordini = ControllerListaOrdini()
        self.controller_listafornitori = ControllerListaFornitori()
        self.controller_listadelpersonale = ControllerListaDelPersonale()
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
            return self.andamento_finanziario(anno, stagione)

    # Metodo per costruire un dizionario contentente il codice del prodotto associato al numero di prodotti venduti
    def costruzione_dizionario(self, anno, stagione):
        lista_prodotti = self.controller_listaprodotti.get_lista_prodotti()
        dizionario = {}

        for prodotto in lista_prodotti:
            if prodotto.cod_prodotto not in dizionario.keys() and "Venduto" in prodotto.stato \
                    and prodotto.stagione == stagione:
                if anno is None:
                    dizionario[prodotto.cod_prodotto] = 0
                elif anno in prodotto.data_vendita:
                    dizionario[prodotto.cod_prodotto] = 0

        for prodotto in lista_prodotti:
            if prodotto.stagione == stagione and anno is None:
                if prodotto.data_vendita is not None and "," in prodotto.data_vendita:
                    dizionario[prodotto.cod_prodotto] += 2
                elif prodotto.data_vendita is not None and "," not in prodotto.data_vendita:
                    dizionario[prodotto.cod_prodotto] += 1
            elif prodotto.stagione == stagione and "Venduto" in prodotto.stato and anno in prodotto.data_vendita:
                if prodotto.data_vendita is not None and "," in prodotto.data_vendita:
                    dizionario[prodotto.cod_prodotto] += 2
                elif prodotto.data_vendita is not None and "," not in prodotto.data_vendita:
                    dizionario[prodotto.cod_prodotto] += 1

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
        lista_prodotti = self.controller_listaprodotti.get_lista_prodotti()
        dizionario = {}

        for prodotto in lista_prodotti:
            if prodotto.cod_prodotto not in dizionario.keys() and "Venduto" in prodotto.stato \
                    and prodotto.stagione == stagione:
                if anno is None:
                    dizionario[prodotto.cod_prodotto] = prodotto.prezzo_vendita - prodotto.prezzo_acquisto
                elif anno in prodotto.data_vendita:
                    dizionario[prodotto.cod_prodotto] = prodotto.prezzo_vendita - prodotto.prezzo_acquisto

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
        lista_ordini = self.controller_listaordini.get_lista_ordini()
        dizionario = {}

        for ordine in lista_ordini:
            if ordine.cod_fornitore not in dizionario.keys() and ordine.stagione == stagione:
                if anno is None:
                    dizionario[ordine.cod_fornitore] = 0
                elif anno in ordine.data_arrivo_prevista:
                    dizionario[ordine.cod_fornitore] = 0

        for ordine in lista_ordini:
            if ordine.stagione == stagione:
                if anno is None:
                    dizionario[ordine.cod_fornitore] += ordine.importo_totale
                elif anno in ordine.data_arrivo_prevista:
                    dizionario[ordine.cod_fornitore] += ordine.importo_totale

        return dizionario

    # Metodo per calcolare i fornitori da cui acquistiamo di più
    def forn_da_cui_acquistiamo_di_piu(self, anno, stagione):
        lista_ordini = self.controller_listaordini.get_lista_ordini()
        dizionario = {}

        for ordine in lista_ordini:
            if ordine.cod_fornitore not in dizionario.keys() and ordine.stagione == stagione:
                if anno == "":
                    dizionario[ordine.cod_fornitore] = 0
                elif anno in ordine.data_arrivo_prevista:
                    dizionario[ordine.cod_fornitore] = 0

        for ordine in lista_ordini:
            if ordine.stagione == stagione:
                if anno == "":
                    dizionario[ordine.cod_fornitore] += ordine.calzature_totali
                elif anno in ordine.data_arrivo_prevista:
                    dizionario[ordine.cod_fornitore] += ordine.calzature_totali

        return dizionario

    # Metodo per calcolare i fornitori più rapidi nella consegna
    def forn_piu_rapidi_nella_consegna(self, anno, stagione):
        lista_ordini = self.controller_listaordini.get_lista_ordini()
        dizionario = {}

        for ordine in lista_ordini:
            if ordine.cod_fornitore not in dizionario.keys() and ordine.data_arrivo_effettiva is not None \
                    and ordine.stagione == stagione:
                if anno is None:
                    dizionario[ordine.cod_fornitore] = 0
                elif anno in ordine.data_arrivo_prevista:
                    dizionario[ordine.cod_fornitore] = 0

        for ordine in lista_ordini:
            if ordine.data_arrivo_effettiva is not None and ordine.stagione == stagione:
                if anno is None:
                    d1 = datetime.strptime(ordine.data_arrivo_prevista, "%Y-%m-%d")
                    d2 = datetime.strptime(ordine.data_arrivo_effettiva, "%Y-%m-%d")
                    dizionario[ordine.cod_fornitore] = abs((d2 - d1).days)
                elif anno in ordine.data_arrivo_effettiva:
                    d1 = datetime.strptime(ordine.data_arrivo_prevista, "%Y-%m-%d")
                    d2 = datetime.strptime(ordine.data_arrivo_effettiva, "%Y-%m-%d")
                    dizionario[ordine.cod_fornitore] = abs((d2 - d1).days)

        return dizionario

    # Metodo per calcolare l'andamento finanziario
    def andamento_finanziario(self, anno, stagione):
        diz_prod_vend = self.costruzione_dizionario(anno, stagione)
        dizionario_af = {"Spesa totale": 0, "Incasso": 0, "Spesa prodotti": 0, "Guadagno": 0}
        lista_chiavi_usate = []

        lista_prodotti = self.controller_listaprodotti.get_lista_prodotti()
        for prodotto in lista_prodotti:
            if prodotto.cod_prodotto in diz_prod_vend.keys() \
                    and prodotto.cod_prodotto not in lista_chiavi_usate \
                    and "Venduto" in prodotto.stato and anno in prodotto.data_vendita:
                lista_chiavi_usate.append(prodotto.cod_prodotto)
                dizionario_af["Incasso"] += prodotto.prezzo_vendita * diz_prod_vend[prodotto.cod_prodotto]
                dizionario_af["Guadagno"] += (prodotto.prezzo_vendita - prodotto.prezzo_acquisto) * \
                                             diz_prod_vend[prodotto.cod_prodotto]

        lista_ordini = self.controller_listaordini.get_lista_ordini()
        for ordine in lista_ordini:
            if ordine.stagione == stagione and ordine.stato == "In negozio" \
                    and anno in ordine.data_arrivo_effettiva:
                dizionario_af["Spesa prodotti"] += ordine.importo_totale
        dizionario_af["Spesa totale"] = dizionario_af["Spesa prodotti"]

        lista_del_personale = self.controller_listadelpersonale.get_lista_del_personale()
        for utente in lista_del_personale:
            if utente.ruolo == "D":
                d1 = datetime.strptime(self.get_data_inizio_contratto(utente), "%Y-%m-%d")
                d2 = datetime.strptime(self.get_data_scadenza_contratto(utente), "%Y-%m-%d")
                if d1.year <= int(anno) <= d2.year:
                    dizionario_af["Spesa totale"] += utente.stipendio * 12

        return dizionario_af

    #Convertitore della data di inizio contratto
    def get_data_inizio_contratto(self, utente):
        if utente.data_inizio_contratto is None:
            return "00/00/0000"
        else:
            data = str(utente.data_inizio_contratto)
            data_divisa = data.split("/")
            giorno = data_divisa[0]
            mese = data_divisa[1]
            anno = data_divisa[2]
            data_covertita = anno + "-" + mese + "-" + giorno
            return data_covertita

    # Convertitore della data di scadenza contratto
    def get_data_scadenza_contratto(self, utente):
        if utente.data_scadenza_contratto is None:
            return "31/12/9999"
        else:
            data = str(utente.data_scadenza_contratto)
            data_divisa = data.split("/")
            giorno = data_divisa[0]
            mese = data_divisa[1]
            anno = data_divisa[2]
            data_covertita = anno + "-" + mese + "-" + giorno
            return data_covertita