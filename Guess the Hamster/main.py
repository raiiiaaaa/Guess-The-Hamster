from libs import login, menu_message
from shop import hamster_shop
from games import hamster_game

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
    menu_message()
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        print("🎮 Mode Singleplayer dipilih!\n")
        hamster_game.singleplayer()
    # elif pilihan == "2":
    #     vs_bot()
    # elif pilihan == "3":
    #     achievement_collections()
    elif pilihan == "4":    
        print("🛒 Selamat datang di PowerUP Shop!\n")
        hamster_shop.PowerUP_shop()
    elif pilihan == "5":
        print("👋 Terima kasih telah bermain!")
        exit()
    else:
        print(f"Input tidak valid. Coba lagi!\n")
        menu()

def main():
    login()
    menu()

if __name__ == '__main__':
    main()