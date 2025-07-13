Di hari 17 ini saya belajar mengenai Teknik menduplikat list, Nested List, looping list
semisal kita punya data
a = \["ucup", "otong", "dudung"]
print(f"a = {a}")

\#lalu kita punya list baru
b = a
print(f"b = {b})

hasilnya
a = \["ucup", "otong", "dudung"]
b = \["ucup", "otong", "dudung"]

semisal kita ubah item di list b
b\[1] = Michael

print(f"a = {a}")
print(f"b = {b}")
hasilnya

a = \["ucup", "Michael", "dudung"]
b = \["ucup", "Michael", "dudung"]

bisa dilihat yang juga berubah padahal kita ngeditnya yang b, kenapa begitu? itu dikarenakan
kedua addres a dan b itu sama,
bisa dilihat dengan menjalan)
print(hex(id(a))
print(hex(id(b))

itu hasil eksekusinya address nya sama
nah kalau mau ngeduplikat list, supaya list yang diduplikat itu bisa diedit, address nya harus beda, gk sembarangan hanya dengan a=b. cara duplikat list yaitu dengan .copy()
contoh
c = a.copy()
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

c\[0] = "Dadang"
print("ubah si c")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

hasilnya
a = \["ucup", "Michael", "dudung"]
b = \["ucup", "Michael", "dudung"]
c = \["ucup", "Michael", "dudung"]
ubah si c
a = \["ucup", "Michael", "dudung"]
b = \["ucup", "Michael", "dudung"]
c = \["Dadang", "Michael", "dudung"]

bisa dilihat di hasilnya kalau kita ubah yang c, yang a dan b gk ikut berubah, itu dikarekan a dan b adressnya beda dengan list c



Lalu mengenai Nested List, nested list itu intinya List di dalam list, contohnya
list\_0 = \[1,2]
list\_1 = \[3,4,5]
list\_2 = \[list\_0, list\_1]
print(list\_2)

hasilnya
\[\[1, 2], \[3, 4, 5]]

Trus gunanya nested list ini apa? semisal kita punya list peserta kyk gini
peserta\_a = \["Budi", 4, "Makan"] #Nama, Umur, Hobi
peserta\_b = \["Asep", 32, "Tidur"]
peserta\_c = \["Anton", 23, "Joget"]
list\_peserta = \[peserta\_0, peserta\_b, peserta\_c]

for peserta in list\_peserta:
print(f"Nama \\t: {peserta\[0]}")
print(f"Umur \\t: {peserta\[1]}")
print(f"Hobi \\t: {peserta\[2]}\\n")

hasilnya
Nama	: Budi
Umur	: 4
Hobi	: Makan

Nama	: Asep
Umur	: 32
Hobi	: Tidur

Nama	: Anton
Umur	: 23
Hobi	: Joget



Nah cara untuk mengcopy suatu nested list caranya tidak hanya seperti dibawah
list\_copy = list\_peserta.copy()
print(list\_peserta) #Sebelum
peserta\_a\[0] = "Michael"
print(list\_peserta)
print(list\_copy)

hasilnya
\[\["Budi", 4, "Makan"], \["Asep", 32, "Tidur"], \["Anton", 23, "Joget"]]
\[\["Michael", 4, "Makan"], \["Asep", 32, "Tidur"], \["Anton", 23, "Joget"]]
\[\["Michael", 4, "Makan"], \["Asep", 32, "Tidur"], \["Anton", 23, "Joget"]]

bisa dilihat list\_copy hasilnya sama dengan list\_peserta, nah itu dikarena list peserta\_0 addresnya masih sama.

Sebelum belajar bagaaimana cara copy nested list, kita pahami dulu bagaimana cara mengambil data dari list yang ada di dalam list, contoh
list\_a = \[1,2]
list\_b = \[3,4]
list\_c = \[list\_a, list\_b]
print(list\_c)

data\_a = list\_c\[0]\[0] ###ini ngambil data index ke 0 di list\_a, yang ada di dalem list\_c
print(data\_a)

hasilnya
\[\[1,2], \[3,4]]
1



nah untuk mencopy data list yang ada list di dalam listnya, agar list yang ada didalam list tersebut, Ketika dicopy addressnya berbeda dengan yg aslinya. menggunakan deepcopy. contohnya

from copy import deepcopy #import package deepcopy
data\_2D = \[list\_a, list\_b, 10]
data\_deepcopy = deepcopy(data\_2D)

print(hex(id(data\_2D)))
print(hex(id(data\_deepcopy)))

print(hex(id(data\_2D\[0])))
print(hex(id(data\_deepcopy\[0])))

hasilnya nanti address dari list dan nested list hasil dari deepcopy dgn aslinya, address-nya akan berbeda secara keseluruhan.

Looping dari list
semisal untuk for loop
missal kita punya list
kumpulan\_angka = \[4,3,2,5,6,1]

for angka in kumpulan\_angka: #artinya setiap satu putaran akan mengambil komponen(angka) dari kumpulan angka lalu
print(f"angka = {angka}")
hasilnya
angka = 4
angka = 3
angka = 2
angka = 5
angka = 6
angka = 1



kita bisa juga ngambil berdasarkan indexnya

for loop dan range
semisal
logika dari script dibawah ini gmana ya? saya gk paham
kumpulan\_angka = \[4,3,2,5,6,1]
Panjang = len(kumpulan\_angka) #len dari kumpulan angka hasilnya 6

for i in range(Panjang): #karena Panjang=6 maka range(6) yang mana adalah \[0,1,2,4,5], jadi i-nya ngambil dari range
print(f"angka = {kumpulan\_angka\[i]") #loopingnya berdasarkan range(6)

hasilnya
angka = 4
angka = 3
angka = 2
angka = 5
angka = 6
angka = 1

kita juga bisa looping menggunakan while
semisal
kumpulan\_angka = \[4,3,2,5,6,1]
Panjang = len(kumpulan\_angka) #len dari kumpulan angka hasilnya 6
i = 0

while i < Panjang:
print(f"angka = {kumpulan\_angka\[i]}")
i += 1

hasilnya
angka = 4
angka = 3
angka = 2
angka = 5
angka = 6
angka = 1

Kemudian ada list comprehension
semisal kita punya list
logika script dibawah ini gmana ya
data = \["ucup",1,2,3,"otong"]

\[print(f"data={i}") for i in data]

hasilnya
data=ucup
data=1
data=2
data=3
data=otong

struktur dasar dari list comprehension itu
\[ekspresi for item in iterable if kondisi]

* ekspresi: Operasi/modifikasi pada item (misal: i\*2, i.lower()).
* for item in iterable: Loop untuk mengambil setiap elemen dari data sumber.
* if kondisi (opsional): Filter untuk memilih elemen yang memenuhi syarat.

contoh lain
squared = \[i\*\*2 for i in range(5)]  # Output: \[0, 1, 4, 9, 16]





Lalu ada cara menggunakan enumerate, jadi dia mengambil index dan datanya
contoh


data\_list = \["ucup",1,2,3,"otong"]



for index,data in enumerate(data\_list): #kalo pake enumerate() bisa ngambil data listnya

&nbsp;	print(f"index = {index}, data = {data}")



hasilnya

index = 0 data = ucup
index = 1 data = 1
index = 2 data = 2
index = 3 data = 3
index = 4 data = otong



