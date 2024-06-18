class Produk:
    def __init__(self, nama, harga, kuantitas):
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

    def get_total_harga(self):
        return self.harga * self.kuantitas

    def __str__(self):
        return f"{self.nama}: Rp{self.harga:,} x {self.kuantitas} = Rp{self.get_total_harga():,}"

class Elektronik(Produk):
    def __init__(self, nama, harga, kuantitas, garansi):
        super().__init__(nama, harga, kuantitas)
        self.garansi = garansi

    def __str__(self):
        return f"Elektronik - {super().__str__()} (Garansi: {self.garansi} tahun)"

class Pakaian(Produk):
    def __init__(self, nama, harga, kuantitas, ukuran, bahan):
        super().__init__(nama, harga, kuantitas)
        self.ukuran = ukuran
        self.bahan = bahan

    def __str__(self):
        return f"Pakaian - {super().__str__()} (Ukuran: {self.ukuran}, Bahan: {self.bahan})"

def main():
    laptop = Elektronik("Laptop", 12000000, 2, 2)
    kaos = Pakaian("Kaos", 50000, 5, "L", "Katun")

    print(laptop)  
    print(kaos)   

 
    laptop.kuantitas += 1
    kaos.kuantitas -= 1

    print(f"Update: {laptop}") 
    print(f"Update: {kaos}")    

if __name__ == "__main__":
    main()