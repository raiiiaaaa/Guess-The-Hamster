from libss import login, menu_message
from hamster_shop import PowerUP_shop
from exp_guess import singleplayer

database = {
    "Rayyuuu": "SevenHamster",
    "Jojo": "ParnoMusic"
}

koin = 0
ws = 0
auto_catch = 0
double_point = 0
fifty_fifty = 0
skor = 0
is_developer = False
win_event = False
    
def menu():
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        print("🎮 Mode Singleplayer dipilih!")
        singleplayer()
    # elif pilihan == "2":
    #     vs_bot()
    # elif pilihan == "3":
    #     achievement_collections()
    elif pilihan == "4":    
        print("🛒 Selamat datang di PowerUP Shop!")
        PowerUP_shop()
    elif pilihan == "5":
        print("👋 Terima kasih telah bermain!")
        exit()
    else:
        print(f"Input tidak valid. Coba lagi.")
        menu()

def main():
    login()
    menu_message()
    menu()



if __name__ == '__main__':
    main()
    # welcome_message()
#     print(success, username, is_developer)