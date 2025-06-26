import random
from libs import data
import main

def PowerUP_shop():
    print("=== POWER UP SHOP ===")
    print(f"Koin Anda: {data.game_status['koin']}")
    print("1. Auto Catching - 50 koin")
    print("   (Menangkap hamster secara otomatis)")
    print("2. 2X!! - 30 koin") 
    print("   (Double poin jika benar, hangus jika salah)")
    print("3. Fifty-fifty - 40 koin")
    print("   (Memberikan 2 pilihan : 1 benar & 1 salah)")
    print("0. Kembali")
    print('==============================')

    pilihan = input("Beli power up (0-3): ")

    if pilihan == "1":
        PowerUP_buy("auto_catch", 50)
    elif pilihan == "2":
        PowerUP_buy("double_point", 30)
    elif pilihan == "3":
        PowerUP_buy("fifty_fifty", 40)
    elif pilihan == "0":
        main.menu()
    else:
        print(f"Input tidak valid. Coba lagi!\n")
        PowerUP_shop()

def PowerUP_buy(nama, harga):
    if data.game_status['koin'] >= harga:
        data.game_status['koin'] -= harga
        data.game_status[nama] += 1
        print(f"Berhasil membeli {nama.replace('_', ' ').title()}!")
        print(f"Sisa koin: {data.game_status['koin']}")
    else:
        print("Koin tidak cukup!")
    PowerUP_shop()

def auto_catch(posisi_hamster):
    if data.game_status["auto_catch"] > 0:
        data.game_status["auto_catch"] -= 1
        print(f"Auto Catch digunakan!")
        print(f"Hamster ditemukan di posisi {posisi_hamster}!")
        return True
    return False

def double_point():
    if data.game_status["double_point"] > 0:
        data.game_status["double_point"] -= 1
        print("2X Points diaktifkan!")
        print("Hati-hati: Poin hangus jika salah!")
        return True
    return False

def fifty_fifty(posisi_hamster):
    if data.game_status["fifty_fifty"] > 0:
        data.game_status["fifty_fifty"] -= 1
        print("Fifty-Fifty digunakan!")

        posisi_lain = [i for i in range(1, 4) if i != posisi_hamster]
        posisi_salah = random.choice(posisi_lain)

        pilihan_tersisa = [posisi_hamster, posisi_salah]
        pilihan_tersisa.sort()

        print(f"Pilihan tersisa: {pilihan_tersisa}")
        print("50-50 chance! Satu benar, satu salah!")
        return pilihan_tersisa
    return None

if __name__ == '__main__':
    PowerUP_shop()
