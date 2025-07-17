Di hari ke-24 ini saya belajar mengenai fungsi (function), fungsi ini bisa disebut method di Bahasa lain atau subroutine. 
fungsi pada dasarnya adalah blok kode yang terstruktur, yang nantinya bisa digunakan tanpa menulis ulang blok kode tersebut, cukup dengan memanggil fungsi yang sudah dibuat saja. Tujuannya script menjadi lebih rapih. function pada python bisa dilihat seperti dibawah:
def hello(): #ini contoh fungsi
	print("hello world") #dan ini body dari fungsinya

nah disinikan sudah dibuat fungsi hello(), cara pakainya cukup
hello()
nanti hasil eksekusinya
hello world

bisa dilihat, kita tidak perlu menulis print("hello World") di script cukup menulis hello() saja di script dan ini bisa dilakukan berkali2.

function bisa menerima input
contoh pemakaiannya semisal untuk operasi perhitungan

def luas_segitiga(alas,tinggi): 
	luas = (alas*tinggi)/2
	print(luas)

#nah input yang didalam tanda kurung ini disebut dengan arguments, variabel arguments cuman berpengaruh ke blok kode yang ada didalem fungsinya. bisa dilihat contoh 2 yang dibawah meskipun variabelnya a atau b tetep bisa dijalanin bukan alas ataupun tinggi

#Contoh 1
luas_segitiga(4,8) #disini alasnya adalah 4 dan tingginya 8
hasilnya
16

#Contoh 2
a = 4
b = 8
luas_segitiga(a,b) 

hasilnya
16

#Contoh 3 bisa juga dituker posisinya caranya dengan menulis argumentnya, contoh
luas_segitiga(tinggi = b, alas = a)

hasilnya
16

nah pada function untuk memperoleh value dari function untuk dipakai itu menggunakan return. contohnya

def luas_segitiga(alas,tinggi): 
	luas = (alas*tinggi)/2
	return luas

a = 4
b = 8
c = luas_segitiga(a,b) #value fungsinya jadi c
print(c)

hasilnya
16

nah pada function kita bisa membuat default value dari argumentnya jika nantinya Ketika memanggil fungsinya tidak memasukan inputnya
contoh
def sapa(nama="Pengguna"):
    print(f"Halo, {nama}!")

sapa()          # Output: Halo, Pengguna! ini default
sapa("Ani")     # Output: Halo, Ani! ini 


lalu gmana semisal argumennya banyak kyk dibawah dan udh ada defaultnya, dan kita cuman mau kasih input ke  argument yang kita mau aja, caranya contoh:
def fungsi(a = 1,b = 2,c = 3,d = 4,e = 5):
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)

#itu caranya
fungsi() #default
fungsi(b = 3, a = 4) #custom

hasilnya
#defult
1
2
3
4
5
#custom
4
3
3
4
5


