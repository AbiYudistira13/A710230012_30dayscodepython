class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")


class Mahasiswa(Orang):
    def __init__(self, nama, umur, tim):
        super().__init__(nama, umur)
        self.tim = tim

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku berada di tim {self.tim}")


class Pekerja(Orang):
    def __init__(self, nama, umur, tempatKerja):
        super().__init__(nama, umur)
        self.tempatKerja = tempatKerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan dan pekerjaanku adalah {self.tempatKerja}")


namaku = Mahasiswa('Abi', 18, 'Pendekar United')
print(namaku.kenalan())

pekerjaanku = Pekerja('Abi', '18', 'Pemain Futsal')
print(pekerjaanku.kenalan())