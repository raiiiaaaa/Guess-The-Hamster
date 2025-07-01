from libs.login import login, menu_message
from shop.hamster_powerup import PowerUP_shop
from games.hamster_game import play_game
from achievement import achievement_collections

def menu():
    while True:
        menu_message()
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            print("🎮 Selamat datang di Game!!\n")
            play_game()
        elif pilihan == "2":
            achievement_collections()
        elif pilihan == "3":    
            print("🛒 Selamat datang di PowerUP Shop!\n")
            PowerUP_shop()
        elif pilihan == "4":
            print("👋 Terima kasih telah bermain!")
            break
        else:
            print(f"Input tidak valid. pilih sesuai menu!\n")

def main():
    login()
    menu()

if __name__ == '__main__':
    main()
