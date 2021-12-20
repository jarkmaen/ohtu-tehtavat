from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()
