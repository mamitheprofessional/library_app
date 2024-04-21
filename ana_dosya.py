import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


kutuphane_kitaplari={}


def arama_penceresi():
    arama_pencere = tk.Toplevel()
    arama_pencere.title("Kitap Arama")

    arama_etiketi = tk.Label(arama_pencere, text="Aramak istediğiniz kitabın adını girin:")
    arama_etiketi.pack()

    arama_giris = tk.Entry(arama_pencere)
    arama_giris.pack()

    def kitap_ara_buton():
        kitap_ara = arama_giris.get()
        found = False
        with open("kutuphane_kitap_listesi.txt", "r") as dosya:
            for satir in dosya:
                if kitap_ara.lower() in satir.lower():
                    sonuc = f"{satir.strip()} kitap kütüphanede mevcut"
                    found = True
                    break
            if not found:
                sonuc = f"'{kitap_ara}' kitabı kütüphanede bulunamadı"

        sonuc_penceresi(sonuc)

    arama_button = tk.Button(arama_pencere, text="Ara", command=kitap_ara_buton)
    arama_button.pack()


def sonuc_penceresi(sonuc):
    sonuc_pencere = tk.Toplevel()
    sonuc_pencere.title("Arama Sonuçları")

    sonuc_etiketi = tk.Label(sonuc_pencere, text=sonuc)
    sonuc_etiketi.pack()


def kitap_ekle_penceresi():
    def ekle_buton_tikla():
        kitap_adi = kullanıcıdan_al_1.get().strip()  # Kitap adını alırken boşlukları sil
        if kitap_adi.lower() in kutuphane_kitaplari.keys():
            messagebox.showerror("Hata", "Bu isimde bir kitap zaten kütüphanede bulunmaktadır.")
            return

        yazar_adi = kullanıcıdan_al_2.get()
        isbn_numarasi = kullanıcıdan_al_3.get()
        yayin_evi = kullanıcıdan_al_4.get()
        yil = kullanıcıdan_al_5.get()
        sayfa_sayisi = kullanıcıdan_al_6.get()
        dil = kullanıcıdan_al_7.get()
        tur = kullanıcıdan_al_8.get()

        # Kullanıcı girişlerini sözlüğe ekleyin
        kutuphane_kitaplari[kitap_adi] = {
            "Yazar Adı": yazar_adi,
            "ISBN Numarası": isbn_numarasi,
            "Yayın Evi": yayin_evi,
            "Yıl": yil,
            "Sayfa Sayısı": sayfa_sayisi,
            "Dil": dil,
            "Tür": tur
        }

        # Kullanıcı girişlerini dosyaya ekle
        with open("kutuphane_kitap_listesi.txt", "a") as dosya:
            dosya.write(f"{kitap_adi}:\n")
            dosya.write(f"Yazar: {yazar_adi}\n")
            dosya.write(f"ISBN: {isbn_numarasi}\n")
            dosya.write(f"Yayınevi: {yayin_evi}\n")
            dosya.write(f"Yıl: {yil}\n")
            dosya.write(f"Dil: {dil}\n")
            dosya.write(f"Tür: {tur}\n")
            dosya.write(f"Sayfa Sayısı: {sayfa_sayisi}\n\n")

            messagebox.showinfo("Başarılı", "Kitap başarıyla eklendi!")
            
            

            # kitap başarıyla eklendi mesajını gördükten sonra pencere kapansın ve yeniden açılsın
            ekle_pencere.destroy()
            kitap_ekle_penceresi()

    ekle_pencere = tk.Toplevel()
    ekle_pencere.title("Kitap Ekle")

    ekleme_etiketi_1 = tk.Label(ekle_pencere, text="Eklemek istediğiniz kitap adını yazınız:")
    ekleme_etiketi_1.pack()

    kullanıcıdan_al_1 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_1.pack()

    ekleme_etiketi_2 = tk.Label(ekle_pencere, text="Yazar adı giriniz:")
    ekleme_etiketi_2.pack()

    kullanıcıdan_al_2 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_2.pack()

    ekleme_etiketi_3 = tk.Label(ekle_pencere, text="ISBN numarası giriniz:")
    ekleme_etiketi_3.pack()

    kullanıcıdan_al_3 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_3.pack()

    ekleme_etiketi_4 = tk.Label(ekle_pencere, text="Yayın evi giriniz:")
    ekleme_etiketi_4.pack()

    kullanıcıdan_al_4 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_4.pack()

    ekleme_etiketi_5 = tk.Label(ekle_pencere, text="Yıl giriniz:")
    ekleme_etiketi_5.pack()

    kullanıcıdan_al_5 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_5.pack()

    ekleme_etiketi_6 = tk.Label(ekle_pencere, text="Sayfa Sayısı giriniz:")
    ekleme_etiketi_6.pack()

    kullanıcıdan_al_6 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_6.pack()

    ekleme_etiketi_7 = tk.Label(ekle_pencere, text="Dil giriniz:")
    ekleme_etiketi_7.pack()

    kullanıcıdan_al_7 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_7.pack()

    ekleme_etiketi_8 = tk.Label(ekle_pencere, text="Tür giriniz:")
    ekleme_etiketi_8.pack()

    kullanıcıdan_al_8 = tk.Entry(ekle_pencere)
    kullanıcıdan_al_8.pack()

    ekle_buton = tk.Button(ekle_pencere, text="Ekle", command=ekle_buton_tikla)
    ekle_buton.pack()


def kitap_silme_penceresi():
    def kitap_silme_buton_tikla():
        kitap_adi = silmeye_giris.get()
        found = False

        # dosyayı oku kullanıcının yazdığı kitabı sil
        with open("kutuphane_kitap_listesi.txt", "r") as dosya:
            lines = dosya.readlines()
        with open("kutuphane_kitap_listesi.txt", "w") as dosya:
            for line in lines:
                if kitap_adi.lower() not in line.lower():
                    dosya.write(line)
                else:
                    found = True

        if found:
            sonuc_penceresi(f"{kitap_adi} kitabı başarıyla silindi.")
            sil_pencere.destroy() #pencereyi kapat
        else:
            sonuc_penceresi(f"{kitap_adi} kitabı bulunamadı.")

    sil_pencere = tk.Toplevel()
    sil_pencere.title("Kitap Sil")

    silme_etiketi = tk.Label(sil_pencere, text="Silmek istediğiniz kitap adını giriniz:")
    silme_etiketi.pack()

    silmeye_giris = tk.Entry(sil_pencere)
    silmeye_giris.pack()

    silme_buton = tk.Button(sil_pencere, text="Sil", command=kitap_silme_buton_tikla)
    silme_buton.pack()


