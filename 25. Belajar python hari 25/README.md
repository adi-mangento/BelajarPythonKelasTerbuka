Hari ke-25 ini saya belajar mengenai hints pada fungsi, dan \*args dan \*\*kwargs



jadi hint pada fungsi itu apa sih? intinya adalah clue2 yang memberitahu cara menggunakan fungsi yang dipakai. Nah contoh fungsi yang sudah diberia dengan hint yg lengkap seperti dibawah: 



saya sedang belajar hint pada fungsi  contoh nya apakah benar seperti ini



def fungsi(a:int) -> int:

&nbsp;	'''ini fungsi menambahkan nilai 1 pada input'''

&nbsp;	b = a+1

&nbsp;	return b



nanti Ketika ingin menggunakan fungsi tersebut akan muncul seperti dibawah:





nah \*args ini sebenarnya penggunaan-nya gk harus dengan \*args tapi bisa dengan nama variable yg lain contohnya \*argument ataupun \*input, nah yang penting itu \*-nya. \*-nya ini digunakan jika input yang dimasukan ada banyak dan tidak ada Batasan inputnya, yang mana nantinya data input-nya akan menjadi tipe data tuples



contoh penggunaannya



semisal ingin buat fungsi rata-rata



def rata2(\*data):

&nbsp;	jumlah\_data = len(data)

&nbsp;	Penjumlahan\_semua\_data = 0

&nbsp;	for angka in data:

&nbsp;		Penjumlahan\_semua\_data += angka

&nbsp;	output = Penjumlahan\_semua\_data/jumlah\_data

&nbsp;	return output



rata2(1,2,3)



maka hasilnya

2 

karena dari (1+2+3)/3





nah untuk \*\*kwargs ini sama seperti \*args yang mana yg penting \*\*-nya. penggunaan \*\*kwargs kita memerluakan keyword untuk penggunaan fungsinya, nah cara tau keyword yang dipakai, kita kasih tau dari hints yg kita berikan. 



contoh



def fungsi\_aman(\*\*kwargs):

&nbsp;   if 'nama' in kwargs:

&nbsp;       print(f"Nama: {kwargs\['nama']}")

&nbsp;   else:

&nbsp;       print("Parameter 'nama' tidak ditemukan")



fungsi\_aman(umur=25)  #Output Parameter 'nama' tidak ditemukan

fungsi\_aman(nama='budi') #Output 'Nama: budi'



fungsi diatas adalah fungsi yang aman dikarenakan jika tidak keywordnya akan diberikan alternatif prosesnya



nah kalo gk ada alternatifnya contohnya seperti di Bawah 

def fungsi(\*\*kwargs):

&nbsp;   '''fungsi kwargs'''

&nbsp;   nama = kwargs\["nama"]

&nbsp;   tinggi = kwargs\["tinggi"]

&nbsp;   berat = kwargs\["berat"]

&nbsp;   print(f"{nama} punya tinggi {tinggi} dan berat {berat}")



fungsi(nama="ucup",tinggi=183,sehat=23) #output error

fungsi(nama="ucup",tinggi=183,berat=79,sehat=23) #Output ucup punya tinggi 183 dan berat 79



nah argument \* dan \*\* sendiri bisa digabung dalam satu fungsi, contohnya seperti dibawah:

def math(\*args,\*\*kwargs):

&nbsp;   output = 0

&nbsp;   if kwargs\["option"] == "tambah":

&nbsp;       for angka in args:

&nbsp;           output +=angka

&nbsp;   elif kwargs\["option"] == "kali":

&nbsp;       output = 1

&nbsp;       for angka in args:

&nbsp;           output \*= angka

&nbsp;   else:

&nbsp;       print("tidak ada operasi")



&nbsp;   return output



hasil = math(1,2,3,4,option="tambah")



print(f"hasil jumlah {hasil}")



outputnya adalah

hasil jumlah 10

kesimpulannya output argumen menggunakan * adalah tuples dan ** adalah dict.

kalo mau make fungsi yg ada ** sebagai argumennya, masukan keynya. contoh fungsi(key='a')









