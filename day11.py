class Karyawan:
    def __init__(self, nama, id_karyawan, jabatan, gaji):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.jabatan = jabatan
        self.gaji = gaji
    
    def tampilkan_info(self):
        """Menampilkan informasi karyawan."""
        print(f"Nama: {self.nama}, ID Karyawan: {self.id_karyawan}, Jabatan: {self.jabatan}, Gaji: {self.gaji}")
    
    def naikkan_gaji(self, persentase):
        """Menaikkan gaji karyawan berdasarkan persentase yang diberikan."""
        kenaikan = self.gaji * (persentase / 100)
        self.gaji += kenaikan
        print(f"Gaji {self.nama} naik sebesar {persentase}%. Gaji baru: {self.gaji}")

class Perusahaan:
    def __init__(self, nama_perusahaan):
        self.nama_perusahaan = nama_perusahaan
        self.karyawan_karyawan = []
    
    def tambah_karyawan(self, karyawan):
        """Menambahkan karyawan ke dalam perusahaan."""
        self.karyawan_karyawan.append(karyawan)
        print(f"Karyawan {karyawan.nama} ditambahkan ke perusahaan.")
    
    def tampilkan_semua_karyawan(self):
        """Menampilkan semua karyawan di perusahaan."""
        if not self.karyawan_karyawan:
            print("Tidak ada karyawan di perusahaan.")
        else:
            for karyawan in self.karyawan_karyawan:
                karyawan.tampilkan_info()
    
    def cari_karyawan(self, id_karyawan):
        """Mencari karyawan berdasarkan ID karyawan."""
        for karyawan in self.karyawan_karyawan:
            if karyawan.id_karyawan == id_karyawan:
                return karyawan
        return None
    
# Membuat objek karyawan
karyawan1 = Karyawan("Andi", 101, "Manajer", 10000000)
karyawan2 = Karyawan("Budi", 102, "Staff", 5000000)

# Membuat objek perusahaan
perusahaan = Perusahaan("PT Maju Sejahtera")

# Menambahkan karyawan ke perusahaan
perusahaan.tambah_karyawan(karyawan1)
perusahaan.tambah_karyawan(karyawan2)

# Menampilkan semua karyawan di perusahaan
perusahaan.tampilkan_semua_karyawan()

# Mencari karyawan berdasarkan ID
karyawan_dicari = perusahaan.cari_karyawan(101)
if karyawan_dicari:
    karyawan_dicari.tampilkan_info()

# Menaikkan gaji karyawan
karyawan_dicari.naikkan_gaji(10)

# Menampilkan semua karyawan setelah kenaikan gaji
perusahaan.tampilkan_semua_karyawan()