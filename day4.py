kontak = {}
for i in range(1, 6):
    nama = input("Masukkan nama teman ke-{}: ".format(i))
    no_hp = input("Masukkan nomor HP teman ke-{}: ".format(i))
    kontak[nama] = no_hp


kata = "Kontak"


print()
print(kata.center(50))
print()
for no, nama in enumerate(kontak, start=1):
    print("{}. [{}] = [{}]".format(no, nama, kontak[nama]))