print("\n\n Faiz Projeksiyon Aracı ")


anapara = input("\n\nHesabınızdaki anapara miktarını giriniz: ")
while not anapara.isdigit():
    anapara = input("\nYanlış tuşlama yaptınız. Hesabınızdaki anapara miktarını tam sayı cinsinden girmelisiniz: ")
ilk_anapara=anapara

yillik_faiz_orani = input("\nYıllık faiz oranını giriniz (%10 ise 10 yazınız): ")
while not yillik_faiz_orani.isdigit():
    yillik_faiz_orani = input("\nYanlış tuşlama yaptınız. Yıllık faiz oranını tam sayı cinsinden girmelisiniz (%10 ise 10 yazınız): ")

if float(yillik_faiz_orani) >= 100:
    emin = input("\nYanlış tuşlama yapmadığınızdan emin misiniz? (Evet 'E', Hayır 'H'): ")
    if emin == "H":
        yillik_faiz_orani = input("\nTekrardan yıllık faiz oranını giriniz (%10 ise 10 yazınız): ")
        while not yillik_faiz_orani.isdigit():
            yillik_faiz_orani = input(
                "\nYanlış tuşlama yaptınız. Yıllık faiz oranını sayı cinsinden girmelisiniz (%10 ise 10 yazınız): ")
    while not (emin == "H" or emin =="E"):
        emin = input("\nEmin olup olmadığınız belirtmek için lütfen 'E' veya 'H' tuşlayınız (Evet 'E', Hayır 'H'): ")
        if emin == "H":
            yillik_faiz_orani = input("\nTekrardan yıllık faiz oranını giriniz (%10 ise 10 yazınız): ")
            while not yillik_faiz_orani.isdigit():
                yillik_faiz_orani = input("\nYanlış tuşlama yaptınız. Yıllık faiz oranını sayı cinsinden girmelisiniz (%10 ise 10 yazınız): ")


ne_zaman = input("\nYatırım süresini ay bazında giriniz: ")
while not ne_zaman.isdigit():
    ne_zaman = input("\nYanlış tuşlama yaptınız. Yatırım süresini ay bazında tam sayı olarak giriniz:")


eklenecek_mi= input("\nHer ay anaparanın üstüne eklemeyi planladığınız miktar var mı? (Varsa 'V', Yoksa 'Y'): ")
while not (eklenecek_mi == "V" or eklenecek_mi ==  "Y"):
    eklenecek_mi = input("\nYanlış tuşlama yaptınız. Varsa 'V', Yoksa 'Y' tuşlayınız: ")

if eklenecek_mi == "V" :
    eklenme_miktari = input("\nHer ay ekleyeceğiniz miktarı giriniz: ")
    while not eklenme_miktari.isdigit():
        eklenme_miktari = input("\nYanlış tuşlama yaptınız. Her ay ekleyeceğiniz miktarı sayı cinsinden girmelisiniz: ")
    for i in range(1, int(ne_zaman) + 1):
        aylik_getiri = float(anapara) * (int(yillik_faiz_orani)/100) / 12
        anapara = float(anapara) + float(aylik_getiri)
        anapara = anapara + float(eklenme_miktari)
    print("\n{}. ayın sonunda bakiyeniz {:.2f} TL olacak.\n{} ay boyunca elde edilen toplam getiri: {:.0f} TL\nBu süre boyunca her ay ortalama {:.0f} TL kazandınız.\nSizin yatırdıklarınız dışında elde ettiğiniz: {:.0f} TL".format(ne_zaman, anapara,ne_zaman,anapara-int(ilk_anapara),(anapara-int(ilk_anapara))/int(ne_zaman),anapara-int(ilk_anapara)-int(eklenme_miktari)))
elif eklenecek_mi == "Y" :
    eklenecek_mi = False
    for i in range(1, int(ne_zaman) + 1):
        aylik_getiri = float(anapara) * (int(yillik_faiz_orani)/100) / 12
        anapara = float(anapara) + float(aylik_getiri)
    print("\n{}. ayın sonunda bakiyeniz {:.2f} TL olacak.\n{} ay boyunca elde edilen toplam getiri: {:.0f} TL\nBu süre boyunca her ay ortalama {:.0f} TL kazandınız.".format(ne_zaman, anapara,ne_zaman,anapara-int(ilk_anapara),(anapara-int(ilk_anapara))/int(ne_zaman)))
