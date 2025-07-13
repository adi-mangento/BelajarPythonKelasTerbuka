Di hari kedua saya belajar variabel, tipe data, konversi tipe data (casting tipe data), mengambil input data dari user, operasi aritmatika

Variabel
- Dalam variabel tidak boleh ada spasi seperti "nilai y=", bolehnya nilai_Y atau nilaiZ
- Dalam variabel tidak boleh angka didepan Huruf seperti "10juta", bolehnya Juta10 atau a10juta
- Dalam variabel, jika di baris pertama semisal a= 10 kemudian di print(a) maka yang keluar 10, jika setelah print(a)
  dibarisnya berikut a menjadi a=7 , kemudian di baris berikutnya print(a), maka yang keluar
  10
  7


Tipe Data
untuk mengetahui tipe data suatu variabel yaitu type(variabel_data_kamu)
di python ada beberapa tipe data:
	- data integer (int), seperti 1, 2, dst. 
	- data float (float), seperti 1.5; 1.4; dst. bilangan desimal bisa dibilang. Tipe data seperti double seperti di kebanyakan program lain itu gk ada, disini masuknya ke data float
	- data string (str), seperti "makan" "minum". kumpulan karakter bisa huruf atau angka, text bisa dibilang
	- data boolean (bool), tipe data biner, nilainya cuman True atau false

kemudian tipe data khusus:
Bilangan kompleks, complex(angka real,Imajiner), complex ini equivalen dengan (real+imajiner*j) semisal kita print complex(5,6) maka hasilnya (5+6j), j-nya itu imajiner

kemudian ada tipe data dari bahasa C seperti double dll, untuk menggunakannya di python caranya yaitu: semisal mau menggunakan tipe data double maka caaranya
from ctypes import c_double
c_double(10.5)
maka si 10.5 tipe datanya jadi c double
di ctype tidak hanya c_double, ada c_long; c_char; c_long; dll


Konversi Tipe data  (casting)
Semisal kita punya tipe data integer yaitu a=9, mau kita ubah jadi float
maka perintah float(a) hasilnya jadi 9.0
nah kalau semisal kita ubah bool(a) hasilnnya True, karena a=9, kalau a=0 hasilnya false, karena di bool selain angka 0  itu true cuman 0 aja yang false.

Semisal kita punya data float a=9.7 kemudian diubah menjadi data integer int(a). maka hasilnya 9. karena pembulatannya ke bawah
Nah kalau data boolean seperti True kita ubah jadi int atau float maka hasilnya 1 atau 1.0
Nah kalau data string isinya ada huruh seperti "piring" atau "piring10", diubah jadi int atau float maka hasilnya akan eror, kalau datanya stringnya cuman angka kyk 10, ,maka bisa diubah. Kalau data string semisal a = "piring" "0" "true" atau "false", lalu diubah jadi bool maka hasilnya ada true meskipun tulisannya "False". itu karena data string kalau ada isinya dianggap true. Kalau a ="" ,maka hasilnya false karena kosong

Untuk input data user caranya yaitu
data= input("masukan data:") setelah dirun, di run maka diterminal akan muncul masukan data:, disitu kamu diminta untuk input di terminal. dalam input() data yang dimasukan tipe datanya otomasis berubah menjadi str. kalau mau datanya jadi integer, maka datanya data inputnya di casting menjadi int. nah kalau semisal data boolean yaitu data inputnya casting dulu ke int lalu ke Boolean

operasi aritmatika
+ tambah a+b
- kurang a-b
* kali a*b
/ pembagian, hasilnya otomatis float a/b
** pangkat a**b
$ sisa pembagian atau modulus a$b, misalkan 10 dibagi 3 itu sisanya 1. kalua 11 dibagi 3 sisanya 2, kalua 12 sisanya 0
// floor division, itu hasil bagi dibulatkan kebawah misal 10 dibagi 3 hasilnya 3 bukan 3.3333
dalam Operasi aritmatika ada prioritas perhitungannya
1. ()
2. exponent(pangkat)
3. perkalian, pembagian, modulus, floor division
4. tambah ataupun kurang

