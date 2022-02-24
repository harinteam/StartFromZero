daftar_buku = ['Seven Habits', 'How to influence People', 'First thing First']
print('\n# Menampilkan daftar buku dengan format list')
print(daftar_buku)

print('\n# Menampilkan daftar buku list, dengan fungsi for, tampilan jajar ke bawah')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# menggunakan fungsi append untuk menambahkan buku di dalam list
daftar_buku.append('Buku Sakti Hacker')
print('\n# Menampilkan daftar buku yg sudah ditambahkan dgn fungsi append')
for k in range(0, len(daftar_buku)):
    print((daftar_buku[k]))

print('\n# Menampilkan daftar buku dalam list dengan indeks tertentu')
print(daftar_buku[2])
print(daftar_buku[0])
