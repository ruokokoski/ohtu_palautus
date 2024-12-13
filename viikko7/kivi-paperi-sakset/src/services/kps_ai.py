from services.kps_aipohja import KPSAIPohja
from services.tekoaly import Tekoaly
from services.tekoaly_parannettu import TekoalyParannettu

class KPSAI(KPSAIPohja):
    def __init__(self):
        super().__init__(Tekoaly())

class KPSParempiAI(KPSAIPohja):
    def __init__(self):
        super().__init__(TekoalyParannettu(10))