def txt_dosyayi_ac():
    try:
        with open("kutuphane_kitap_listesi.txt", "r") as dosya:
            icerik = dosya.read()

        # Açılan dosyanın içeriğini gösteren bir pencere oluştur
        dosya_penceresi = tk.Toplevel()
        dosya_penceresi.title("Kütüphane Kitap Listesi")
        dosya_metin = tk.Text(dosya_penceresi)
        dosya_metin.insert(tk.END, icerik)
        dosya_metin.pack(fill=tk.BOTH, expand=True)

    except FileNotFoundError:
        # Dosya bulunamazsa hata mesajı göster
        hata_penceresi = tk.Toplevel()
        hata_penceresi.title("Hata")
        hata_etiket = tk.Label(hata_penceresi, text="Dosya bulunamadı.")
        hata_etiket.pack()


def kitap_odunc_ver():
    def odunc_sistem():
        kisi_isim = odunc_alan_kisi_ismi.get()
        kitap_isim = kitap_ismi_al.get()
        verilis_tarihi = odunc_tarihi.get()
        alis_tarihi = iade_tarihi.get()

        with open("kutuphane_kitap_listesi.txt", "r") as dosya:
            kitap_listesi = dosya.readlines()

        kitap_bulundu = False
        for kitap in kitap_listesi:
            if kitap_isim.lower() in kitap.lower():
                kitap_bulundu = True
                break

        if kitap_bulundu:
            with open("ödünç_alanlar.txt", "r") as odunc_dosya:
                odunc_alanlar = odunc_dosya.readlines()
                for odunc_alan in odunc_alanlar:
                    if kitap_isim.lower() in odunc_alan.lower():
                        messagebox.showerror("Hata", f"{kitap_isim} kitabı zaten ödünç alınmış.")
                        return

            with open("ödünç_alanlar.txt", "a") as odunc_dosya:
                odunc_dosya.write(f"Kitap ismi: {kitap_isim}\n")
                odunc_dosya.write(f"Ödünç alan kişi: {kisi_isim}\n")
                odunc_dosya.write(f"Veriliş tarihi: {verilis_tarihi}\n")
                odunc_dosya.write(f"Alış tarihi: {alis_tarihi}\n\n")

            messagebox.showinfo("Başarılı", f"{kitap_isim} kitabı {kisi_isim} adlı kişiye ödünç verildi.")
        else:
            messagebox.showerror("Hata", f"{kitap_isim} kitabı bulunamadı.")



    odunc_ver = tk.Toplevel()
    odunc_ver.title("Ödünç Verme Sistemi")

    isim_etiket = tk.Label(odunc_ver, text="Kişi İsmi:")
    isim_etiket.pack()

    odunc_alan_kisi_ismi = tk.Entry(odunc_ver)
    odunc_alan_kisi_ismi.pack()

    kitap_isim_etiket = tk.Label(odunc_ver, text="Kitap İsmi:")
    kitap_isim_etiket.pack()

    kitap_ismi_al = tk.Entry(odunc_ver)
    kitap_ismi_al.pack()

    odunc_tarih_etiket = tk.Label(odunc_ver, text="Ödünç Tarihi:")
    odunc_tarih_etiket.pack()

    odunc_tarihi = tk.Entry(odunc_ver)
    odunc_tarihi.pack()

    iade_tarihi_etiket = tk.Label(odunc_ver, text="İade Tarihi:")
    iade_tarihi_etiket.pack()

    iade_tarihi = tk.Entry(odunc_ver)
    iade_tarihi.pack()

    odunc_buton = tk.Button(odunc_ver, text="Kitap Ödünç Ver", command=odunc_sistem)
    odunc_buton.pack()


def odunc_kitaplari_goster():
    try:
        with open("ödünç_alanlar.txt", "r") as dosya:
            icerik = dosya.read()

        # Açılan dosyanın içeriğini gösteren bir pencere oluştur
        dosya_penceresi = tk.Toplevel()
        dosya_penceresi.title("ödünç alanlar Listesi")
        dosya_metin = tk.Text(dosya_penceresi)
        dosya_metin.insert(tk.END, icerik)
        dosya_metin.pack(fill=tk.BOTH, expand=True)

    except FileNotFoundError:
        # Dosya bulunamazsa hata mesajı göster
        hata_penceresi = tk.Toplevel()
        hata_penceresi.title("Hata")
        hata_etiket = tk.Label(hata_penceresi, text="Dosya bulunamadı.")
        hata_etiket.pack()


