"""
Program Perulangan Membaca buku dengan WHILE sampai paham
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu dan pahami"')
total_jumlah_baca = 0

jumlah_buku_yg_sudah_dibaca_dan_dipahami = 0
print(f' Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yg_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2 :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yg_sudah_dibaca_dan_dipahami == 9:
        print(f'Buku ke {jumlah_buku_yg_sudah_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yg_sudah_dibaca_dan_dipahami = jumlah_buku_yg_sudah_dibaca_dan_dipahami + 1
        print(f'Buku ke {jumlah_buku_yg_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca_dan_dipahami}')
if jumlah_buku_yg_sudah_dibaca_dan_dipahami == jumlah_buku:
    print(f'Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'Bu, tidak semua buku bisa dipahami, '
          f'Budi hanya bisa memahami {jumlah_buku_yg_sudah_dibaca_dan_dipahami} buku')