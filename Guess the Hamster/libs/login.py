from libs import data
import time

# Database akun
database = {
    "Rayyuuu": "SevenHamster",
    "Jojo": "ParnoMusic"
}

# Fungsi login lengkap
def login():
    while True:
        kesempatan = 3
        while kesempatan > 0:
            print('===== LOGIN =====')
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            if username in database and database[username] == password:
                print("Login berhasil! Selamat datang,", username)
                if username == 'Rayyuuu':
                    print('Anda login sebagai developer!')
                    data.game_status['is_developer'] = True
                    return True, username, True  # login sukses, nama, developer=True
                return True, username, False  # login sukses, nama, developer=False
            else:
                kesempatan -= 1
                print(f"Username atau password salah. Sisa kesempatan: {kesempatan}\n")

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

# Contoh penggunaan
if __name__ == '__main__':
    success, username, is_developer = login()
    menu_message()
    
    # Di sini kamu bisa lanjutkan ke menu atau logika berikutnya