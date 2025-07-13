print("""
List dengan Syarat Unik
Buat list bernama hasil yang berisi:
- Angka dari 1 sampai 30.
- Ganti angka kelipatan 4 dengan string "Empat".
- Ganti angka yang berakhiran 7 (contoh: 7, 17, 27) dengan string "Tujuh".
""")

hasil = list("Empat" if i % 4 == 0 else "Tujuh" if i % 10 == 7 else i for i in range(0,31))
print(hasil)

hasil2= list(i for i in range(0,30) if i % 10 == 7)  #ambil semua i yang berakhiran 7
print(hasil2)