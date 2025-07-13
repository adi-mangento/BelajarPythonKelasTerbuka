Di hari ke-11 ini, saya belajar perulangan menggunakan for, jadi semisal kita punya alur seperti dibawah

 input
   |
   |<----------Aksi
   |             |
   V             |
Kondisi---true---
   |
 false
   |
   V
akhir program

jadi for itu kyk 
Untuk setiap X dalam Y, lakukan sesuatu sampai kondisinya terpenuhi, jadi ngeloop terus sampai kondisinya terpernuhi
nah bentuk dasarnya
for variabel in kumpulan_data:
     aksi yang mau diulang

contoh
semisal
for i in range(5):
    print("angka ke-", i)

setelah dieksekusi hasilnya
angka ke- 0
angka ke- 1
angka ke- 2
angka ke- 3
angka ke- 4

Nah kalo dia data string contohnya kyk dibawah
for huruf in "bagus":
    print(huruf)
maka hasilnya
b
a
g
u
s

ataupun semisal dia data list 
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print("Saya suka", item)
Saya suka apel
Saya suka jeruk
Saya suka mangga
