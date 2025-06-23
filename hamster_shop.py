import random
import main

# Data pemain
player_coins = 100
power_ups = {
    "auto_catching": 0,
    "double_points": 0,
    "fifty_fifty": 0
}

def PowerUP_shop():
    print("=== POWER UP SHOP ===")
    print(f"Koin Anda: {player_coins}")
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
        PowerUP_buy("auto_catching", 50)
    elif pilihan == "2":
        PowerUP_buy("double_points", 30)
    elif pilihan == "3":
        PowerUP_buy("fifty_fifty", 40)
    elif pilihan == "0":
        main.menu()
    else:
        print("Pilihan tidak valid!")
        PowerUP_shop()

def PowerUP_buy(nama, harga):
    global player_coins
    
    if player_coins >= harga:
        player_coins -= harga
        power_ups[nama] += 1
        print(f"Berhasil membeli {nama}!")
        print(f"Sisa koin: {player_coins}")
    else:
        print("Koin tidak cukup!")
    PowerUP_shop()
 
def auto_catch(posisi_hamster):
    if power_ups["auto_catching"] > 0:
        power_ups["auto_catching"] -= 1
        print(f"Auto Catching digunakan!")
        print(f"Hamster ditemukan di posisi {posisi_hamster}!")
        return True
    return False

def double_point():
    if power_ups["double_points"] > 0:
        power_ups["double_points"] -= 1
        print("2X Points diaktifkan!")
        print("Hati-hati: Poin hangus jika salah!")
        return True
    return False

def fifty_fifty(posisi_hamster):
    if power_ups["fifty_fifty"] > 0:
        power_ups["fifty_fifty"] -= 1
        print("Fifty-Fifty digunakan!")
        
        # Pilih 1 posisi random selain posisi hamster
        posisi_lain = [i for i in range(1, 3) if i != posisi_hamster]
        posisi_salah = random.choice(posisi_lain)
        
        # Buat 2 pilihan: hamster + 1 posisi salah
        pilihan_tersisa = [posisi_hamster, posisi_salah]
        pilihan_tersisa.sort()
        
        print(f"Pilihan tersisa: {pilihan_tersisa}")
        print("50-50 chance! Satu benar, satu salah!")
        return pilihan_tersisa
    return None

# PowerUP_shop()