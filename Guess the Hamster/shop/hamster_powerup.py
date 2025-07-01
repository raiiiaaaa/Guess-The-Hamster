import random
from libs import data

__all__ = ['PowerUP_shop', 'use_auto_catch', 'use_double_point', 'use_fifty_fifty']

def PowerUP_shop():
    print("=== POWER UP SHOP ===")
    print(f"Koin Anda: {data.game_status['koin']}")
    print("1. Auto Catch - 50 koin")
    print("   (Menangkap hamster secara otomatis)")
    print("2. Double Point - 10 koin") 
    print("   (Double poin jika benar, hangus jika salah)")
    print("3. Fifty-fifty - 40 koin")
    print("   (Memberikan 2 pilihan : 1 benar & 1 salah)")
    print("4. Kembali")
    print('==============================')

    pilihan = input("Beli power up (1-4): ")

    if pilihan == "1":
        PowerUP_buy("auto_catch", 50)
    elif pilihan == "2":
        PowerUP_buy("double_point", 10)
    elif pilihan == "3":
        PowerUP_buy("fifty_fifty", 40)
    elif pilihan == "4":
        return
    else:
        print(f"Input tidak valid. Coba lagi!\n")
        PowerUP_shop()

def PowerUP_buy(nama, harga):
    if data.game_status['koin'] >= harga:
        data.game_status['koin'] -= harga
        data.game_status[nama] += 1
        print(f"Berhasil membeli {nama.replace('_', ' ').title()}!")
    else:
        print("Koin tidak cukup!")
    PowerUP_shop()

def use_auto_catch(hamster_pos):
    """Langsung menang, mengurangi power-up, dan return hasil menang"""
    if data.game_status["auto_catch"] > 0:
        data.game_status["auto_catch"] -= 1
        print(f"\n🧲 Auto Catch digunakan! Hamster otomatis tertangkap di lubang {hamster_pos}!")
        return {
            'status': 'win',
            'powerup': 'auto_catch',
            'hamster': hamster_pos,
            'bonus': 10
        }
    else:
        print('PowerUP anda kosong!\n')
    return None

def use_double_point(player_choice, hamster_pos):
    """Gandakan skor jika benar, hangus jika salah"""
    if data.game_status["double_point"] > 0:
        data.game_status["double_point"] -= 1
        if player_choice == hamster_pos:
            return {
                'status': 'win',
                'powerup': 'double_point',
                'bonus': 20
            }
        else:
            return {
                'status': 'lose',
                'powerup': 'double_point',
                'bonus': 0
            }
    return None

def use_fifty_fifty(hamster_pos):
    """Tampilkan 1 jawaban benar dan 1 salah"""
    if data.game_status["fifty_fifty"] > 0:
        data.game_status["fifty_fifty"] -= 1
        print("\n🎰 Fifty-Fifty digunakan!")

        opsi = [1, 2, 3]
        opsi.remove(hamster_pos)
        pilihan_salah = random.choice(opsi)

        pilihan = [hamster_pos, pilihan_salah]
        pilihan.sort()
        print(f"Pilihan tersisa: {pilihan} (1 berisi, 1 kosong!)")
        return pilihan
    else:
        print('PowerUP anda kosong!\n')
    return None
