def Penjumlahan(x, y):
    return int(x + y)

def Pengurangan(x, y):
    return int(x - y)

def Perkalian(x, y):
    return int(x * y)

def Pembagian(x, y):
    if y == 0:
        return "Kesalahan! Pembagian dengan nol."
    else:
        return int(x / y)
    
def calculator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    while True:
        choice = input("Masukkan pilihan(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Masukkan Angka Pertama: "))
            num2 = float(input("Masukkan Angka Kedua: "))

            if choice == '1':
                print(f"Hasilnya adalah: {Penjumlahan(num1, num2)}")

            elif choice == '2':
                print(f"Hasilnya adalah: {Pengurangan(num1, num2)}")

            elif choice == '3':
                print(f"Hasilnya adalah: {Perkalian(num1, num2)}")

            elif choice == '4':
                print(f"Hasilnya adalah: {Pembagian(num1, num2)}")

            next_calculation = input("Apakah Anda ingin melakukan perhitungan lain? (ya/tidak): ")
            if next_calculation.lower() != 'ya':
                break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    calculator()
