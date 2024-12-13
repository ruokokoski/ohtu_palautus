from services.kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        if not self._onko_ok_siirto(tokan_siirto):
            return None
        return tokan_siirto