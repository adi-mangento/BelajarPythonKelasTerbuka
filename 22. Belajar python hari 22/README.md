Di ke-22 ini saya belajar mengenai nested multi keys dan nesting dictionary, simpenya dictionary dalam dictionary 
kan kalo di nested list bentuknya kyk dibawah
data_list = [[1,2,3],1,3]
trus kalo mau dapetin data 2 gitu caranya kan
print(data_list[0][1]) #outputnya: 2, karena ini artinya ambil data di indeks pertama kemudian ambil data di indeks 1

nah kalo di dictionary, mau dapetin datana bukan berdasarkan indeks, tapi keynya. contoh
kita punya dictionary kyk dibawah
mahasiswa1 = {
	'nama':'Ucup Surucup',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
	'nama':'Otong Surotong',
	'nim':'19022002',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
	'nama':'Asep Si Kasyep',
	'nim':'19022003',
	'sks_lulus':100,
	'beasiswa':False,
	'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
	'MAH001':mahasiswa1,
	'MAH002':mahasiswa2,
	'MAH003':mahasiswa3
}

ini kan data mahasiswa1 sampai mahasiswa3 ada di dalem dict data_mahasiswa, pake keynya
nah semisal cara mau dapetin data value Otong surotong caranya
dataOtong = data_mahasiswa['MAH001']['nama']
print("dataOtong") # hasilnya otong surotong


