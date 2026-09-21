from ultralytics.trackers.byte_tracker import BYTETracker

class Tracker:

    def __init__(self):
        """
        Tracker sınıfı.

        Görevi:
        - Aynı aracı kareler arasında takip etmek.
        - Her araca benzersiz (unique) bir ID vermek.
        - Araç ekrandan çıkana kadar aynı ID'yi korumak.
        """
        pass

    def update(self, detections): # update() fonksiyonu bizim detection formatımızı ByteTrack'in anlayacağı formata çevirecek.
        """
        Tracker'ı güncelle.

        Args:
            detections (list): Tespit edilen araçların listesi.
        """
        pass