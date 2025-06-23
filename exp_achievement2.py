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

# Cek dan update achievement berdasarkan kondisi
def cek_achievement(achievement, koin, is_developer, menang_event, skor, top_score):
    if koin > 1000:
        achievement.add("💰 AKU KAYA!")
    if menang_event:
        achievement.add("🐐 GOAT!!!!")
    if is_developer:
        achievement.add("🤯 A DEVELOPER!!??")
    if skor > top_score:
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

# Contoh penggunaan
if __name__ == "__main__":
    # Ambil data achievement
    achievement, achievement_guide = data_achievement()

    # Contoh input data
    koin = 1200
    is_developer = True
    menang_event = True
    skor = 950
    top_score = 900

    # Proses dan tampilkan hasil
    cek_achievement(achievement, koin, is_developer, menang_event, skor, top_score)
    tampilkan_achievement(achievement)
    tampilkan_petunjuk(achievement, achievement_guide)
