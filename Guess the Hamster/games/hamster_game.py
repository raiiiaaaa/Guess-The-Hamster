import random
from libs import data
pil_python = 0
ws = 0
ls = 0

def event():
    lobang = '|0|'
    lobang_event = [lobang] * 10
    lobang_event1 = lobang_event.copy()
    hamster_event = random.randint(1, 10)
    lobang_event[hamster_event - 1] = '|🐹|'
    lobang_event = ' '.join(lobang_event)
    lobang_event1 = ' '.join(lobang_event1)
    print(f'\n~~~~~~~~~~ HaMSTER EVENT ~~~~~~~~~~')
    print(hamster_event)
    while True:
        try:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'kamu Win Streak 5x! tebak di lubang mana hamster berada?\n{lobang_event1}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            pil = int(input('pilih sesuai menu berikut [1 - 10]: '))

            # VALIDASI INPUTAN PLAYER
            if 1 <= pil <= 10:
                break       # JIKA INPUT SESUAI MENU, PROGRAM BERPINDAH KE PENENTUAN HASIL GAME
            else:
                print("Input tidak valid. pilih sesuai menu!\n")
        except ValueError:  # KODE INI UNTUK MENGHANDLE PYTHON CRASH JIKA INPUTAN ADALAH STRING
            print("Input tidak valid. pilih sesuai menu!\n")

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        
    # PENENTUAN HASIL GAME
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if pil == hamster_event:
        print(f'SELAMAT ANDA MEMENANGKAN EVENT!!\n{lobang_event}\nhamster ada di {hamster_event} dan pilihanmu adalah {pil}')
        print('ANDA MENDAPATKAN 100 KOIN!')
        data.game_status['koin'] += 100

        # PENENTUAN ACHIEVEMENT KEKAYAAN KOIN PLAYER
        if data.game_status['koin'] >= 50:
            if data.game_status['rich_coin'] == False:      # JIKA BERNILAI TRUE, KODE INI TIDAK BERLAKU LAGI
                data.game_status['rich_coin'] = True
                print('>>> Kamu mendapatkan achievement! 🤑💰 AKU KAYA❗ <<<')

        # PENENTUAN ACHIEVEMENT 1x KEMENANGAN EVENT
        if data.game_status['win_event'] == False:
            data.game_status['win_event'] = True
            print('>>> Kamu mendapatkan achievement! 🖐🤠🖐 GOAT🔥 <<<')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    else:
        print(f'maaf anda kalah!\n{lobang_event}\nhamster ada di {hamster_event} dan pilihanmu adalah {pil}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    return data.game_status['koin']     #  MENGEMBALIKAN NILAI DATA KOIN KE DATA PLAYER STATUS



def singleplayer():
    global ws, ls       # MEMASUKKAN DATA VARIABEL KE LOKAL FUNCTION

    while True:
        lobang = '|O|'
        lobang_berderet = [lobang] * 3      # MEMBUAT VARIABEL ARRAY DENGAN NILAI LOBANG X 3
        lobang_kosong = lobang_berderet.copy()      # NILAI VARIABEL DUPLIKAT
        hamster = random.randint(1, 3)         # MENGALOKASIKAN POSISI HAMSTER SECARA RANDOM
        lobang_berderet[hamster - 1] = '|🐹|'   # MEMANIPULASI INDEX DATA DALAM ARRAY DENGAN POSISI HAMSTER
        lobang_berderet = ' '.join(lobang_berderet) # MENGGANTI SISI KURUNG ARRAY DENGAN STRING KOSONG
        lobang_kosong = ' '.join(lobang_kosong)

        # VALIDASI POWERUP INPUT
        while True:
            try:
                print('\n========== GUESS THE HAMSTER ==========')
                print(hamster)
                print(lobang_kosong)
                print(f'''1. auto-catch: {data.game_status['auto_catch']}
2. double-point: {data.game_status['double_point']}
3. fifty-fifty: {data.game_status['fifty_fifty']}
4. keluar''')
                print('========================================')
                pil_power = int(input('ingin gunakan PowerUP? [1 / 2 / 3 / 4]: '))

                if pil_power in [1, 2, 3, 4]:
                    break
                else:
                    print("Input tidak valid. pilih sesuai menu!")
            except ValueError:  # KODE INI UNTUK MENGHANDLE PYTHON CRASH JIKA INPUTAN ADALAH STRING
                print("Input tidak valid. pilih sesuai menu!")
        print('========================================\n')

        # MENGINPUT TEBAKAN PLAYER
        while True:
            try:
                print('\n========================================')
                print(f'''halo {data.game_status['username']}! tebak di lubang mana hamster berada?
{lobang_kosong}''')             # PLAYER MENEBAK POSISI HAMSTER 
                print('========================================')
                pil = int(input('pilih sesuai menu berikut [1 / 2 / 3]: '))
                
                # VALIDASI INPUTAN PLAYER
                if pil in [1, 2, 3]:
                    break       # JIKA INPUT SESUAI MENU, PROGRAM BERPINDAH KE PENENTUAN HASIL GAME
                else:
                    print("Input tidak valid. pilih sesuai menu!\n")
            except ValueError:      # KODE INI UNTUK MENGHANDLE PYTHON CRASH JIKA INPUTAN ADALAH STRING
                print("Input tidak valid. pilih sesuai menu!\n")
        print('========================================\n')

        # PENENTUAN HASIL GAME
        print('\n========================================')
        if pil == hamster:
            print(f'selamat anda menang!\n{lobang_berderet}\nhamster ada di {hamster} dan pilihanmu adalah {pil}')
            data.game_status['koin'] += 10
            ws += 1
            ls = 0

        # TRIGGER EVENT 5X WIN STREAK
            if ws == 1:
                data.game_status['koin'] = event()
                ws = 0

            # PENENTUAN ACHIEVEMENT KEKAYAAN KOIN PLAYER
            if data.game_status['koin'] >= 50:
                if data.game_status['rich_coin'] == False:      # JIKA BERNILAI TRUE, KODE INI TIDAK BERLAKU LAGI
                    data.game_status['rich_coin'] = True
                    print('>>> Kamu mendapatkan achievement! 🤑💰 AKU KAYA❗ <<<')

            print('========================================\n')

        else:
            print(f'maaf anda kalah!\n{lobang_berderet}\nhamster ada di {hamster} dan pilihanmu adalah {pil}')
            print(ls)
            print(data.game_status['5lose_streak'])
            if not data.game_status['5lose_streak']:
                ls += 1
            print('========================================\n')
            
        # PENENTUAN ACHIEVEMENT 5X LOSE STREAK
        if ls == 5:
            if data.game_status['5lose_streak'] == False:       # JIKA BERNILAI TRUE, KODE INI TIDAK BERLAKU LAGI
                data.game_status['5lose_streak'] = True
                print('''>>> Kamu mendapatkan achievement! 💪😉 DON'T WORRY, YOU'RE THE STRONGEST❗❗ <<<''')


        # VALIDASI KELANJUTAN BERMAIN
        print(f'Koin saat ini: {data.game_status["koin"]}')
        mainlagi = input('kamu mau main lagi? [y / n]: ')

        # MEMVALIDASI INPUTAN MENU
        while mainlagi.lower() not in ['y', 'n']:   # MENGUBAH INPUTAN UPPERCASE MENJADI LOWERCASE
            mainlagi = input('kesalahan input! tolong pilih sesuai pilihan! [y / n]: ')
        if mainlagi.lower() == 'n':
            return          # JIKA MEMILIH N/n, PROGRAM KEMBALI KE MENU


# def vs_bot():
    global ws, ls, pil_python

    while True:
        pil_python = random.randint(1, 3)
        lobang = '|O|'
        lobang_berderet = [lobang] * 3
        lobang_kosong = lobang_berderet.copy()
        hamster = random.randint(1, 3)
        lobang_berderet[hamster - 1] = '|🐹|'
        lobang_berderet = ' '.join(lobang_berderet)
        lobang_kosong = ' '.join(lobang_kosong)
        print('===== GUESS THE HAMSTER =====')
        print(hamster)
        print(lobang_kosong)

        # Validasi powerup input
        while True:
            try:
                pil_power = int(input(f'''
1. auto-catch: {data.game_status['auto_catch']}
2. double-point: {data.game_status['double_point']}
3. fifty-fifty: {data.game_status['fifty_fifty']}
4. keluar
ingin gunakan PowerUP? [1 / 2 / 3 / 4]: '''))
                if pil_power in [1, 2, 3, 4]:
                    break
                else:
                    print("Pilih angka 1 sampai 4!")
            except ValueError:
                print("Input tidak valid! Masukkan angka antara 1 sampai 4.")

        print('====================')

        # Validasi input tebakan
        while True:
            try:
                pil = int(input(f'''\nhalo {data.game_status['username']}! tebak di lubang mana hamster berada?
{lobang_kosong}\npilihlah pilihan berikut [1 / 2 / 3]: '''))
                if pil in [1, 2, 3]:
                    break
                else:
                    print("Input hanya boleh 1, 2, atau 3!")
            except ValueError:
                print("Input tidak valid! Masukkan angka 1, 2, atau 3.")

        if pil == hamster:
            if pil == pil_python:
                print()
            print(f'\nselamat anda menang!\n{lobang_berderet}\nhamster ada di {hamster}\npilihan python adalah {pil_python} dan pilihanmu {pil}')
            data.game_status['koin'] += 10
            ws += 1
        else:
            print(f'\nmaaf anda kalah!\n{lobang_berderet}\nhamster ada di {hamster}\npilihan python adalah {pil_python} dan pilihanmu {pil}')

        # trigger event
        if ws == 1:
            data.game_status['koin'] = event()
            ws = 0

        # lanjut main?
        print(f'\nKoin saat ini: {data.game_status["koin"]}')
        mainlagi = input('kamu mau main lagi? [y / n]: ')
        while mainlagi.lower() not in ['y', 'n']:
            mainlagi = input('Input tidak valid. pilih sesuai menu! [y / n]: ')
        if mainlagi.lower() == 'n':
            return
