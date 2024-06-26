class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama}: Rp{self.harga:.2f}"


class Pesanan:
    def __init__(self):
        self.item = []

    def tambah_item(self, item):
        self.item.append(item)

    def hitung_total(self):
        return sum(item.harga for item in self.item)

    def __str__(self):
        ringkasan_pesanan = "\n".join(str(item) for item in self.item)
        total_harga = self.hitung_total()
        return f"Ringkasan Pesanan:\n{ringkasan_pesanan}\nTotal: Rp{total_harga:.2f}"


class Restoran:
    def __init__(self, nama):
        self.nama = nama
        self.menu = []

    def tambah_item_menu(self, item):
        self.menu.append(item)

    def tampilkan_menu(self):
        for idx, item in enumerate(self.menu, start=1):
            print(f"{idx}. {item}")

    def get_item_menu(self, indeks):
        if 0 <= indeks < len(self.menu):
            return self.menu[indeks]
        else:
            return None


def main():
    # Membuat restoran dan item menu
    restoran = Restoran("Makanan Lezat")
    restoran.tambah_item_menu(MenuItem("Burger", 25000))
    restoran.tambah_item_menu(MenuItem("Pizza", 50000))
    restoran.tambah_item_menu(MenuItem("Salad", 30000))

    # Membuat pesanan
    pesanan = Pesanan()

    # Menampilkan menu dan menerima pesanan
    while True:
        print(f"\nSelamat Datang di {restoran.nama}")
        restoran.tampilkan_menu()
        
        pilihan = input("Masukkan nomor item menu untuk ditambahkan ke pesanan Anda (atau 'q' untuk keluar): ")
        if pilihan.lower() == 'q':
            break

        try:
            indeks_item = int(pilihan) - 1
            item_menu = restoran.get_item_menu(indeks_item)
            if item_menu:
                pesanan.tambah_item(item_menu)
                print(f"{item_menu.nama} telah ditambahkan ke pesanan Anda.")
            else:
                print("Nomor item menu tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

    # Menampilkan ringkasan pesanan
    print("\nPesanan Anda:")
    print(pesanan)


if __name__ == "__main__":
    main()