def KullaniciEkleme():
    def ogrenci():
        def bilgileri_kaydet():
            ad = ad_entry.get()
            soyad = soyad_entry.get()
            tc_no = tc_entry.get()

            if len(tc_no) != 11 or not tc_no.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir TC Kimlik No giriniz.")
            else:
                with open("ogrenci_bilgileri.txt", "a") as dosya:
                    dosya.write("isim={}\nsoyisim={}\ntc={}\n\n".format(ad, soyad, tc_no))
                messagebox.showinfo("Bilgi", "Bilgiler kaydedildi.\nAd: {}\nSoyad: {}\nTC Kimlik No: {}".format(ad, soyad, tc_no))
                ogrenci_penceresi.destroy()

        ogrenci_penceresi = tk.Toplevel()
        ogrenci_penceresi.title("Öğrenci Bilgileri")
        ogrenci_penceresi.geometry("300x200+750+350")

        ad_label = tk.Label(ogrenci_penceresi, text="Ad:")
        ad_label.grid(row=0, column=0, padx=10, pady=5)
        ad_entry = tk.Entry(ogrenci_penceresi)
        ad_entry.grid(row=0, column=1, padx=10, pady=5)

        soyad_label = tk.Label(ogrenci_penceresi, text="Soyad:")
        soyad_label.grid(row=1, column=0, padx=10, pady=5)
        soyad_entry = tk.Entry(ogrenci_penceresi)
        soyad_entry.grid(row=1, column=1, padx=10, pady=5)

        tc_label = tk.Label(ogrenci_penceresi, text="TC Kimlik No:")
        tc_label.grid(row=2, column=0, padx=10, pady=5)
        tc_entry = tk.Entry(ogrenci_penceresi)
        tc_entry.grid(row=2, column=1, padx=10, pady=5)

        kaydet_buton = tk.Button(ogrenci_penceresi, text="Kaydet", command=bilgileri_kaydet)
        kaydet_buton.grid(row=3, column=0, columnspan=2, pady=10)

    def gorevli():
        def bilgileri_kaydet():
            ad = ad_entry.get()
            soyad = soyad_entry.get()
            tc_no = tc_entry.get()
            sifre = sifre_entry.get()

            if len(tc_no) != 11 or not tc_no.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir Telefon No giriniz.")
            else:
                with open("görevli_bilgileri.txt", "a") as dosya:
                    dosya.write("isim={}\nsoyisim={}\ntel={}\nşifre={}\n\n".format(ad, soyad, tc_no, sifre))
                messagebox.showinfo("Bilgi", "Bilgiler kaydedildi.\nAd: {}\nSoyad: {}\nTel No: {}\nŞifre: {}".format(ad, soyad, tc_no, sifre))
                ogrenci_penceresi.destroy()

        ogrenci_penceresi = tk.Toplevel()
        ogrenci_penceresi.title("Görevli Bilgileri")
        ogrenci_penceresi.geometry("350x230+750+350")

        ad_label = tk.Label(ogrenci_penceresi, text="Ad:")
        ad_label.grid(row=0, column=0, padx=10, pady=5)
        ad_entry = tk.Entry(ogrenci_penceresi)
        ad_entry.grid(row=0, column=1, padx=10, pady=5)

        soyad_label = tk.Label(ogrenci_penceresi, text="Soyad:")
        soyad_label.grid(row=1, column=0, padx=10, pady=5)
        soyad_entry = tk.Entry(ogrenci_penceresi)
        soyad_entry.grid(row=1, column=1, padx=10, pady=5)

        tc_label = tk.Label(ogrenci_penceresi, text="Telefon No:")
        tc_label.grid(row=2, column=0, padx=10, pady=5)
        tc_entry = tk.Entry(ogrenci_penceresi)
        tc_entry.grid(row=2, column=1, padx=10, pady=5)

        sifre_label = tk.Label(ogrenci_penceresi, text="şifre:")
        sifre_label.grid(row=3, column=0, padx=10, pady=5)
        sifre_entry = tk.Entry(ogrenci_penceresi)
        sifre_entry.grid(row=3, column=1, padx=10, pady=5)

        kaydet_buton = tk.Button(ogrenci_penceresi, text="Kaydet", command=bilgileri_kaydet)
        kaydet_buton.grid(row=4, column=0, columnspan=2, pady=10)

    def yonetici():
        def bilgileri_kaydet():
            ad = ad_entry.get()
            soyad = soyad_entry.get()
            tc_no = tc_entry.get()
            sifre = sifre_entry.get()

            if len(tc_no) != 11 or not tc_no.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir Telefon No giriniz.")
            else:
                with open("yönetici_bilgileri.txt", "a") as dosya:
                    dosya.write("isim={}\nsoyisim={}\ntel={}\nşifre={}\n\n".format(ad, soyad, tc_no, sifre))
                messagebox.showinfo("Bilgi", "Bilgiler kaydedildi.\nAd: {}\nSoyad: {}\nTel No: {}\nŞifre: {}".format(ad, soyad, tc_no, sifre))
                ogrenci_penceresi.destroy()

        ogrenci_penceresi = tk.Toplevel()
        ogrenci_penceresi.title("Yönetici Bilgileri")
        ogrenci_penceresi.geometry("350x230+750+350")

        ad_label = tk.Label(ogrenci_penceresi, text="Ad:")
        ad_label.grid(row=0, column=0, padx=10, pady=5)
        ad_entry = tk.Entry(ogrenci_penceresi)
        ad_entry.grid(row=0, column=1, padx=10, pady=5)

        soyad_label = tk.Label(ogrenci_penceresi, text="Soyad:")
        soyad_label.grid(row=1, column=0, padx=10, pady=5)
        soyad_entry = tk.Entry(ogrenci_penceresi)
        soyad_entry.grid(row=1, column=1, padx=10, pady=5)

        tc_label = tk.Label(ogrenci_penceresi, text="Telefon No:")
        tc_label.grid(row=2, column=0, padx=10, pady=5)
        tc_entry = tk.Entry(ogrenci_penceresi)
        tc_entry.grid(row=2, column=1, padx=10, pady=5)

        sifre_label = tk.Label(ogrenci_penceresi, text="şifre:")
        sifre_label.grid(row=3, column=0, padx=10, pady=5)
        sifre_entry = tk.Entry(ogrenci_penceresi)
        sifre_entry.grid(row=3, column=1, padx=10, pady=5)

        kaydet_buton = tk.Button(ogrenci_penceresi, text="Kaydet", command=bilgileri_kaydet)
        kaydet_buton.grid(row=4, column=0, columnspan=2, pady=10)

    kullanici_secim_penceresi = tk.Toplevel(pencere)
    kullanici_secim_penceresi.title("Kullanıcı Ekleme")
    kullanici_secim_penceresi.geometry("300x150+750+350")

    secim_var = tk.StringVar()

    ogrenci_buton = tk.Radiobutton(kullanici_secim_penceresi, text="Öğrenci", variable=secim_var, value="ogrenci")
    ogrenci_buton.pack(anchor=tk.W)

    gorevli_buton = tk.Radiobutton(kullanici_secim_penceresi, text="Görevli", variable=secim_var, value="gorevli")
    gorevli_buton.pack(anchor=tk.W)

    yonetici_buton = tk.Radiobutton(kullanici_secim_penceresi, text="Yönetici", variable=secim_var, value="yonetici")
    yonetici_buton.pack(anchor=tk.W)

    def onayla():
        secilen = secim_var.get()
        if secilen == "ogrenci":
            ogrenci()
        elif secilen == "gorevli":
            gorevli()
        elif secilen == "yonetici":
            yonetici()
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir seçim yapın.")

    onay_buton = tk.Button(kullanici_secim_penceresi, text="Onayla", command=onayla)
    onay_buton.pack()



