import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10
            elif tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "kalja", 10)
            elif tuote_id == 3:
                return Tuote(3, "tomaatti", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_osta_kaksi_eri_ja_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("teemu", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("teemu", ANY, "54321", ANY, 15)

    def test_osta_kaksi_samaa_ja_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("teemu", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("teemu", ANY, "54321", ANY, 20)

    def test_osta_kaksi_eri_toinen_loppu_ja_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("teemu", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("teemu", ANY, "54321", ANY, 5)

    def test_aloita_asiointi_nollaa_edelliset_ostokset(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("teemu", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("teemu", ANY, "54321", ANY, 5)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pertti", "6789")
        self.pankki_mock.tilisiirto.assert_called_with("pertti", ANY, "6789", ANY, 20)
    
    def test_uusi_viitenumero_joka_maksulle(self):
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("teemu", "54321")
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("teemu", "54321")
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)
        
    def test_poista_tuote_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))