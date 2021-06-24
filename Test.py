import unittest, sys

#sys.path.append("C:\Users\Giuseppe\PycharmProjects\Progetto-Ingegneria-del-software-2021\listaprodotti\data")
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti

from prodotto.model.Prodotto import Prodotto

"""
    CLASSE DI TEST DEL PROGRAMMA
    DA FARE: test per ogni componente
"""


class Test(unittest.TestCase):
    def setUp(self):
        self.controller_listaprodotti = ControllerListaProdotti()
        self.model_lista_prodotti = self.controller_listaprodotti.get_lista_prodotti()
        self.prodotto = Prodotto(cod_fattura=100, cod_fornitore="AD000", data_ordine="28/07/2020", cod_prodotto="S01",
                                 marca="Pier One", nome=None, tipo="Eleganti", genere="U", materiale="Grafite",
                                 colore="Nero", taglia=49,
                                 quantita=1, prezzo_acquisto=60, prezzo_vendita=120, stagione="P/E", stato="Venduto",
                                 sconto_consigliato=20, sconto=15, data_vendita="26/03/2021")

    def test_inserisci_prodotto(self):
        self.assertIsNotNone(self.prodotto.cod_prodotto)
        self.controller_listaprodotti.inserisci_prodotto(self.prodotto)
        self.assertTrue(self.prodotto in self.model_lista_prodotti)

    def test_visualizza_prodotto(self):
        prodotto = self.controller_listaprodotti.get_prodotto_by_code(self.prodotto.cod_prodotto)
        self.assertTrue(prodotto is self.prodotto)


if __name__ == '__main__':
    unittest.main()
