"""
Ini adalah demo project pertama dengan python!
"""

# test hello word
# print("Hello World Denny")
# print("Let's learn Fundamental Python")

"""
Semua sintaksis dalam bahasa pemrograman terdiri dari :
1. Sekuential : langkah berurutan
2. Percabangan : langkah melompah jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali / sampai kondisi terpenuhi
"""

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")