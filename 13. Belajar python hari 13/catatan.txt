Di hari ke 13 saya belajar pass, continue, dan break

jadi pass itu berfungsi sebagai dummy, tidak akan dieksekusi
semisal 
angka = 0
while angka < 5:
	angka +=1
	if angka == 3:
		pass  #ini tidak akan dieksekusi, tidak diimplementasikan
	print(angka)

setelah dieksekusi hasilnya:
1
2
3
4
5

trus pass nya buat apa? pass nya dipakai semisal kalau semisal nanti kita udh make yang Namanya fungsi, ataupun oop sesmial
class hero:
	pass #jadi dia ada tapi tidak diimplementasikan

lalu continue itu apa? jadi continue itu dipakai kalau semisal alurnya

  start
    |
    |<----------------
    |                 |
    |               aksi 2
    |    loop 2       |
    |                 |  
    | continue        |false
    |<---aksi 3--- Kondisi 2
    |                 ^
    |                 |
    |                 |
    |     loop 1      |
    |                 |
    |                 |
    v                 |
Kondisi 1 --true--> aksi 1
    |
    |false
    V

angka = 0
while angka < 5: #Kondisi 1
	angka +=1                           #aksi 1
	print(f"angka sekarang -> {angka}") #aksi 1
	if angka == 3:         #kondisi 2
		print("nice") #aksi 3 
		continue  #bikin aksi (aksi 2) yang di bawah script tidak dieksekusi di iterasi ini jadi nya langsung ke kondisi 1 (sebenarnya tidak ada aksi 3 gk masalah, continue masih bisa digunakan
	print("same") # aksi 2
print("cukup")

pas dieksekusi hasilnya jadi
angka sekarang -> 1
same
angka sekarang -> 2
same
angka sekarang -> 3
nice
angka sekarang -> 4
same
angka sekarang -> 5
same
cukup

Kemudian ada break, jadi break itu alurnya
start
  |
  | <-------------aksi 2
  |                 ^
  |                 |         
  |             Kondisi 2 ---break---              
  |                 ^                |
  V                 |                |
kondisi 1--true-->aksi 1             |
  |                                  | 
  |false                             |
  |                                  |
  |<---------------------------------
  V
finish

angka=0
while angka < 5: #kondisi 1, ini bisa juga pakai while true: biar loop terus, gk harus sampe 5
	angka +=1
	print(f"angka sekarang -> {angka}")
	if angka == 3:
 		print("nice")
		break #untuk keluar dari loop 
	print("same")
print("cukup")

pas dieksekusi hasilnya jadi
angka sekarang -> 1
same
angka sekarang -> 2
same
angka sekarang -> 3
nice
cukup
