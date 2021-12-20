from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        if self._onko_ok_siirto(ensimmaisen_siirto):
            return input("Toisen pelaajan siirto: ")
        else:
            return None
