Di hari 16 ini saya belajar manipulasi dan operasi untuk data list
jadi di list itu ada yang Namanya index
semisal
nama = ["Ucup", "Otong", "Dudung"]
index    0(-3)    1(-2)    2(-1)

jadi index itu data ke-... dari list tersebut semisal kalau index ke 0 berarti datanya Ucup kalau -2 berarti Otong

Nah di list ada operasi untuk mengambil data dari list ini, yaitu variabel[index ke-]
contoh penggunaannya
data_0 = nama[0]
print(f"data pertama (index 0) = {data_0}")

hasilnya adalah
data pertama (index 0) = Ucup

missal
data_terakhir = nama[-1]
print(f"data terakhir = {data_terakhir}")

hasilnya adalah
data terakhir = Dudung

Di list untuk mengambil info jumlah data dalam list menggunakan len(variable list)
contoh
Panjang_data = len(nama)
print(f"panjang data = {Panjang_data}")

Untuk memanipulasi data list ada berbagai cara
semisal kalau mau menambahkan item pada list sesuai posisi, variable.insert(posisi,item yang mau ditambahkan)

nama = ["Ucup", "Otong", "Dudung"]
print(f"data sebelum ditambahkan = {nama}")
data.insert(1, "asep") #disini saya nambahin string Asep di posisi 1
print(f"data sesudah ditambahkan = {nama}")

setelah dieksekusi hasilnya
data sebelum ditambahkan = ['Ucup', 'Otong', 'Dudung']
data sesudah ditambahkan = ['Ucup', 'asep', 'Otong', 'Dudung']

Adapun cara menambah data di akhir list menggunakan variabel list.append(item yg ditambahkan)
nama = ["Ucup", "Otong", "Dudung"]
nama.append("Jajang")
print(nama)

hasilnya adalah 
['Ucup', 'Otong', 'Dudung', 'Jajang']


Dalam manipulasi data list kita bisa menambah list dengan list, variable.extend(data listnya)
semisal
nama = ["Ucup", "Otong", "Dudung"]
data_baru = ["Ujang", "Asep", "Dadang"]

nama.extend(data_baru)

print(nama)
maka hasilnya
["Ucup", "Otong", "Dudung", "Umang", "Asep", "Dadang"]

Dalam manipulasi data list kita bisa merubah data dalam list kita semisal
nama = ["Ucup", "Otong", "Dudung"]
nama[2] = "Michael" #disini kita merubah data index ketiga yaitu Dudung menjadi Michael
print(f"Data rubah = {nama}")

hasilnya adalah 
['Ucup', 'Otong', 'Michael')

Dalam manipulasi data list kita bisa meremove data (menghapus data), semisal:
nama = ["Ucup", "Otong", "Dudung"]
nama.remove("Otong") #disini saya menghapus item Otong dari list, ingat item untuk data string harus sesuai kapitalnya
print(f"data remove = {nama}")
["Ucup", "Dudung"]


Dalam manipulasi data list kita bisa meremove dan mengambil data paling belakang caranya
nama = ['Ucup', 'Otong', 'Michael')
data_akhir = data.pop()
print(f"data hasil pop = {nama}")
print(data_akhir)
nama = ['Ucup', 'Otong']
Michael


lalu semisal saya punya data list angka seperti dibawah:
data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 7, 8, 9, 0]

untuk menghitung jumlah item yang sama didalam menggunakan variabel.count(item)
semisal
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(jumlah_data_4)
print(jumlah_data_3)

hasilnya adalah
2
3

disini jumlah angka 4 ada 2 dan jumlah angka 3 ada 3

Untuk mengambil informasi posisi(index) suatu item dari list menggunakan variable list.index(item yang mau diketahui posisinya)

semisal
nama = ['ucup','dodi','dadang','ujang']
index_dadang = nama.index("dadang")

print(f"Posisi index si dadang = {index_dadang}")

hasilnya adalah 
Posisi index si dadang = 2 

Untuk membuat data list menjadi terurut caranya variabel list.sort()
data_angka = [3, 1, 2, 1]
data_angka.sort()

print(data_angka)
[1, 1, 2, 3]

nah kalau untuk list yang berisi data string dia bakal terurut berdasarkan alfabetnya
nah kalau membalik urutan listnya caranya yaitu
data_angka.reverse()
print(data_angka)

hasilnya
[3, 2, 1, 1]
