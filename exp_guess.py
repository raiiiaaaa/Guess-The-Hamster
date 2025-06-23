import random
import main
koin = 0
ws = 0
auto_catch = 0
double_point = 0
fifty_fifty = 0

def event(koin):
    lobang = '|0|'
    lobang_event = [lobang] * 10
    lobang_event1 = lobang_event.copy()
    hamster_event = random.randint(1, 10)
    lobang_event[hamster_event - 1] = '|🐹|'
    lobang_event = ' '.join(lobang_event)
    lobang_event1 = ' '.join(lobang_event1)
    print(f'\n===== HaMSTER EVENT =====')
    print(hamster_event)
    pil = int(input(f'''kamu Win Streak 5x! sekarang tebak di lubang mana hamster berada?
\n{lobang_event1}\npilihlah pilihan berikut [1 - 10]: '''))
    
    while pil > 10:
            pil = int(input(f'''\nInput tidak valid! tolong inputkan sesuai pilihan!
{lobang_event1}\npilihlah pilihan berikut [1 - 10: '''))


    if pil == hamster_event:
        print(f'\nselamat anda memenangkan event!\n{lobang_event}\nhamster ada di {hamster_event} dan pilihanmu adalah {pil}')
        koin += 50
        win_event = True
    else:
        print(f'\nmaaf anda kalah!\n{lobang_event}\nhamster ada di {hamster_event} dan pilihanmu adalah {pil}')
    return koin


# looping ketika pemain memilih melanjutkan bermain
def singleplayer():
    global koin, ws, auto_catch, double_point, fifty_fifty

    while True:
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
        pil_power = int(input(f'''
1. auto-catch: {auto_catch}
2. double-point: {double_point}
3. fifty-fifty: {fifty_fifty}
4. keluar
ingin gunakan PowerUP? [1 / 2 / 3 / 4]: '''))
        print('====================')
        pil = int(input(f'''\nhalo! sekarang tebak di lubang mana hamster berada?
{lobang_kosong}\npilihlah pilihan berikut [1 / 2 / 3]: '''))

    # rekursi jika pemain memilih tidak sesuai pilihan
        while pil not in [1, 2, 3]:
            pil = int(input(f'''\nInput tidak valid! tolong inputkan sesuai pilihan!
{lobang_kosong}\npilihlah pilihan berikut [1 / 2 / 3]: '''))

    # memastikan keyakinan memilih
        if pil == hamster:
            print(f'\nselamat anda menang!\n{lobang_berderet}\nhamster ada di {hamster} dan pilihanmu adalah {pil}')
            koin += 10
            ws += 1
        else:
            print(f'\nmaaf anda kalah!\n{lobang_berderet}\nhamster ada di {hamster} dan pilihanmu adalah {pil}')

        # trigger event
        if ws == 1:
            koin = event(koin)
            ws = 0
            
    # memastikan kelanjutan bermain
        print(f'\nKoin saat ini: {koin}')
        mainlagi = input('kamu mau main lagi? [y / n]: ')
        while mainlagi.lower() not in ['y', 'n']:
            mainlagi = input('kesalahan input! tolong pilih sesuai pilihan! [y / n]: ')
        if mainlagi.lower() == 'n':
            main.menu()