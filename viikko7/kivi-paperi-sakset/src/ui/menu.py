from services.kps_pvp import KPSPelaajaVsPelaaja
from services.kps_ai import KPSAI, KPSParempiAI

def show_menu():
    while True:
        options = {
            "a": lambda: KPSPelaajaVsPelaaja().pelaa(),
            "b": lambda: KPSAI().pelaa(),
            "c": lambda: KPSParempiAI().pelaa()
        }
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus in options:
            options[vastaus]()
        else:
            break