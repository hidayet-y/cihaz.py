from cihaz import Cihaz, AkilliCihaz


def main():
    cihaz1 = AkilliCihaz("Samsung", 2020, "Android", 56)
    cihaz2 = AkilliCihaz("iPhone", 2021, "iOS", 85)
    cihaz3 = AkilliCihaz("Xiaomi Redmi", 2022, "Android", 40)

    cihaz1.yazdir()
    cihaz2.yazdir()
    cihaz3.yazdir()
    Cihaz.toplam_cihaz_sayisi()
    AkilliCihaz.batarya_kontrol(cihaz1.batarya_kapasitesi)
    AkilliCihaz.batarya_kontrol(cihaz3.batarya_kapasitesi)


if __name__ == "__main__":
    main()