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