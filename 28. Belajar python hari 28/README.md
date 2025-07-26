Pada hari ke-28 saya belajar mengenai:
- import statement
- membuat module
- membuat package
- _init_.py pada package

jadi import statement itu intinya kita jalanin program python didalam python kita,
jadi contohnya semisal kita punya file
Dongdot.py dan isinya:
print("dongdot")

nah penggunaan importnya itu contohnya, kita punya program python yg inti:
main.py dan isinya:
print("ini main")
import Dongdot

nah Ketika dieksekusi file main.py hasilnya
ini main
dongdot

kenapa keluar dongdot karena sebelumnya mengimport program dongdot itu, program dongdot ini disebut dengan module.
cara menjalankan module tersebut di program inti kita yaitu main.py, syaratnya yaitu module tersebut path harus setara dengan file main.py, ilustrasinya kyk dibawah:
abrakadabra   (folder)
---main.py
---Dongdot.py (module)
---matematika.py (module)
---fisika.py (module)

Nah kita akses fungsi ataupun variable yang ada di dalam module caranya yaitu, semisal didalam module (matematika) isinya:
data = 32
def tambah(a,b):
	return a+b
def kurang(a,b):
	return a-b

module fisika:
def gaya(massa,percepatan):
	return massa*percepatan


nah cara akses fungsi dan variable yang ada di module tersebut caranya yaitu, di program main.py:
import matematika

print(matematika.data) #akses variable data

print(matematika.tambah(1,2)) #akses fungsi dalam module


atau semisal kita mau import salah satu fungsi atau variable biar kalo make matematika.tambah() cukup dengan tambah().
caranya make 'from' contohnya
from matematika import tambah
a = tambah(1,2)
print(a)

hasilnya 
3

atau lebih singkat lagi menggunakan "as"
from matematika import kurang as k
import fisika as f

force = f.gaya(3,10)
print(force) #outputnya 30

pengurangan = k(12,6)
print(pengurangan) #output 6

Nah trus gmana kalo semisal struktur file nya nya seperti dibawah
abrakadabra   (folder)
---sains      (folder)
   ----matematika.py (module)
   ----fisika.py (module)
---main.py
---Dongdot.py (module)
nah untuk strukstur diatas si folder sains yang berisi module matematika dan fisika disebut dengan package, nah cara menggunakannya
di main.py:
import sains.matematika #bisa dengan struktur seperti ini
from sains import fisika #bisa dengan struktur seperti ini
from sains.fisika import gaya as f #bisa dengan struktur seperti ini

a = sains.matematika.tambah(1,2)
print(a) #output 3

b = fisika.gaya(4,10)
print(b) #output 40

c = f(3,10)
print(c) #output 30


nah kalo semisal kita mau import sains trus module yang ada didalam bisa langsung dipakai tanpa harus kyk import sains.matematika.tambah(), itu menggunakan _init_.py , nah _init_
cara pakai strukturnya seperti ini 
abrakadabra   (folder)
---sains      (folder)
   ---matematika (Folder)
       ---_init.py_
       ---basic.py (module)
       ---Scientific.py (module)
   ---fisika.py (module)
   ---_init_.py 
---main.py
---Dongdot.py (module)

nah _init_.py gunanya kyk buat menghubungkan semua modul yang ada di path sama ke parentnya secara mudah,
nah dalam hal ini isi dari _init_.py ini gunanya buat import modul atau package yang setara pathnya
isi _init_.py dalam folder sains
from . import matematika
from . import fisika

isi _init_.py dalam folder matematika
from . import basic
from . import scientific

from .basic import tambah,kali #dalam modul basic ada fungsi tambah & kali
from .scientific import pangkat #dalam modul scientific ada fungsi pangkat

isi dari main.py:
import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1,2,3,4,45)
print(f"hasil tambah = {hasil_tambah}")

hasil_pisika = sains.pisika.gaya(10,9.8)
print(f"hasil pisika = {hasil_pisika}")

hasil_kali = sains.matematika.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(5)}")

perlu diingat file __init__.py itu underscorenya ada dua