def kullanici_sil():
    def ogrenci_sil():
        def sil():
            tc_no = tc_entry.get()
            isim = isim_entry.get()
            soyisim = soyisim_entry.get()
            if len(tc_no) != 11 or not tc_no.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir TC Kimlik No giriniz.")
            else:
                with open("ogrenci_bilgileri.txt", "r") as dosya:
                    lines = dosya.readlines()
                with open("ogrenci_bilgileri.txt", "w") as dosya:
                    for line in lines:
                        if f"tc= {tc_no}" not in line and f"isim= {isim}" not in line and f"soyisim= {soyisim}" not in line:
                            dosya.write(line)
                    messagebox.showinfo("Bilgi", "Kullanıcı başarıyla silindi.")

        silme_penceresi = tk.Toplevel()
        silme_penceresi.title("Kullanıcı Silme")
        silme_penceresi.geometry("300x200+750+350")

        tc_label = tk.Label(silme_penceresi, text="Silinecek TC Kimlik No:")
        tc_label.grid(row=0, column=0, padx=10, pady=5)
        tc_entry = tk.Entry(silme_penceresi)
        tc_entry.grid(row=0, column=1, padx=10, pady=5)

        isim_label = tk.Label(silme_penceresi, text="Silinecek İsim:")
        isim_label.grid(row=1, column=0, padx=10, pady=5)
        isim_entry = tk.Entry(silme_penceresi)
        isim_entry.grid(row=1, column=1, padx=10, pady=5)

        soyisim_label = tk.Label(silme_penceresi, text="Silinecek Soyisim:")
        soyisim_label.grid(row=2, column=0, padx=10, pady=5)
        soyisim_entry = tk.Entry(silme_penceresi)
        soyisim_entry.grid(row=2, column=1, padx=10, pady=5)

        sil_buton = tk.Button(silme_penceresi, text="Sil", command=sil)
        sil_buton.grid(row=3, column=0, columnspan=2, pady=10)


    def gorevli_sil():
        def sil():
            tc_no = tc_entry.get()
            isim = isim_entry.get()
            soyisim = soyisim_entry.get()
            sifre = sifre_entry.get()
            if len(tc_no) != 11 or not tc_no.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir Telefon No giriniz.")
            else:
                with open("görevli_bilgileri.txt", "r") as dosya:
                    lines = dosya.readlines()
                with open("görevli_bilgileri.txt", "w") as dosya:
                    for line in lines:
                        if f"tel= {tc_no}" not in line and f"isim= {isim}" not in line and f"soyisim= {soyisim}" not in line and f"şifre= {sifre}" not in line:
                            dosya.write(line)
                    messagebox.showinfo("Bilgi", "Kullanıcı başarıyla silindi.")

        silme_penceresi = tk.Toplevel()
        silme_penceresi.title("Kullanıcı Silme")
        silme_penceresi.geometry("450x230+750+350")

        tc_label = tk.Label(silme_penceresi, text="Silinecek Telefon No:")
        tc_label.grid(row=0, column=0, padx=10, pady=5)
        tc_entry = tk.Entry(silme_penceresi)
        tc_entry.grid(row=0, column=1, padx=10, pady=5)

        isim_label = tk.Label(silme_penceresi, text="Silinecek İsim:")
        isim_label.grid(row=1, column=0, padx=10, pady=5)
        isim_entry = tk.Entry(silme_penceresi)
        isim_entry.grid(row=1, column=1, padx=10, pady=5)

        soyisim_label = tk.Label(silme_penceresi, text="Silinecek Soyisim:")
        soyisim_label.grid(row=2, column=0, padx=10, pady=5)
        soyisim_entry = tk.Entry(silme_penceresi)
        soyisim_entry.grid(row=2, column=1, padx=10, pady=5)

        sifre_label = tk.Label(silme_penceresi, text="Silinecek Şifre:")
        sifre_label.grid(row=3, column=0, padx=10, pady=5)
        sifre_entry = tk.Entry(silme_penceresi)
        sifre_entry.grid(row=3, column=1, padx=10, pady=5)

        sil_buton = tk.Button(silme_penceresi, text="Sil", command=sil)
        sil_buton.grid(row=4, column=0, columnspan=2, pady=10)

        
    def yonetici_sil():
        def sil():
            tc_no = tc_entry.get()
            isim = isim_entry.get()
            soyisim = soyisim_entry.get()
            sifre = sifre_entry.get()
            if len(tc_no) != 11 or not tc_no.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir Telefon No giriniz.")
            else:
                with open("yönetici_bilgileri.txt", "r") as dosya:
                    lines = dosya.readlines()
                with open("yönetici_bilgileri.txt", "w") as dosya:
                    for line in lines:
                        if f"tel= {tc_no}" not in line and f"isim= {isim}" not in line and f"soyisim= {soyisim}" not in line and f"şifre= {sifre}" not in line:
                            dosya.write(line)
                    messagebox.showinfo("Bilgi", "Kullanıcı başarıyla silindi.")

        silme_penceresi = tk.Toplevel()
        silme_penceresi.title("Kullanıcı Silme")
        silme_penceresi.geometry("450x230+750+350")

        tc_label = tk.Label(silme_penceresi, text="Silinecek Telefon No:")
        tc_label.grid(row=0, column=0, padx=10, pady=5)
        tc_entry = tk.Entry(silme_penceresi)
        tc_entry.grid(row=0, column=1, padx=10, pady=5)

        isim_label = tk.Label(silme_penceresi, text="Silinecek İsim:")
        isim_label.grid(row=1, column=0, padx=10, pady=5)
        isim_entry = tk.Entry(silme_penceresi)
        isim_entry.grid(row=1, column=1, padx=10, pady=5)

        soyisim_label = tk.Label(silme_penceresi, text="Silinecek Soyisim:")
        soyisim_label.grid(row=2, column=0, padx=10, pady=5)
        soyisim_entry = tk.Entry(silme_penceresi)
        soyisim_entry.grid(row=2, column=1, padx=10, pady=5)

        sifre_label = tk.Label(silme_penceresi, text="Silinecek Şifre:")
        sifre_label.grid(row=3, column=0, padx=10, pady=5)
        sifre_entry = tk.Entry(silme_penceresi)
        sifre_entry.grid(row=3, column=1, padx=10, pady=5)

        sil_buton = tk.Button(silme_penceresi, text="Sil", command=sil)
        sil_buton.grid(row=4, column=0, columnspan=2, pady=10)


    
    kullanici_secim_penceresi = tk.Toplevel(pencere)
    kullanici_secim_penceresi.title("Kullanıcı silme")
    kullanici_secim_penceresi.geometry("300x150+750+350")

    secim_var = tk.StringVar()

    ogrenci_buton = tk.Radiobutton(kullanici_secim_penceresi, text="Öğrenci", variable=secim_var, value="ogrenci")
    ogrenci_buton.pack(anchor=tk.W)

    gorevli_buton = tk.Radiobutton(kullanici_secim_penceresi, text="Görevli", variable=secim_var, value="gorevli")
    gorevli_buton.pack(anchor=tk.W)

    yonetici_buton = tk.Radiobutton(kullanici_secim_penceresi, text="Yönetici", variable=secim_var, value="yonetici")
    yonetici_buton.pack(anchor=tk.W)

    def onayla():
        secilen = secim_var.get()
        if secilen == "ogrenci":
            ogrenci_sil()
        elif secilen == "gorevli":
            gorevli_sil()
        elif secilen == "yonetici":
            yonetici_sil()
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir seçim yapın.")

    onay_buton = tk.Button(kullanici_secim_penceresi, text="Onayla", command=onayla)
    onay_buton.pack()



