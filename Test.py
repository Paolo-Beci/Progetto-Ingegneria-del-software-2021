import unittest
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.controller.ControllerProdotto import ControllerProdotto

from prodotto.model.Prodotto import Prodotto

"""
    CLASSE DI TEST DEL PROGRAMMA
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

        self.controller_prodotto = ControllerProdotto(self.prodotto)

    def test_inserisci_prodotto(self):
        self.assertIsNotNone(self.prodotto.cod_prodotto)
        self.controller_listaprodotti.inserisci_prodotto(self.prodotto)
        self.assertTrue(self.prodotto in self.model_lista_prodotti)

    def test_filtra_lista_prodotti(self):
        elementi_da_rimuovere= []
        for prodotto in self.model_lista_prodotti:
            if prodotto.stato != "Venduto":
                elementi_da_rimuovere.append(prodotto)
        for prodotto in elementi_da_rimuovere:
            self.model_lista_prodotti.remove(prodotto)
        elementi_da_rimuovere.clear()

        for prodotto in self.model_lista_prodotti:
            if "Venduto" not in prodotto.stato:
                self.fail()

    def test_visualizza_prodotto(self):
        prodotto = self.controller_listaprodotti.get_prodotto_by_code(self.prodotto.cod_prodotto)
        self.assertTrue(prodotto, self.prodotto)

    def test_modifica_prodotto(self):
        self.controller_prodotto.set_cod_prodotto("S02")
        self.assertEqual(self.controller_prodotto.get_cod_prodotto(), "S02")

    def test_elimina_prodotto(self):
        self.assertIsNotNone(self.model_lista_prodotti)
        self.controller_listaprodotti.elimina_prodotto_by_codice(self.prodotto.cod_prodotto, self.model_lista_prodotti)
        self.assertTrue(self.prodotto not in self.model_lista_prodotti)

if __name__ == '__main__':
    unittest.main()
