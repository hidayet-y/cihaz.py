class Cihaz:
    cihaz_sayisi = 0
    def __init__(self, model, uretim_yili):
        self.model = model
        self.uretim_yili = uretim_yili
        Cihaz.cihaz_sayisi += 1

    def yazdir(self):
        print(f"Modeli: {self.model}")
        print(f"Üretim Yılı: {self.uretim_yili}")

    @classmethod
    def toplam_cihaz_sayisi(cls):
        print(f"Toplam cihaz sayısı: {cls.cihaz_sayisi}")


class AkilliCihaz(Cihaz):
    def __init__(self, model, uretim_yili,isletim_sistemi, batarya_kapasitesi):
        super().__init__(model, uretim_yili)
        self.isletim_sistemi = isletim_sistemi
        self.batarya_kapasitesi = batarya_kapasitesi

    def yazdir(self):
        super().yazdir()
        print(f"İşletim Sistemi: {self.isletim_sistemi}")
        print(f"Batarya kapasitesi: {self.batarya_kapasitesi}%")

    @staticmethod
    def batarya_kontrol(batarya_kapasitesi):
        if batarya_kapasitesi < 50:
            print("Batarya gün boyu kullanıma uygun değildir.")
        else:
            print("Batarya gün boyu kullanıma uygundur.")
