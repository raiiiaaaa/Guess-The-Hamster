import random
from libs import data
from shop.hamster_powerup import use_auto_catch, use_double_point, use_fifty_fifty

ws = 0
ls = 0
double_point = False

''' EVENT MODE '''
def event():
    lobang = '|0|'
    lobang_event = [lobang] * 10                # LOBANG BERDERET BERJUMLAH 10 DI MODE EVENT
    lobang_event1 = lobang_event.copy()
    hamster_event = random.randint(1, 10)       # MENGALOKASIKAN POSISI HAMSTER MODE EVENT
    lobang_event[hamster_event - 1] = '|🐹|'
    lobang_event = ' '.join(lobang_event)
    lobang_event1 = ' '.join(lobang_event1)
    print(f'\n~~~~~~~~~~ HaMSTER EVENT ~~~~~~~~~~')
    while True:
        try:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'kamu Win Streak 5x! tebak di lubang mana hamster berada?\n{lobang_event1}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            pil = int(input('pilih sesuai menu berikut [1 - 10]: '))

            # VALIDASI INPUTAN PLAYER
            if 1 <= pil <= 10:
                break        # JIKA INPUT SESUAI MENU, PROGRAM BERPINDAH KE PENENTUAN HASIL GAME
            else:
                print("Input tidak valid. pilih sesuai menu!\n")
        except ValueError:     #  KODE INI UNTUK MENGHANDLE PYTHON CRASH JIKA INPUTAN ADALAH STRING
            print("Input tidak valid. pilih sesuai menu!\n")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # PENENTUAN HASIL GAME
    if pil == hamster_event:
        print(f'SELAMAT ANDA MEMENANGKAN EVENT!!\n{lobang_event}\nhamster ada di {hamster_event} dan pilihanmu adalah {pil}')
        print('ANDA MENDAPATKAN 100 KOIN!')
        data.game_status['koin'] += 100

        # PENENTUAN ACHIEVEMENT KEKAYAAN KOIN PLAYER
        if data.game_status['koin'] > 500 and not data.game_status['rich_coin']:
            data.game_status['rich_coin'] = True
            print('>>> Kamu mendapatkan achievement! 🤑💰 AKU KAYA❗ <<<')

        # PENENTUAN ACHIEVEMENT 1x KEMENANGAN EVENT
        if not data.game_status['win_event']:
            data.game_status['win_event'] = True
            print('>>> Kamu mendapatkan achievement! 🕐🤠🕐 GOAT🔥 <<<')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    else:
        print(f'maaf anda kalah!\n{lobang_event}\nhamster ada di {hamster_event} dan pilihanmu adalah {pil}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    return data.game_status['koin']

'''PROGRAM GAME UTAMA '''
def play_game():
    global ws, ls, double_point     # MEMASUKKAN DATA VARIABEL KE LOKAL FUNCTION
    
    ''' MENAMPILAN DERETAN LUBANG '''
    while True:
        lobang = '|O|'
        lobang_berderet = [lobang] * 3  # MEMBUAT VARIABEL ARRAY DENGAN NILAI LOBANG X 3
        lobang_kosong = lobang_berderet.copy()      # NILAI VARIABEL DUPLIKAT
        hamster = random.randint(1, 3)          # MENGALOKASIKAN POSISI HAMSTER SECARA RANDOM
        lobang_berderet[hamster - 1] = '|🐹|'   # MEMANIPULASI INDEX DATA DALAM ARRAY DENGAN POSISI HAMSTER
        lobang_berderet_str = ' '.join(lobang_berderet)     # MENGGANTI SISI KURUNG ARRAY DENGAN STRING KOSONG
        lobang_kosong_str = ' '.join(lobang_kosong)

        ''' INPUT PEMILIHAN POWERUP '''
        while True:
            try:
                print('\n========== GUESS THE HAMSTER ==========')
                print('LIST POWERUP')
                print(hamster)
                print(f'''1. auto-catch: {data.game_status['auto_catch']}
2. double-point: {data.game_status['double_point']}
3. fifty-fifty: {data.game_status['fifty_fifty']}
4. keluar''')
                pil_power = int(input('ingin gunakan PowerUP? [1 / 2 / 3 / 4]: '))
                print('========================================')

                # VALIDASI INPUT POWERUP
                if pil_power in [1, 2, 3, 4]:
                    break
                else:
                    print("Input tidak valid. pilih sesuai menu!")
            except ValueError:      # KODE INI UNTUK MENGHANDLE PYTHON CRASH JIKA INPUTAN ADALAH STRING
                print("Input tidak valid. pilih sesuai menu!")

        ''' MEKANISME POWER UP '''
        hasil_power = None      # VARIABEL UNTUK PENENTUAN HASIL PENGGUNAAN POWERUP

        # AUTO CATCH POWERUP
        if pil_power == 1:
            hasil_power = use_auto_catch(hamster)
            if hasil_power:
                print('========================================')
                print(f'''selamat anda menang!\n{lobang_berderet_str}
hamster ada di {hamster} dan kamu menggunakan Auto Catch!''')
                print('========================================')
                data.game_status['koin'] += hasil_power['bonus']    # PENAMBAHAN DATA KOIN
                ws += 1
                ls = 0
                if ws == 5: # TRIGGER EVENT 5X WIN STREAK
                    data.game_status['koin'] = event()
                    ws = 0
                print(f'Koin saat ini: {data.game_status["koin"]}')
                print(f'Win Streak saat ini: {ws}')
                
                # VALIDASI KELANJUTAN BERMAIN
                mainlagi = input('kamu mau main lagi? [y / n]: ')
                print('========================================')
                while mainlagi.lower() not in ['y', 'n']:
                    mainlagi = input('kesalahan input! tolong pilih sesuai pilihan! [y / n]: ')
                if mainlagi.lower() == 'n':
                    return          # PROGRAM KEMBALI KE MENU
                else:
                    continue        # PROGRAM GAME BERLANJUT

        # DOUBLE POINT POWERUP
        elif pil_power == 2:        
            if data.game_status['double_point'] > 0:
                double_point = True     # VARIABEL UNTUK MEMANGGIL FUNCTION DOUBLE POINT
                print("\n🔥 Double Point digunakan!\n⚠️ Hati-hati: Jika salah, Double Point gugur!")
            else:
                print("PowerUP anda kosong!\n")

        # FIFTY-FIFTY POWERUP
        elif pil_power == 3:
            pilihan_tersisa = use_fifty_fifty(hamster)
            if pilihan_tersisa:
                print(f"Gunakan pilihan ini: {pilihan_tersisa}")

        ''' MENGINPUT TEBAKAN PLAYER '''
        while True:
            try:
                print('\n========================================')
                print(f'HALO {data.game_status["username"]}! tebak di lubang mana hamster berada?\n{lobang_kosong_str}')
                pil = int(input(f'pilih sesuai menu berikut [1 / 2 / 3]: '))
                print('========================================')

                # VALIDASI INPUTAN PLAYER
                if pil in [1, 2, 3]:
                    break       # JIKA INPUT SESUAI MENU, PROGRAM BERPINDAH KE PENENTUAN HASIL GAME
                else:
                    print("Input tidak valid. pilih sesuai menu!")
            except ValueError:      # KODE INI UNTUK MENGHANDLE PYTHON CRASH JIKA INPUTAN ADALAH STRING
                print("Input tidak valid. pilih sesuai menu!")

        # PEMANGGILAN FUNCTION DOUBLE POINT POWERUP
        if double_point:
            hasil_power = use_double_point(pil, hamster)

        print('\n========================================')

        # PENENTUAN HASIL GAME
        if pil == hamster:
            print(f'selamat anda menang!\n{lobang_berderet_str}\nhamster ada di {hamster} dan pilihanmu adalah {pil}')
            
            # NOTIF POWERUP DOUBLE POINT GUGUR JIKA KALAH
            if hasil_power and hasil_power['powerup'] == 'double_point':
                print("Berkat double point, anda mendapatkan 2x koin!")


            # PENAMBAHAN DATA 2X KOIN
            bonus = hasil_power['bonus'] if hasil_power and hasil_power['powerup'] == 'double_point' else 10
            data.game_status['koin'] += bonus
            ws += 1
            ls = 0

            # TRIGGER EVENT 5X WIN STREAK
            if ws == 5:
                data.game_status['koin'] = event()
                ws = 0
        else:
            print(f'maaf anda kalah!\n{lobang_berderet_str}\nhamster ada di {hamster} dan pilihanmu adalah {pil}')
            ws = 0
            # NOTIF POWERUP DOUBLE POINT GUGUR JIKA KALAH
            if hasil_power and hasil_power['powerup'] == 'double_point':
                print("Sayang sekali, double point hangus karena jawaban salah!")
        print('========================================\n')

        # LOSE STREAK TIDAK AKAN BERTAMBAH JIKA SUDAH DAPAT ACHIEVEMENT
        if not data.game_status['5lose_streak']:
            ls += 1

        # PENENTUAN ACHIEVEMENT KEKAYAAN KOIN PLAYER
        if data.game_status['koin'] > 500 and not data.game_status['rich_coin']:
            data.game_status['rich_coin'] = True
            print('>>> Kamu mendapatkan achievement! 🤑💰 AKU KAYA❗ <<<')

        # PENENTUAN ACHIEVEMENT 5X LOSE STREAK
        if ls == 5 and not data.game_status['5lose_streak']:
            data.game_status['5lose_streak'] = True
            print('''>>> Kamu mendapatkan achievement! 💪😉 DON'T WORRY, YOU'RE THE STRONGEST❗❗ <<<''')

        # VALIDASI KELANJUTAN BERMAIN
        print(f'Koin saat ini: {data.game_status["koin"]}')
        print(f'Win Streak saat ini: {ws}')
        mainlagi = input('kamu mau main lagi? [y / n]: ')

        # MEMVALIDASI INPUTAN MENU
        while mainlagi.lower() not in ['y', 'n']:       # MENGUBAH INPUTAN UPPERCASE MENJADI LOWERCASE
            mainlagi = input('Input tidak valid. pilih sesuai menu! [y / n]: ')
        if mainlagi.lower() == 'n':
            return          # JIKA MEMILIH N/n, PROGRAM KEMBALI KE MENU
