class Tiket:
    def __init__(self, harga_dasar):
        self.harga_dasar = harga_dasar

    def hitung_harga(self, jumlah_tiket):
        return self.harga_dasar * jumlah_tiket

class TiketBiasa(Tiket):
    def __init__(self):
        super().__init__(50000) 

class TiketVIP(Tiket):
    def __init__(self):
        super().__init__(75000)  

class TiketGold(Tiket):
    def __init__(self):
        super().__init__(100000) 


def main():
    print('SELAMAT DATANG DI MPL INDONESIA'.center(50))
    print()
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket == 'biasa':
        tiket = TiketBiasa()
    elif jenis_tiket == 'vip':
        tiket = TiketVIP()
    elif jenis_tiket == 'gold':
        tiket = TiketGold()
    else:
        print("Jenis tiket tidak valid")
        return
    


    total_harga = tiket.hitung_harga(jumlah_tiket)
    print("Total Harga Tiket: Rp", total_harga)
    print()
    tunai = int(input("Tunai: "))
    kembalian = tunai - total_harga
    print(f"Kembalian: {kembalian}")
    print()
    print("TERIMAKASIH".center(50))
    print("SELAMAT MENONTON".center(50))

if __name__ == "__main__":
    main()