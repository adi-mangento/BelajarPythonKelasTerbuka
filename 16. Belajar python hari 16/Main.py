print("""
Operasi Indexing & Slicing
Buat program untuk memanipulasi list data = [10, 20, 30, 40, 50, 60, 70, 80]:
      1. Ambil elemen ke-3 (index 2) dan elemen ke-6 (index 5)
      2. Gabungkan kedua elemen tersebut menjadi list baru hasil
      3. Reverse list hasil
      4. Sisipkan angka 99 di antara kedua elemen hasil
""")
data_angka = [10, 20, 30, 40, 50, 60, 70, 80]
print(data_angka)
elemen3 = data_angka[2]
elemen6 = data_angka[5]
hasil = [elemen3, elemen6]
print(hasil)
hasil.reverse()
print(hasil)
hasil.insert(1, 99)
print(hasil)

print("""
Adu Skill Manipulasi List
Buat program yang:
    1. Menerima input 3 nama (user input)
    2. Simpan dalam list tim_a

Lakukan:
    1. Ubah nama index 1 menjadi "SkuyTeam"
    2. Tambahkan "PlayerX" di index 0
    3. Hapus nama terakhir menggunakan pop()
    4. Tampilkan list akhir dan panjang list
""")

input1=input("Masukan nama kamu yang Pertama = ")
input2=input("Masukan nama kamu yang Pertama = ")
input3=input("Masukan nama kamu yang Pertama = ")

tim_a = [input1, input2, input3]
print(tim_a)
tim_a[0] = "SkuyTeam"
tim_a.insert(0, "PlayerX")
tim_a.pop()
print(tim_a)
panjang_list = len(tim_a)
print(f"Panjang tim = {panjang_list}")

print("""
Diberikan list nilai = [7, 9, 8, 9, 5, 7, 8, 5, 9]:
    1. Hitung jumlah angka 7 dan 9
    2. Urutkan list dari terbesar ke terkecil
    3. Temukan index pertama dari angka 8 setelah diurutkan
""")
nilai = [7, 9, 8, 9, 5, 7, 8, 5, 9]
jumlah_7 = nilai.count(7)
jumlah_9 = nilai.count(9)
print(f"""
Jumlah angka 7 = {jumlah_7}
Jumlah angka 9 = {jumlah_9}
      """)

nilai.sort()
nilai.reverse()
print(nilai)
indexke = nilai.index(8)

print(f"index angka 8 ada di = {indexke}")
print("\n")
print("""
Mission: Merge & Transform
Buat program untuk:
1. Gabungkan 2 list:
    list1 = ["Apel", "Mangga"]  
    list2 = [100, 200]  
    Hasil gabung: ["Apel", 100, "Mangga", 200]
2. Reverse list hasil gabungan
3. Ubah elemen index 1 menjadi "Jeruk"
""")

list1 = ["Apel", "Mangga"]  
list2 = [100, 200]
list1.extend(list2)
print(list1)
list1.reverse()
print(list1)
list1[1] = "Jeruk"
print(list1)

print("\n")
print("""
Challenge: Data Detective
Diberikan list misteri = [11, 25, "???", 42, 15]:
1. Temukan dan hapus elemen "???"
2. Hitung rata-rata angka yang tersisa
3. Sisipkan hasil rata-rata di index 2
4. Urutkan list dari terkecil ke terbesar
""")
misteri = [11, 25, "???", 42, 15]
print(misteri)
misteri.remove("???")
rata2 = (misteri[0]+misteri[1]+misteri[2]+misteri[3])/len(misteri)
misteri.insert(2, rata2)
print(misteri)
misteri.sort()
print(misteri)