def kitap_guncelle_penceresi():
    def guncelle_buton_tikla():
        # Kullanıcının girdiği bilgileri al
        kitap_adi = kullanici_girisleri[0].get()
        yeni_yazar = kullanici_girisleri[1].get()
        yeni_isbn = kullanici_girisleri[2].get()
        yeni_yayinevi = kullanici_girisleri[3].get()
        yeni_yil = kullanici_girisleri[4].get()
        yeni_sayfa_sayisi = kullanici_girisleri[5].get()
        yeni_dil = kullanici_girisleri[6].get()
        yeni_tur = kullanici_girisleri[7].get()

        # Dosyayı güncelle
        try:
            with open("kutuphane_kitap_listesi.txt", "r+") as dosya:
                satirlar = dosya.readlines()
                dosya.seek(0)
                yeni_satirlar = []
                for satir_index, satir in enumerate(satirlar):
                    if kitap_adi in satir:
                        # Kitap adı eşleştiğinde, yeni bilgileri girilen bilgilerle değiştir
                        yeni_satirlar.append(f"{kitap_adi}\n")
                        yeni_satirlar.append(f"Yazar: {yeni_yazar}\n")
                        yeni_satirlar.append(f"ISBN: {yeni_isbn}\n")
                        yeni_satirlar.append(f"Yayınevi: {yeni_yayinevi}\n")
                        yeni_satirlar.append(f"Yıl: {yeni_yil}\n")
                        yeni_satirlar.append(f"Sayfa Sayısı: {yeni_sayfa_sayisi}\n")
                        yeni_satirlar.append(f"Dil: {yeni_dil}\n")
                        yeni_satirlar.append(f"Tür: {yeni_tur}\n")
                        # Her satırın sonuna bir alt satır ekleyelim
                        yeni_satirlar.append("\n")
                    else:
                        yeni_satirlar.append(satir)
                dosya.seek(0)
                dosya.writelines(yeni_satirlar)
                dosya.truncate()
            messagebox.showinfo("Başarılı", "Kitap bilgileri başarıyla güncellendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {e}")


    guncelle_pencere = tk.Toplevel()
    guncelle_pencere.title("Kitap Güncelle")

    ekleme_etiketleri = ["Güncellemek istediğiniz kitap adını yazınız:", "Yeni yazar adı giriniz:",
                         "Yeni ISBN numarası giriniz:", "Yeni yayın evi giriniz:",
                         "Yeni yıl giriniz:", "Yeni Sayfa Sayısı giriniz:", "Yeni Dil giriniz:",
                         "Yeni Tür giriniz:"]
    kullanici_girisleri = []

    for etiket_metni in ekleme_etiketleri:
        etiket = tk.Label(guncelle_pencere, text=etiket_metni)
        etiket.pack()

        kullanici_giris = tk.Entry(guncelle_pencere)
        kullanici_giris.pack()

        kullanici_girisleri.append(kullanici_giris)

    guncelle_buton = tk.Button(guncelle_pencere, text="Güncelle", command=guncelle_buton_tikla)
    guncelle_buton.pack()



def odunc_iade():
    def iade_et():
        kitap_isim = iade_et_kitap.get()

        with open("ödünç_alanlar.txt", "r") as odunc_dosya:
            odunc_satirlar = odunc_dosya.readlines()

        yeni_odunc_listesi = []
        kitap_bulundu = False

        i = 0
        while i < len(odunc_satirlar):
            if kitap_isim.lower() in odunc_satirlar[i].lower():
                # Kitap bulunduğunda, kitap adı, ödünç alan kişi, veriliş tarihi ve alış tarihini sil.
                i += 4  # Bir sonraki kitabın adına geç
                kitap_bulundu = True
                continue
            yeni_odunc_listesi.append(odunc_satirlar[i])
            i += 1

        if not kitap_bulundu:
            messagebox.showerror("Hata", f"{kitap_isim} kitabı ödünç alınmamış.")
        else:
            with open("ödünç_alanlar.txt", "w") as odunc_dosya:
                for satir in yeni_odunc_listesi:
                    odunc_dosya.write(satir)

            messagebox.showinfo("Başarılı", f"{kitap_isim} kitabı iade edildi.")

    iade_et_pencere = tk.Toplevel()
    iade_et_pencere.title("Kitap İade Et")

    kitap_ismi_etiket = tk.Label(iade_et_pencere, text="Kitap adı:")
    kitap_ismi_etiket.pack()

    iade_et_kitap = tk.Entry(iade_et_pencere)
    iade_et_kitap.pack()

    iade_et_buton = tk.Button(iade_et_pencere, text="İade Et", command=iade_et)
    iade_et_buton.pack()


