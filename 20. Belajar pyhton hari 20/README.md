di Hari ke 20 ini saya belajar data collection tipe lain yaitu dictionary (dict).
Jadi kan kalo list itu, bentuknya kyk dibawah
data_list = [1,2,6,3,2]

nah kalo dict
data_dict = {'key:value','tg:otong','bd:Budi'}

nah trus bedanya apa? kalo list kita ngambil datanya berdasarkan index-nya, semisal kita mau ngambil data angka 3 di list
caranya yaitu:
data_list[3] atau data_list[-2]

tapi kalo dict, kita ngambil datanya(value) berdasarkan keynya, semisal kita mau ambil data otong, caranya yaitu
data_dict[tg]
nah value dari data dict, isinya bisa macam-macam, boleh angka, string, Boolean, list, ataupun dict lagi juga bisa

nah di dictionary ada beberapa opearasi yang saya pelajari
semisal punya dict
data_dict ={
	'cup':'Ucup Surucup',
	'tong':'otong surotong',
	'dudu':'dudung surudung'
	}

# Panjang dictionary (len)
lendict = len(data_dict)
print(lendict) #hasilnya 3

#mengecek key-nya exist atau gk di dictionary-nya
key = "cup"
cek = key in data_dict
print(f"apakah {key} ada di data_dict: {cek}") # hasilnya: apakah cup ada di data_dict: True

#mengakses value dengan get
kan akses data dict bisa pakai
print("data_dict['cup']") #nah tapi ini kekurangannya kalau key-nya gk ada ('semisal kis') hasilnya bakal eror
kalo
print("data_dict.get('cup') #pake ini biar enak, biar bisa bedain variabel mana yang list dan dict, sama kalo semisal key-nya gk ada hasil programnya bukan error muncul none aja
print("data_dict.get("cup","key tidak ditemukan") #kata none-nya pun bisa diganti dengan "key tidak ditemukan" kalo semisal key-nya tidak ditemukan

#mengupdate data
data_dict = {"a": 1, "b": 2}
# Cara 1: Langsung assign
data_dict["a"] = 100  # Update
data_dict["c"] = 3    # Tambah baru

# Cara 2: Update
data_dict.update({"a": 1000, "d": 4})  # Update 'a' dan tambah 'd'

print(data_dict)
# Output: {'a': 1000, 'b': 2, 'c': 3, 'd': 4}

bedanya yang pertama dan yang kedua, kalo yang pertama hanya 1 key-value saja dan yang kedua bisa banyak key-value sekaligus

#mendelete
# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)

hasilnya menghapus data yang key-nya faqih