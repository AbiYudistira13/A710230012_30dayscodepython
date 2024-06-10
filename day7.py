jumlah_anak_bebek = int(input("Masukkan jumlah anak bebek : "))
for i in range(jumlah_anak_bebek,0,-1):
    if i ==1:
        print(f'anak bebek turun 1, mati satu tinggal induknya')
    else:
        print(f'anak bebek turun {i}, mati satu tinggal {i-1}')