def oneri_sikayet():
    # Yeni öneri veya şikayeti almak için bir pencere oluşturuyoruz
    pencere = tk.Tk()
    pencere.title("Öneri ve Şikayet")

    def onayla():
        yeni_oneri_sikayet = metin_alani.get("1.0", "end-1c")  # Metin kutusundaki veriyi al
        with open("öneri_şikayet.txt", "a") as dosya:
            dosya.write(f"öneri/şikayet={yeni_oneri_sikayet}\n")
        pencere.destroy()  # Pencereyi kapat

    etiket = tk.Label(pencere, text="Öneri veya şikayetinizi girin:")
    etiket.pack()

    metin_alani = tk.Text(pencere, height=5, width=30)
    metin_alani.pack()

    onay_butonu = tk.Button(pencere, text="Onayla", command=onayla)
    onay_butonu.pack()

    pencere.mainloop()



def ogrenci_giris():
    ogrenci_pencere = tk.Toplevel(pencere)
    ogrenci_pencere.title("Öğrenci Paneli")
    ogrenci_pencere.geometry("700x530")

    # Arkaplan resmini yükle
    arkaplan_resmi = Image.open("bakircay_logo2.png")
    arkaplan_resmi = arkaplan_resmi.resize((200, 250))  # Pencere boyutuna uyacak şekilde boyutlandır

    # Resmi tkinter PhotoImage formatına dönüştür
    arkaplan_resmi_tk = ImageTk.PhotoImage(arkaplan_resmi)

    # Arkaplan resmi için bir Label oluştur ve pencereye yerleştir
    arkaplan_etiketi = tk.Label(ogrenci_pencere, image=arkaplan_resmi_tk, bg="#303030")
    arkaplan_etiketi.place(x=0, y=0, relwidth=1, relheight=1)

    button1 = tk.Button(ogrenci_pencere, text="Kitap Ara       ", image=kitap_ara_buton, command=arama_penceresi, bg="#0D67A2", compound="left")
    button1.place(x=40, y=30) 

    button8 = tk.Button(ogrenci_pencere, text="Kitap iade        ", image=kitap_iade_logo, command=odunc_iade, bg="#0D67A2", compound="right")
    button8.place(x=430, y=30)

    button6 = tk.Button(ogrenci_pencere, text="Kitap listesi      ", image=buton_resim5, command=txt_dosyayi_ac, bg="#0D67A2", compound="right")
    button6.place(x=430, y=410)

    button_oneri_sikayet=tk.Button(ogrenci_pencere, text="öneri-şikayet", image=oneri_logo, command=oneri_sikayet, bg="#0D67A2", compound="left")
    button_oneri_sikayet.place(x=40,y=410)


    # Pencereyi göster
    ogrenci_pencere.mainloop()



def gorevli_giris():
    gorevli_pencere = tk.Toplevel(pencere)
    gorevli_pencere.title("Görevli Paneli")
    gorevli_pencere.geometry("840x520")
    gorevli_pencere.resizable(width=False, height=False)

    # Arkaplan resmini yükle
    arkaplan_resmi = Image.open("bakircay_logo2.png")
    arkaplan_resmi = arkaplan_resmi.resize((200, 250))  # Pencere boyutuna uyacak şekilde boyutlandır

    # Resmi tkinter PhotoImage formatına dönüştür
    arkaplan_resmi_tk = ImageTk.PhotoImage(arkaplan_resmi)

    # Arkaplan resmi için bir Label oluştur ve pencereye yerleştir
    arkaplan_etiketi = tk.Label(gorevli_pencere, image=arkaplan_resmi_tk, bg="#303030")
    arkaplan_etiketi.place(x=0, y=0, relwidth=1, relheight=1)


    button2 = tk.Button(gorevli_pencere,text="Kitap ekle        ", image=kitap_ekle_buton, command=kitap_ekle_penceresi, bg="#0D67A2", compound="left")
    button2.place(x=560, y=30)

    button3 = tk.Button(gorevli_pencere,text="Kitap sil            ", image=kitap_sil_buton, command=kitap_silme_penceresi, bg="#0D67A2", compound="left")
    button3.place(x=560, y=150)

    buton4=tk.Button(gorevli_pencere,text="kitap güncelle",image=kitap_bilgi_guncelle_logo, command=kitap_guncelle_penceresi, bg="#0D67A2", compound="left")
    buton4.place(x=560,y=270)

    button5 = tk.Button(gorevli_pencere,text="Ödünç ver   ", image=odunc_ver_buton, command=kitap_odunc_ver, bg="#0D67A2", compound="left")
    button5.place(x=40, y=390)

    button7 = tk.Button(gorevli_pencere,text="Ödünç listesi   ", image=buton_resim6, command=odunc_kitaplari_goster, bg="#0D67A2", compound="left")
    button7.place(x=560, y=390)

    #sonra diğer öğrenci ortak fonksiyonlar

    button1 = tk.Button(gorevli_pencere, text="Kitap Ara     ", image=kitap_ara_buton, command=arama_penceresi, bg="#0D67A2", compound="left")
    button1.place(x=40, y=30) 

    button8 = tk.Button(gorevli_pencere, text="Kitap iade   ", image=kitap_iade_logo, command=odunc_iade, bg="#0D67A2", compound="left")
    button8.place(x=40, y=150)

    button6 = tk.Button(gorevli_pencere, text="Kitap listesi", image=buton_resim5, command=txt_dosyayi_ac, bg="#0D67A2", compound="left")
    button6.place(x=40, y=270)

    # Pencereyi göster
    gorevli_pencere.mainloop()


