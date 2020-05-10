kayıtlı_kullanıcı_adı = "heceka"
kayıtlı_parola = "1234567"

giriş_hakkı = "3"

giriş_hakkı = int(giriş_hakkı)



while (giriş_hakkı > 0):
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")

    if(kullanıcı_adı == kayıtlı_kullanıcı_adı and parola != kayıtlı_parola):
        giriş_hakkı -= 1
        print("Parola hatalı...","\nKalan giriş hakkınız: ",giriş_hakkı)
        if(giriş_hakkı == 0):
            print("Giriş hakkınız bitti...")
            break

    elif (kullanıcı_adı != kayıtlı_kullanıcı_adı and parola == kayıtlı_parola):
        giriş_hakkı -= 1
        print("Kullanıcı Adı hatalı...","\nKalan giriş hakkınız: ",giriş_hakkı)
        if (giriş_hakkı == 0):
            print("Giriş hakkınız bitti...")
            break

    elif(kullanıcı_adı != kayıtlı_kullanıcı_adı and parola != kayıtlı_parola):
        giriş_hakkı -= 1
        print("Kullanıcı Adı ve Parola hatalı...","\nKalan giriş hakkınız: ",giriş_hakkı)
        if (giriş_hakkı == 0):
            print("Giriş hakkınız bitti...")
            break
    else:
        print("Sisteme başarıyla giriş yaptınız...")
        break