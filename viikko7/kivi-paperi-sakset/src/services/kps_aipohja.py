from services.kps import KiviPaperiSakset

class KPSAIPohja(KiviPaperiSakset):
    def __init__(self, ai):
        self._ai = ai

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._ai.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._ai.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto