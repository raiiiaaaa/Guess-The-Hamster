from libs.login import login, menu_message
from shop.hamster_shop import PowerUP_shop
from games.hamster_game import singleplayer, vs_bot
from achievement import achievement_collections

def menu():
    while True:
        menu_message()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            print("🎮 Mode Singleplayer dipilih!\n")
            singleplayer()
        elif pilihan == "2":
            vs_bot()
        elif pilihan == "3":
            achievement_collections()
        elif pilihan == "4":    
            print("🛒 Selamat datang di PowerUP Shop!\n")
            PowerUP_shop()
        elif pilihan == "5":
            print("👋 Terima kasih telah bermain!")
            break
        else:
            print(f"Input tidak valid. Coba lagi!\n")

def main():
    login()
    menu()

if __name__ == '__main__':
    main()
