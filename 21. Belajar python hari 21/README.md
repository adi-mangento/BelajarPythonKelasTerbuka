Di hari ke 21 saya belajar mengenai looping, copy, dan pop pada dictionary
semisal kita punya data dict seperti dibawah
temen_temen = {
	"cep":"Acep Nurmagedov",
	"sep":"Asep Surasep",
	"toy":"Atoy Sulatoy",
	"Cup":"Ucup Surucup"
	}
di dictionary ada berbagai cara untuk looping
# looping hanya keynya saja
for temen in temen_temen:
	print(temen)
hasilnya
cep
sep
toy
cup

di dictionary agar skrip untuk looping menjadi lebih rapih menggunakan suatu operator untuk mengambil itemnya mau itu key ataupun value

keys = temen_temen.keys()
print(keys) # Hasilnya dict_keys(['cep', 'sep', 'toy', 'cup'])
#semisal ngambil berdasarkan keynya
#untuk loopingnya
for key in temen_temen.keys:
	print(key)	#ambil keynya aja 
	#hasilnya
	cep
	sep
	toy
	cup
	print(temen_temen.get(key) #ambil valuenya
	#hasilnya
	Acep Nurmagedov
	Asep Surasep
	Atoy Sulatoy
	Ucup Surucup

# semisal mau ngambil values-nya
values = temen_temen.values()
print(values) 
# hasilnya
dict_values(['Acep Nurmagedov', 'Asep Surasep', 'Atoy Sulatoy', 'Ucup Surucup'])

#loopingnya 
for value in temen_temen.values():
	print(value)
#hasilnya
Acep Nurmagedov
Asep Surasep
Atoy Sulatoy
Ucup Surucup

# semisal mau ngambil item (key dan value-nya sekaligus
items = temen_temen.items()
print(items)
#hasilnya
dict_items([('cep', 'Acep Nurmagedov'), ('sep', 'Asep Surasep'), ('toy', 'Atoy Sulatoy'), ('Cup', 'Ucup Surucup')])

#loopingnya
for item in teman_teman.items():
	print(item)
#hasilnya
('cep', 'Acep Nurmagedov')
('sep', 'Asep Surasep')
('toy', 'Atoy Sulatoy')
('Cup', 'Ucup Surucup')

#untuk mengeksekusi key dan values-nya terpisah caranya
for key,value in temen_temen.items()
	print(f"key = {key}, value = {values}"):
hasilnya
key = cep, value = Acep Nurmagedov
key = sep, value = Asep Surasep
key = toy, value = Atoy Sulatoy
key = Cup, value = Ucup Surucup

lalu untuk copy dictionary sama seperti di list, semisal kita punya dictionary
temen_temen = {
	"cep":"Acep Nurmagedov",
	"sep":"Asep Surasep",
	"toy":"Atoy Sulatoy",
	"Cup":"Ucup Surucup"
	}

kita tidak bisa hanya sekedar temen_temen = friends untuk menduplikatnya harus menggunakan .copy() agar addressnya berbeda
contoh
friends = temen_temen #ini addressnya bakal sama
frends = temen_temen.copy() #duplikat dan addressnya berbeda

lalu untuk mentransfer data dari dictionary berdasarkan key-nya menggunakan .pop(key) 
contoh
dataAtoy = friends.pop('toy')
print(friends)
print(f"Data Atoy = {dataAtoy}")

# hasilnya
{'cep': 'Acep Nurmagedov', 'sep': 'Asep Surasep', 'Cup': 'Ucup Surucup'}
Data Atoy = Atoy Sulatoy

bisa dilihat hasilnya, kalau data atoy menghilang dari dictionary dan berpindah ke variabel Data Atoy

Adapun cara mentransfer data terakhir menggunakan .popitem(), disini kita tidak perlu memasukan key-nya
DataTerakhir = friends.popitem()
print(friends)
print(f"Data Atoy = {dataAtoy}")

#hasilnya
{'cep': 'Acep Nurmagedov', 'sep': 'Asep Surasep'}
Data terakhir = ('Cup', 'Ucup Surucup')
bisa dilihat hasilnya, kalau data ucup menghilang dari dictionary yang posisinya di akhir dan berpindah ke variabel Data terakhir