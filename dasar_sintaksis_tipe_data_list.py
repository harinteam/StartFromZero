book_titles = ['Seven Habits', 'How to influence People', 'First thing First']
print('\n# Menampilkan daftar buku dengan format list')
print(book_titles)

print('\n# Menampilkan daftar buku list, dengan fungsi for, tampilan jajar ke bawah')
for i in range(0, len(book_titles)):
    print(book_titles[i])

print('\n# Menampilkan daftar buku dalam list dengan indeks tertentu')
print(book_titles[2])
print(book_titles[0])

print('\n$ Mencoba isi variabel list dengan tipe data sembarangan')
daftar_campur = [123123, 'oke', 3.02, -313]
for i in range(0, len(daftar_campur)):
    print(daftar_campur[i])

# menggunakan fungsi append untuk menambahkan buku di dalam list
book_titles.append('Buku Sakti Hacker')
print('\n# Menampilkan daftar buku yg sudah ditambahkan dgn fungsi append')
for k in range(0, len(book_titles)):
    print((book_titles[k]))

# Clear List
print('\n# Clear list menggunakan .clear')
book_titles.clear()
for k in range(0, len(book_titles)):
    print((book_titles[k]))

# Ganti Elemen
print('\n# Ganti elemen keempat')
book_titles = ['Atomic Habits', 'First Thing First', 'Ikigai', 'Steve Jobs']
book_titles[3] = 'Seven Habits'
for i in range(0, len(book_titles)):
    print(book_titles[i])

# Ambil Elemen dgn pop
print('\n# Ambil elemen ke 2')
book = book_titles.pop(1)
for i in range(0, len(book_titles)):
    print(book_titles[i])

# Memunculkan elemen yg diambil diatas
print('\n# Munculkan Buku yang diambil tadi di atas')
print(book)

# Pop
print('\n# Pop = mengambil elemen dari paling belakang')
book_titles.pop()
for i in range(0, len(book_titles)):
    print(book_titles[i])

# Uses pop -
print('\n# Menggunakan pop -1')
book_titles = ['Atomic Habits', 'First Thing First', 'Ikigai', 'Steve Jobs']
book_titles.pop(-1)
for i in range (0, len(book_titles)):
    print(book_titles[i])

# Menggunakan perintah del
print('\n# Menggunakan perintah del untuk hapus elemen')
book_titles = ['Atomic Habits', 'First Thing First', 'Ikigai', 'Steve Jobs']
del book_titles[0]
for i in range(0, len(book_titles)):
    print(book_titles[i])

# Perintah del dengan list comprehension
print('\n# Menggunakan perintah del dgn list comprehension')
book_titles = ['Atomic Habits', 'First Thing First', 'Ikigai', 'Steve Jobs']
del book_titles[ : ]
for i in range(0, len(book_titles)):
    print(book_titles[i])

# Perintah del dengan list comprehension start
print('\n# Perintah del dengan list comprehension start')
book_titles = ['Atomic Habits', 'First Thing First', 'Ikigai', 'Steve Jobs']
del book_titles[0:-1] # START : END
for i in range(0, len(book_titles)):
    print(book_titles[i])

# Perintah del dengan list comprehension start
print('\n# Perintah del dengan list comprehension start')
book_titles = ['Atomic Habits', 'First Thing First', 'Ikigai', 'Steve Jobs', 'Origami', 'Hitsimishu']
del book_titles[0::2] # START : END : STEP
for i in range(0, len(book_titles)):
    print(book_titles[i])