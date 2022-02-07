"""
dasar perulangan di python ada 2 : for dan while

for : jelas berapa perulangannya

while : tidak jelas berapa perulangan tapi jelas kapan berhentinya

programmer : ada permasalah, disusun penyelesainnya

coding : proses memasukan baris perintah ke komputer dgn bahasa pemrograman yg kita pilih
"""

# Program perulangan membaca buku

jumlah_buku = 17
print('Ibu Berkata : "Baca semua bukumu"')

jumlah_buku_sudah_dibaca = 0
print(f'jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca}')

for jumlah_buku_sudah_dibaca in range (1,jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_sudah_dibaca} sudah dibaca")

print(f'jumlah buku sudah dibaca {jumlah_buku_sudah_dibaca}')