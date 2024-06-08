class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"{self.nim}")
        print(f"{self.nama}")
        print(f"{self.angkatan}")
        print(f"{self.prodi}")

    def selamat(self):
        print(f"Selamat datang {self.nama} di kampus UMS.")

data = Mahasiswa("A710230012", "Abi Yudistira", "2023", "Pendidikan Teknik Informatika")

data.kartu_mahasiswa()
data.selamat()