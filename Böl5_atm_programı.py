print("""
**************************************
          ATM'ye Hoşgeldiniz

               İşlemler

1. Bakiye Sorma

2. Para Yatırma

3. Para Çekme

4. Para Transferi

5. İletişim Bilgileri Güncelleme

Çıkmak içi q'ya basınız!!!

**************************************** """)

bakiye = 1000

while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz: ")

    if (işlem == "q"):
        print("ATM Programı sonlandırılıyor.\nYine bekleriz...")
        break

    elif (işlem == "1"):
        print("Bakiye: ",bakiye)

    elif(işlem == "2"):
        yatırılacak_para = int(input("Yatırılacak miktarı giriniz: "))
        bakiye += yatırılacak_para
        print("Para hesabınıza yatırıldı.\nBakiye: ",bakiye)

    elif (işlem == "3"):
        çekilecek_para = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if (bakiye - çekilecek_para < 0):
            print("Bakiye yetersiz...")
            continue
        bakiye -= çekilecek_para
        print("Para hesabınızdan çekilmiştir.\nBakiye: ",bakiye)

    elif (işlem == "4"):
        kişi = input("Paranın gönderileceği kişiyi giriniz: ")
        hesap_no = input("Hesap numarasını giriniz: ")
        miktar = int(input("Gönderilecek para miktarını giriniz: "))
        if (bakiye - miktar < 0):
            print("Bakiye yetersiz...")
            continue
        print("{} isimli {} hesap numaralı kişiye {} TL para transferi gerçekleşmiştir.".format(kişi,hesap_no,miktar))

    elif (işlem == "5"):
        seç = input("Adresiniz güncel mi?(y/n) : ")
        if (seç == "y"):
            seç = input("Telefon numaranız güncel mi? (y/n)")
            if (seç == "y"):
                seç = input("E-mail adresiniz güncel mi?(y/n)")
                if (seç == "y"):
                    print("Bilgileriniz güncel...")
                elif(seç == "n"):
                    input("E-mail adresiniz: ")
                    print("E-Mail adresiniz güncellendi...")
                else:
                    print("Böyle bir seçenek bulunmamaktadır...")
            elif (seç == "n"):
                input("Telefon numaranız: ")
                print("Telefon numaranız güncellendi...")
                seç = input("E-mail adresiniz güncel mi?(y/n)")
                if (seç == "y"):
                    print("Bilgileriniz güncel...")
                elif(seç == "n"):
                    input("E-mail adresiniz: ")
                    print("E-Mail adresiniz güncellendi...")
                else:
                    print("Böyle bir seçenek bulunmamaktadır...")
            else:
                print("Böyle bir seçenek bulunmamaktadır.")
        elif (seç == "n"):
            input("Adresiniz: ")
            print("Adresiniz güncellendi...")
            seç = input("Telefon numaranız güncel mi? (y/n)")
            if (seç == "y"):
                seç = input("E-mail adresiniz güncel mi?(y/n)")
                if (seç == "y"):
                    print("Bilgileriniz güncel...")
                elif (seç == "n"):
                    input("E-mail adresiniz: ")
                    print("E-Mail adresiniz güncellendi...")
                else:
                    print("Böyle bir seçenek bulunmamaktadır...")
            elif (seç == "n"):
                input("Telefon numaranız: ")
                print("Telefon numaranız güncellendi...")
                seç = input("E-mail adresiniz güncel mi?(y/n)")
                if (seç == "y"):
                    print("Bilgileriniz güncel...")
                elif (seç == "n"):
                    input("E-mail adresiniz: ")
                    print("E-Mail adresiniz güncellendi...")
                else:
                    print("Böyle bir seçenek bulunmamaktadır...")
            else:
                print("Böyle bir seçenek bulunmamaktadır.")
    else:
        print("Geçersiz işlem...")