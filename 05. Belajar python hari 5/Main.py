############ Program kartu nama #########
nama = input("Masukan Nama : ").title()
profesi = input("Masukan Profesi : ").title()
kota = (input("Masuka Kota : ")).title()

print("KARTU NAMA".center(20,"="))
print(nama.center(20," "))
print(profesi.center(20," "))
print(kota.center(20," "))
print("=".center(20,"="))

########### Sistem Pemisah String chat ########
chat1 = input("Chat ke-1 : ")
chat2 = input("Chat ke-2 : ")
chat3 = input("Chat ke-3 : ")

chat = chat1+"|||"+chat2+"|||"+chat3
print(chat)

pisah=chat.split("|||")
print(pisah)
gabung='\n'.join(pisah)
print(gabung)

#########Statistika String############
kalimat=input('Masukan Kalimat : ')
len(kalimat)
print('Panjang kalimat : ', len(kalimat))
print("Jumlah huruf 'a' : ", kalimat.count('a'))
print('Semua huruf kecil : ', kalimat.islower())
print(kalimat.upper())