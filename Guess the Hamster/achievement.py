from libs import data
import main

# Fungsi untuk menyimpan struktur data achievement
def data_achievement():
    achievement = set()
    achievement_guide = {
        "💰 AKU KAYA!": "Dapatkan lebih dari 1000 koin.",
        "🐐 GOAT!!!!": "Menangkan event 1x.",
        "🤯 A DEVELOPER!!??": "Login menggunakan akun developer.",
        "🥇 NAMBA WAN!!": "Skor harus melewati top 1 scoreboard."
    }
    return achievement, achievement_guide

# Cek dan update achievement berdasarkan kondisi langsung dari data.game_status
def cek_achievement(achievement, skor, top_score):
    if data.game_status['koin'] > 50:
        achievement.add("💰 AKU KAYA!")
    if data.game_status['win_event']:
        achievement.add("🐐 GOAT!!!!")
    if data.game_status['is_developer']:
        achievement.add("🤯 A DEVELOPER!!??")
    if data.game_status['skor'] > top_score:
        achievement.add("🥇 NAMBA WAN!!")

# Menampilkan achievement yang telah diraih
def tampilkan_achievement(achievement):
    print("\n📜 KOLEKSI ACHIEVEMENT:")
    if not achievement:
        print("Belum ada achievement yang diraih.")
    else:
        for a in achievement:
            print(f"- {a}")

# Menampilkan petunjuk achievement yang belum diraih
def tampilkan_petunjuk(achievement, achievement_guide):
    print("\n📌 PETUNJUK MENDAPATKAN ACHIEVEMENT:")
    belum_didapat = False
    for nama, petunjuk in achievement_guide.items():
        if nama not in achievement:
            print(f"- {petunjuk}")
            belum_didapat = True
    if not belum_didapat:
        print("Semua achievement telah didapatkan!")

def achievement_collections():
    skor = 950          # contoh skor pengguna
    top_score = 900     # contoh skor tertinggi

    # Inisialisasi achievement & panduannya
    achievement_set, achievement_guide = data_achievement()

    # Proses pengecekan achievement berdasarkan status
    cek_achievement(achievement_set, skor, top_score)

    # Tampilkan koleksi & panduan
    tampilkan_achievement(achievement_set)
    tampilkan_petunjuk(achievement_set, achievement_guide)

    input("\nTekan Enter untuk kembali ke menu...")
    main.menu()