def admin_giris():
    admin_pencere = tk.Toplevel(pencere)
    admin_pencere.title("Admin Paneli")
    admin_pencere.geometry("880x650")
    admin_pencere.resizable(width=False, height=False)

    # Arkaplan resmini yükle
    arkaplan_resmi = Image.open("bakircay_logo2.png")
    arkaplan_resmi = arkaplan_resmi.resize((200, 250))  # Pencere boyutuna uyacak şekilde boyutlandır

    # Resmi tkinter PhotoImage formatına dönüştür
    arkaplan_resmi_tk = ImageTk.PhotoImage(arkaplan_resmi)

    # Arkaplan resmi için bir Label oluştur ve pencereye yerleştir
    arkaplan_etiketi = tk.Label(admin_pencere, image=arkaplan_resmi_tk, bg="#303030")
    arkaplan_etiketi.place(x=0, y=0, relwidth=1, relheight=1)
    
    #sadece adminin erişebildikleri
    kullanici_buton = tk.Button(admin_pencere,text="Kullanıcı ekle  ", image=kullanici_ekle_logo, command=KullaniciEkleme, bg="#0D67A2", compound="left")
    kullanici_buton.place(x=600, y=510)

    kullanici_sil_buton=tk.Button(admin_pencere,text="Kullanıcı sil",image=kullanici_sil_logo, command=kullanici_sil, bg="#0D67A2", compound="left")
    kullanici_sil_buton.place(x=40,y=510)

    #ve diğer fonksiyonlar
    button2 = tk.Button(admin_pencere,text="Kitap ekle        ", image=kitap_ekle_buton, command=kitap_ekle_penceresi, bg="#0D67A2", compound="left")
    button2.place(x=600, y=30)

    button3 = tk.Button(admin_pencere,text="Kitap sil             ", image=kitap_sil_buton, command=kitap_silme_penceresi, bg="#0D67A2", compound="left")
    button3.place(x=600, y=150)

    buton4=tk.Button(admin_pencere,text="kitap güncelle",image=kitap_bilgi_guncelle_logo, command=kitap_guncelle_penceresi, bg="#0D67A2", compound="left")
    buton4.place(x=600,y=270)


    button5 = tk.Button(admin_pencere,text="Ödünç ver   ", image=odunc_ver_buton, command=kitap_odunc_ver, bg="#0D67A2", compound="left")
    button5.place(x=40, y=390)

    button7 = tk.Button(admin_pencere,text="Ödünç listesi   ", image=buton_resim6, command=odunc_kitaplari_goster, bg="#0D67A2", compound="left")
    button7.place(x=600, y=390)

    button1 = tk.Button(admin_pencere, text="Kitap ara     ", image=kitap_ara_buton, command=arama_penceresi, bg="#0D67A2", compound="left")
    button1.place(x=40, y=30)

    button8 = tk.Button(admin_pencere, text="Kitap iade   ", image=kitap_iade_logo, command=odunc_iade, bg="#0D67A2", compound="left")
    button8.place(x=40, y=150)

    button6 = tk.Button(admin_pencere, text="Kitap listesi", image=buton_resim5, command=txt_dosyayi_ac, bg="#0D67A2", compound="left")
    button6.place(x=40, y=270)

    admin_pencere.mainloop()



