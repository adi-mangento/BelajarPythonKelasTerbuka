Di Hari 15 ini saya belajar membuat list
jadi list itu adalah kumpulan data, nah data nya itu bisa data number, string, Boolean
contoh 
angka = [1,4,5,2]
print(angka)
hasil eksekusi
[1, 4, 5, 2]

data_string = ["ucup","otong","odah"]
print(data_string)
hasil eksekusi
['ucup', 'otong', 'odah']

data_bool= [True, False, True]
print(data_bool)
hasil eksekusi
[True, False, True]

nah isi dari data list bisa dari campuran ketiga tipe data diatas
data_campuran = ["otong","makan",7,"bakwan",True]
print(data_campuran)
hasilnya
['otong', 'makan' , 7, 'bakwan', True]

Adapun cara list membuat suatu data list menggunakan range
data_range = range(0,10)
data_list = list(data_range)
print(data_list)

hasilnya
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data_range = range(0,10,2) #range(start,stop,step) step ini maksudnya inkremennya
data_list = list(data_range)
print(data_list)

hasilnya
[0, 2, 4, 6, 8]

Adapun cara membuat list menggunakan for loop, list comprehensive
list_pake_for = [i for i in range(0,10)] #ini bacanya i untuk i di dalam range 0-10
print(list_pake_for)

hasilnya 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

trus fungsinya for di list ini apa? yaitu untuk melakukan operasi didalam listnya, semisal kita mau pangkat 2 isi dari tiap listnya
print(list_pake_for**2) #kalo kita pakai kyk gini itu hasilnya bakal error

kalo script nya kyk dibawah
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

hasilnya jadi tiap i dalam list dipangkat 2
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 

membuat list pake for dan pake if
list_pake_for_if = [i for i in range(0,10) if i != 5] #ini bacanya ambil i untuk tiap i di dalam range 0-10 jika i bukan 5 (maksudnya semua i diambil dalam range tersebut kecuali 5)
print(list_pake_for_if)

hasilnya 
[0, 1, 2, 3, 4, 6, 7, 8, 9]

contoh lainnya lagi
list_pake_for_if = [i for i in range(0,10) if i%2 == 0] #ini bacanya ambil semua i pada tiap i di range 0-10 jika hasil modulus i dibagi dua adalah nol yang artinya i yang diambil pasti angka genap

print(list_pake_for_if)
[0, 2, 4, 6, 8]

contoh lainnya lagi
list_pake_for_if = [i for i in range(0,10) if i%2 != 0] #ini bacanya ambil semua i pada tiap i di range 0-10 jika hasil modulus i dibagi dua bukan nol yang artinya i yang diambil pasti angka ganji

print(list_pake_for_if)
hasilnya
[1, 3, 5, 7, 9]

