tahun_lahir = int(input("Masukkan Tahun Kelahiran Anda: "))
harga_tiket = int(input("Masukkan Harga Tiket: "))

usia=int(2023) - int(tahun_lahir)

if (usia >=0 and usia <=4):
    diskon = harga_tiket * 100/100
    setelah_diskon = int(harga_tiket - diskon)
    print("Karena umurmu masih kurang dari 4 tahun, kamu mendapatkan diskon 100%, jadi kamu tidak perlu membayar tiket")
elif (usia >=5 and usia <=11):
    diskon = harga_tiket * 50/100
    setelah_diskon = int(harga_tiket - diskon)
    print("Karena umurmu masih kurang dari 11 tahun, kamu mendapatkan diskon 50%, kamu perlu membayar :",setelah_diskon)
elif usia >= 12:
    print("Karena umurmu sudah lebih dari 12 tahun, maka kamu Tidak mendapatkan diskon")