def kontrol_et_admin():
    # Kullanıcının girdiği ad ve şifreyi al
    girilen_ad = ad_giris.get()
    girilen_sifre = sifre_giris.get()

    # Yönetici bilgilerini dosyadan oku
    with open("yönetici_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            # Her satırı parçalara ayır ve bilgileri al
            bilgiler = satir.strip().split("=")
            if bilgiler[0] == "isim":
                gorevli_isim = bilgiler[1]
            elif bilgiler[0] == "şifre":
                gorevli_sifre = bilgiler[1]

    # Girilen ad ve şifre yönetici bilgileriyle eşleşiyorsa butonu aktif et
    if girilen_ad == gorevli_isim and girilen_sifre == gorevli_sifre:
        button_admin.config(state="normal")  # Butonu aktif yap
        if robot_secili_deger.get()==1:
            messagebox.showinfo("merhaba",f"hoşgeldin " + girilen_ad)
            admin_giris()
        else:
            messagebox.showwarning("robot kontrol",f"tik'i seçmeyi unutmayın")
    elif robot_secili_deger.get() == 0:
        messagebox.showwarning("robot kontrol",f"tik'i seçmeyi unutmayın")
        robotmuymus=tk.Checkbutton(admin_frame, text="Ben robot değilim",variable=robot_secili_deger, fg="#7D0000")
        robotmuymus.place(x=45,y=210)



    else:
        buton_label2.config(text="Giriş Başarısız")  # Etiket metnini değiştir
        buton_label2.place(x=105,y=330)



def kontrol_et_gorevli():
    # Kullanıcının girdiği ad ve şifreyi al
    girilen_ad = gorevli_ad_giris.get()
    girilen_sifre = gorevli_sifre_giris.get()

    # Yönetici bilgilerini dosyadan oku
    with open("görevli_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            # Her satırı parçalara ayır ve bilgileri al
            bilgiler = satir.strip().split("=")
            if bilgiler[0] == "isim":
                admin_isim = bilgiler[1]
            elif bilgiler[0] == "şifre":
                admin_sifre = bilgiler[1]

    if girilen_ad == admin_isim and girilen_sifre == admin_sifre:
        print("Giriş başarılı")  # Şart sağlandığında bu çıktıyı görmeli
        button_admin.config(state="normal")  # Butonu aktif yap
        buton_label2.config(text="Giriş Başarılı")  # Etiket metnini değiştir
        gorevli_giris()
    else:
        print("Giriş başarısız")  # Şart sağlanmadığında bu çıktıyı görmeli
        buton_label2.config(text="Giriş Başarısız")  # Etiket metnini değiştir





pencere = tk.Tk()
pencere.title("Bakırçay kütüphane sistemi uygulaması")
pencere.geometry("670x520+700+250")
pencere.resizable(width=False, height=False)



# Temayı oluştur
stil = ttk.Style()
stil.theme_create("yeni_tema", parent="clam", settings={
    "TNotebook": {"configure": {"background": "#303030"}},
    "TNotebook.Tab": {"configure": {"padding": [10, 5]}, "map": {"background": [("selected", "#1ABAB0")]}},
})
# Temayı uygula
stil.theme_use("yeni_tema")



# Arka plan resimleri
arka_plan_resmi = tk.PhotoImage(file="bakircay_logo2.png")




kitap_ara_buton = Image.open("kitap_ara.png")
kitap_ara_buton = kitap_ara_buton.resize((85, 70))
kitap_ara_buton = ImageTk.PhotoImage(kitap_ara_buton)

kitap_bilgi_guncelle_logo = Image.open("kitap_bilgi_güncelle.png")
kitap_bilgi_guncelle_logo = kitap_bilgi_guncelle_logo.resize((85, 70))
kitap_bilgi_guncelle_logo = ImageTk.PhotoImage(kitap_bilgi_guncelle_logo)

kullanici_ekle_logo = Image.open("kullanici_ekle.png")
kullanici_ekle_logo = kullanici_ekle_logo.resize((85, 70))
kullanici_ekle_logo = ImageTk.PhotoImage(kullanici_ekle_logo)

kullanici_sil_logo = Image.open("kullanici_sil.png")
kullanici_sil_logo = kullanici_sil_logo.resize((85, 70))
kullanici_sil_logo = ImageTk.PhotoImage(kullanici_sil_logo)

kitap_iade_logo = Image.open("kitap_iade.png")
kitap_iade_logo = kitap_iade_logo.resize((85, 70))
kitap_iade_logo = ImageTk.PhotoImage(kitap_iade_logo)

kitap_ekle_buton = Image.open("kitap_ekle.png")
kitap_ekle_buton = kitap_ekle_buton.resize((85, 70))
kitap_ekle_buton = ImageTk.PhotoImage(kitap_ekle_buton)

kitap_sil_buton = Image.open("kitap_sil.png")
kitap_sil_buton = kitap_sil_buton.resize((85, 70))
kitap_sil_buton = ImageTk.PhotoImage(kitap_sil_buton)

odunc_ver_buton = Image.open("odunc_ver.png")
odunc_ver_buton = odunc_ver_buton.resize((85, 70))
odunc_ver_buton = ImageTk.PhotoImage(odunc_ver_buton)

buton_resim5 = Image.open("buton1.png")
buton_resim5 = buton_resim5.resize((85, 70))
buton_resim5 = ImageTk.PhotoImage(buton_resim5)

buton_resim6 = Image.open("odunc_alanlar.png")
buton_resim6 = buton_resim6.resize((85, 70))
buton_resim6 = ImageTk.PhotoImage(buton_resim6)

ogrenci_logo = Image.open("ogrenci.png")
ogrenci_logo = ogrenci_logo.resize((85, 70))
ogrenci_logo = ImageTk.PhotoImage(ogrenci_logo)

personel_logo = Image.open("personel.png")
personel_logo = personel_logo.resize((85, 70))
personel_logo = ImageTk.PhotoImage(personel_logo)

admin_logo = Image.open("admin.png")
admin_logo = admin_logo.resize((85, 70))
admin_logo = ImageTk.PhotoImage(admin_logo)

oneri_logo = Image.open("oneri.png")
oneri_logo = oneri_logo.resize((85, 70))
oneri_logo = ImageTk.PhotoImage(oneri_logo)






notebook = ttk.Notebook(pencere)
notebook.place(x=10, y=10, width=650, height=500)

# Öğrenci Giriş Sekmesi
ogrenci_frame = tk.Frame(notebook)
notebook.add(ogrenci_frame, text="Öğrenci Giriş")

# Öğrenci frame arka planı
ogrenci_arka_plan = tk.Label(ogrenci_frame, image=arka_plan_resmi, bg="#303030")
ogrenci_arka_plan.place(x=0, y=0, relwidth=1, relheight=1)

#öğrenci giriş butonu
button_ogrenci = tk.Button(ogrenci_frame, text="Öğrenci Girişi", image=ogrenci_logo, command=ogrenci_giris)
button_ogrenci.pack(pady=20)



# Görevli Giriş Sekmesi
gorevli_frame = tk.Frame(notebook)
notebook.add(gorevli_frame, text="Görevli Giriş")

# Görevli frame arka planı
gorevli_arka_plan = tk.Label(gorevli_frame, image=arka_plan_resmi, bg="#303030")
gorevli_arka_plan.place(x=0, y=0, relwidth=1, relheight=1)


gorevli_ad_sor = tk.Label(gorevli_frame, text="Ad:", bg="#8D8E8E")
gorevli_ad_sor.place(x=110,y=50)

gorevli_ad_giris = tk.Entry(gorevli_frame, bg="#5C6463")
gorevli_ad_giris.place(x=30,y=80)

gorevli_sifre_sor = tk.Label(gorevli_frame, text="şifre:", bg="#8D8E8E")
gorevli_sifre_sor.place(x=100,y=130)
gorevli_sifre_giris = tk.Entry(gorevli_frame, bg="#5C6463",show="*")
gorevli_sifre_giris.place(x=30,y=160)


button_gorevli = tk.Button(gorevli_frame, text="Görevli Girişi",image=personel_logo, command=gorevli_giris)
button_gorevli.place(x=80,y=220)
buton_label1=tk.Label(gorevli_frame,text="Giriş")
buton_label1.place(x=105,y=300)

# Butonun komutunu kontrol_et fonksiyonu ile değiştir
button_gorevli.config(command=kontrol_et_gorevli)



# Admin Giriş Sekmesi
admin_frame = tk.Frame(notebook)
notebook.add(admin_frame, text="Admin Giriş")

# Admin frame arka planı
admin_arka_plan = tk.Label(admin_frame, image=arka_plan_resmi, bg="#303030")
admin_arka_plan.place(x=0, y=0, relwidth=1, relheight=1)



admin_ad_sor = tk.Label(admin_frame, text="Ad:", bg="#8D8E8E")
admin_ad_sor.place(x=110,y=50)

ad_giris = tk.Entry(admin_frame, bg="#5C6463")
ad_giris.place(x=30,y=80)

admin_sifre_sor = tk.Label(admin_frame, text="şifre:", bg="#8D8E8E")
admin_sifre_sor.place(x=100,y=130)
sifre_giris = tk.Entry(admin_frame, bg="#5C6463", show="*")
sifre_giris.place(x=30,y=160)

#admin giriş butonu
button_admin = tk.Button(admin_frame, text="Admin Girişi",image=admin_logo, command=admin_giris)
button_admin.place(x=80,y=250)
buton_label2=tk.Label(admin_frame,text="Giriş")
buton_label2.place(x=105,y=330)

# Butonun komutunu kontrol_et fonksiyonu ile değiştir
button_admin.config(command=kontrol_et_admin)

#robotlar_giremez=tk.Label("ben robot değilim")
#robotlar_giremez.pack()

robot_secili_deger=tk.IntVar()

robotmuymus=tk.Checkbutton(admin_frame, text="Ben robot değilim",variable=robot_secili_deger, bg="#8D8E8E")
robotmuymus.place(x=45,y=210)



pencere.mainloop()

