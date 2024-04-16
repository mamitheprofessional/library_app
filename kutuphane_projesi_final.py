import tkinter as tk
from tkinter import messagebox


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
                if kitap_ara in satir.lower():
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
        kitap_adi = kullanıcıdan_al_1.get()
        yazar_adi = kullanıcıdan_al_2.get()
        isbn_numarasi = kullanıcıdan_al_3.get()
        yayin_evi = kullanıcıdan_al_4.get()
        yil = kullanıcıdan_al_5.get()
        sayfa_sayisi = kullanıcıdan_al_6.get()
        dil = kullanıcıdan_al_7.get()
        tur = kullanıcıdan_al_8.get()

        # Kullanıcı girişlerini sözlüğe ekleyin --------------------------burayi düzelt
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


        print("Kitap eklendi:", kitap_adi)
        print("Kütüphane Kitapları:", kutuphane_kitaplari)

        # ekleme işlemi tamamlandığında ekrana yeni bir pencere ile mesaj bastırılsın
        success_pencere = tk.Toplevel()
        success_pencere.title("Başarılı")
        success_label = tk.Label(success_pencere, text="Kitap başarıyla eklendi!")
        success_label.pack()

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


pencere = tk.Tk()
pencere.title("Bakırçay kütüphane sistemi uygulaması")
pencere.geometry("670x520+700+250")
pencere.resizable(width=False, height=False)



arka_plan_resmi = tk.PhotoImage(file="bakircay_logo2.png")
arka_plan_etiket = tk.Label(pencere, image=arka_plan_resmi, bg="#303030")
arka_plan_etiket.place(x=0, y=0, relwidth=1, relheight=1)

button1 = tk.Button(text="Kitap ara", fg="#36426C", bg="#A8A8A8", font="arial", command=arama_penceresi, width=9, height=4)
button1.place(x=40, y=30)
button2=tk.Button(text="Kitap ekle", fg="#36426C", bg="#A8A8A8", font="arial", command=kitap_ekle_penceresi, width=9, height=4)
button2.place(x=500, y=30)
button3=tk.Button(text="Kitap sil", fg="#36426C", bg="#A8A8A8", font="arial", command=kitap_silme_penceresi, width=9, height=4)
button3.place(x=500, y=150)
button4=tk.Button(text="Ödünç ver", fg="#36426C", bg="#A8A8A8", font="arial", command=kitap_odunc_ver, width=9, height=4)
button4.place(x=40, y=150)

button5=tk.Button(text="kitap listesi görüntüle", fg="#36426C", bg="#A8A8A8", font="arial", command=txt_dosyayi_ac, width=24, height=3)
button5.place(x=40, y=390)
button6=tk.Button(text="ödünç alanlar listesini görüntüle", fg="#36426C", bg="#A8A8A8", font="arial", command=odunc_kitaplari_goster, width=24, height=3)
button6.place(x=350, y=390)

pencere.mainloop()


