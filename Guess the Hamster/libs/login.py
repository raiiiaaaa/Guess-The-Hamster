from libs import data
import time

# Fungsi login lengkap
def login():
    while True:
        kesempatan = 3
        while kesempatan > 0:
            print('========== LOGIN ==========')
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            print('========================================')

            if username in data.database and data.database[username] == password:
                print("Login berhasil! Selamat datang,", username)
                if username == 'Rayyuuu':
                    print('Anda login sebagai developer!')
                    data.game_status['is_developer'] = True
                    print('>>>Kamu mendapatkan achievement! 🙌👑 A DEVELOPER❗❗❓❓<<<')
                data.game_status['username'] = username
                return
            else:
                kesempatan -= 1
                print(f"Username atau password salah. Sisa kesempatan: {kesempatan}\n\n")

        print("Login gagal 3 kali. Program dikunci selama 60 detik...\n")
        for i in range(60, 0, -1):
            print(f"Tunggu {i} detik...", end='\r')
            time.sleep(1)
        print("\nSilakan coba login kembali.\n")

def menu_message():
    print (f"\n====== MENU UTAMA ======")
    print (f" 1. Singleplayer ")
    print (f" 2. VS Bot ")
    print (f" 3. Achievement Collections ")
    print (f" 4. PowerUP Shop ")
    print (f" 5. Exit ")
    print (f'=========================')
