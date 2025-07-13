Di hari ketiga saya belajar operasi komparasi; operasi logika atau boolean

Operasi komparasi itu untuk bandingkan nilai. Nah hasil dari operasi koomparasi itu adalah Boolean.
	- > lebih besar dari, contoh 9>3 hasilnya adalah true, kalo 3>9 hasilnya false, kalo 2>2 hasilnya false
	- < kurang dari, contoh 3<9 hasilnya adalah true, kalo 9<3 hasilnya false, kalo 2<2 hasilnya false
	- >= lebih dari sama dengan, sama seperti >, tapi kalo nilanya sama seperti 2 >= 2 hasilnya true, batasnya diikuti juga  
	- <= kurang dari sama dengan, sama seperti <, tapi kalo nilanya sama seperti 2 <= 2 hasilnya true, batasnya diikuti juga
	- == sama dengan, kalo ini absolut, contoh kalo 4==4 hasilnya true, kalo nilainya selain itu seperti 3==4 hasilnya false. Ingat sama dengannya ini dobel beda dengan =, sama dengan yang tidak dobel itu digunakan untuk assignment variable.
	- != tidak sama dengan, kalo ini kebalikan dari ==, semisal kalo 3!=4 hasilnya true,
kalo 3!=3 itu hasilnya false

operasi komparasi diatas bekerja pada syntax literal, maksudnya gmana? semisal
a==4 , a nya itu ada nilainya, dan itu memakan memori bisa disebut dengan objek, 4 nya itu literal. 

Nah ada yang Operasi komparasinya yang membandingkan sesama memori atau objek, yaitu is dan is not. Ini nanti digunakan untuk OOP
semisal ada a=3 b=3 
kalau kita jalanin a is 3 itu gk bakalan jalan bakal muncul warning, karena is membandingkan 2 objek
kalau kita jalanin a is b itu jalanan dan hasilnya true, mirip seperti == tapi untuk membandingkan 2 objek

kalo is not kebalikan dari is, mirip seperti !=

untuk mengetahui id atau identitas suatu objek caranya yaitu id(objek/variabel), untuk mengetahui memori atau address suatu objek yang biasa di C caranya yaitu hex(id(objek))
kalo nilai suatu objek itu sama, semisal a=3 b=3, kalau di python akan memiliki id yang sama, karena penyimpanan memori nya sama, jadinya lebih efisien, kalau di C atau c++ itu idnya beda karena disimpan di memori yang berbeda


operasi logika ini digunakan untuk data biner dan hasilnya true atau false
	- not , penggunakan nya kalau semisal
 a= false
 c= not a
 maka Ketika hasilnya adalah c itu jadi true , kalau di print(c) hasil nya true
	- or, penggunaannya kalau semisal
 a = True
 b = False
 c = a or b
 itu hasilnya akan true karena salah satu ada yang true meskipun a false atau b true, beda kalau duanya false
 a = false
 b = false
 c = a or b
 hasilnya c akan false 

	- and penggunaannya kalau semisal 
 a = true
 b = false
 c = a and b
 itu hasinya akan false karena kalau and akan true kalau dua2nya true, gk bisa salah satu saja atau semisal dua2nya itu false hasilnya akan false
	- xor ini beda dia pakai ^, penggunaannya kalau semisal
 a = true
 b = false 
hasilnya akan true, jika salah satu objek true, sisanya false contoh
contoh kalau true dgn true hasilnya false, begitu juga false dengan false hasilnya akan false
 
saya dapat ilmu baru kalau mau spasi enter di print() itu pakai /n

Latihan rentang angka
buat program input angka kalau nilanya benar (+) maka hasilnya true
1. ----0++++5----8++++11----
2. ++++0----5++++8----11++++
