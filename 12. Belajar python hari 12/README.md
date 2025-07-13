Di hari ke 12 saya belajar perulangan menggunakan while, nah jadi perulangan menggunakan while itu Boolean beda dengan for yang list, string, dsb

nah semisal kita punya alur seperti dibawah

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

kan kalo for itu
for i in list:            #tiap item pada list jalankan aksinya yang mana print(i)
	print(i)

beda kalo while
while kondisi:           #kalo while, tiap kondisinya true dia bakal terus jalan aksinya,
    aksi

semisal
a = 1                     #bisa dilihat karena a itu 1 yang mana 1 > 0 dan itu true, maka dia akan terus print "monokorobo", dan gk bakal jalanin print("cukup") karena true terus
while a > 0:
    print("Monokorobo")
print("cukup")

nah cara make while contohnya kyk gini
a = 0
while a < 3:
    a += 1
    print("Monokorobo")   
print("cukuP")   

bisa dilihat karena a itu 0 dan kondisinya a < 3 maka dia bakal jalanin perintah a += 1 lalu print("monokorobo") hasilnya
monokorobo
monokorobo
monokorobo
cukup
kenapa dia bisa sampai print(cukup), itu karena a-nya kan di update terus dengan a+=1 nah Ketika a-nya udh lebih dari 3, dia hasilnya lebih dari 3 yang mana gk ngejalanin perintah didalam while, langsung print("cukup")
