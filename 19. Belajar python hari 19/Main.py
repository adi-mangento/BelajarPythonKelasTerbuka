print("\n")
print("Tantangan 1".center(40,"="))
data_list = [7, 3, 5, 7, 2, 3, 5]

data_tuples = tuple(data_list)
data_set = set(data_list)

print(data_list)
print(data_tuples)
print(data_set)

print("\n\n")
print("Tantangan 2".center(40,"="))
print("Operasi Himpunan")
A = {2, 4, 6, 8, 10}
B = {1, 2, 3, 4, 5}
C = {4, 5, 6, 7, 8}

# Gabungan (union) menggabungkan semua elemen dari A dan B, tanpa duplikat.
print(A | B)  # {1, 2, 3, 4, 5, 6, 8, 10}

# Irisan (intersection) Elemen yang ada di kedua set B dan C.
print(B & C)  # {4, 5}

# Selisih (difference) Elemen yang ada di A tapi tidak ada di C.
print(A - C)  # {2, 10}

# Selisih simetris Elemen yang ada di A atau di C, tapi tidak di keduanya.
print(A^C) # {2, 5, 7, 10}