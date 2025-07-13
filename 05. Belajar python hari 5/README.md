Di hari ke 5 ini saya belajar mengenai data string
jadi string itu adalah kumpulan dari karakter
cara membuat string itu gmana?
1. menggunakan single quote
  '........'
  contoh 
  data = 'Menggunakan single quote'
2. menggunakan double quote
  "........"
  contoh
  data = "Menggunalan double quote 
  bisa juga kutip dalam kutip
  semisal
  data = '"halo"'
  hasilnya adalah "halo"
  print("hari jum'at")

Dalam string ada penggunaan \, ini bisa digunakan untuk:
- membuat tanda ' menjadi string
  print('mari shalat jum\'at') hasilnya mari shalat jum'at
  print('g\' day, isn\'t it?')
- bikin backslash (\) jadi string, karena \ -nya satu kebacanya jadi perintah contoh
  print("C:\user\adi") ini akan error karena \ dibacanya jadi perintah
  yang benar itu
  print("C:\\user\\adi")
- bikin tab
  print("bobo\tsama kamu") hasilnya jadi bobo	sama kamu
- bikin backspace
  print("bobo \bsama kamu") hadilnya jadi bobosama kamu
- newline
  print('bobo sama\nkamu')
  hasilnya 
  bobo sama
  kamu
Dalam data string ada yang namanya string literal atau raw string
raw string ini digunakan untuk mengatasi hal seperti
print('C:\new folder') 
kalau dieksekusi hasilnya akan 
C:
ew folder jadi ada new line atau enter gitu
untuk mengatasinya seperti di bawah ini (raw string)
print(r'C:\new folder') yang didalam tanda kutip dijadikan raw string menghilangkan konvensi string yang menggunakan \
hasilnya akan C:\new folder

dalam string ada yang namanya multiline literal string, semisal
print("""
Nama : Toni
Makanan favorit : Nasi Kuning
Minuman favorit : Es Teh
""")
hasilnnya printnya seperti dibawah yang mana enternya sesuai
Nama : Toni
Makanan favorit : Nasi Kuning
Minuman favorit : Es Teh
 multiline literal string bisa digabungkan juga dengan raw string
Contoh
print(r"""
....
d...
\n..
""")
hasilnya akan 
....
d...
\n..

Operasi dan Manipulasi data string
1. Menyambung string (Concatenate)
 nama_depan = "Adi"
 nama_tengah = "D."
 nama_akhir = "Mangento"
 nama_lengkap = nama_depan + nama_tengah + nama_akhir
 print(nama_lengkap)
 setelah dieksekusi hasilnya akan
 AdiD.Mangento
 nah kalau mau ada spasinya musti
 nama_lengkap = nama_depan +" "+ nama_tengah +" "+ nama_akhir
 lalu print(nama_lengkap)
 hasilnya akan
 Adi D. Mangento

2. Menghitung Panjang string
 Panjang = len(nama_lengkap)
 print(str(Panjang))
 hasilnya akan jumlah karakter pada data string
 dalam hal ini hasilnya 15

3. Mengecek ada komponen char atau string di string
 contoh
 d = "d"
 status = d in nama_lengkap #buat ngecek ada d di nama_lengkap
 karena nama lengkap-nya adi D. Mangento
 hasil statusnya adalah True karena ada komponen d di adi D. Mangento
 kalau 
 status = d not in nama_lengkap ##buat ngecek kalao gak ada d di nama_lengkap
 hasilnya false

4. Mengulang string
 print("wk"*10)
 hasilnya akan wkwkwk sampai 10 kali
 bisa juga
 print(10*"wk")
 hasilnya akan sama

5. Indexing (mengambil data dari string)
 contoh
 print("index ke-0: "+ nama_lengkap[0])
 hasilnya adalah index ke-0: a
 kenapa begitu karena
 adi D. Mangento
 0123456789....14
 kalo nama_lengkap[2]
 maka hasilnya i
 nah kalau semisal nama_lengkap[-1]
 itu dia hasilnya 0, karena dia ngambil dari belakang
 nah semisal kita mau ambil kata adi dari nama_lengkap
 caranya yaitu 
 nama_lengkap[0:4] #ini artinya ngambil data dari 0 sampai sebelum 4
 kalau
 print("index ke-[0,2,4,6,8,10]:"+ nama_lengkap[0:11:2] #ini artinya ngambil data dari 0 sampai 10 dengan inkremen 2, artinya ngeloncatin tiap kelipatan dua. dalam hal ini hasilnya
 aiD agno

6. operator dalam bentuk method
 data = "otong sorotong pararotong"
 jumlah = data.count("o")
 print("jumlah o pada " + data + " = " + str(jumlah))
 hasilnya adalah 6
 kenapa 6 karena si data.coun("o") artinya menghitung jumlah o di dalam objek data
 len(kalimat) #jumlah karakter

7. Mengubah semua Karakter menjadi uppercase
 semisal 
 salam = "bro"
 upper = salam.upper()
 print(upper)
 Ketika dieksekusi maka hasilnya
 BRO

8. Mengubah semua Karakter menjadi lowercase
 contoh
 alay = "Aku KeCe SekaLi"
 rapih = alay.lower()
 print(rapih)
 maka setelah dieksekusi hasilnya
 aku kece sekali

9. Pengecekan dengan isX method
  mengecek apakah semua karakternya lowercase
 salam = "sit"
 apakah_lower = salam.islower()
 print(salam + "is lower = " + str(apakah_lower))
 maka hasilnya 
 sit is lower = True
 
 mengecek apakah semua karakternya uppercase
 salam = "sit"
 apakah_upper = salam.isupper()
 print(salam + "is upper = " + str(apakah_upper))
 maka hasilnya 
 sit is upper = False
 
 Adapun pengecekan lainnya
 isalpha() <- untuk mengecek semuanya huruf
 isalnum() <- huruf dan angka
 isdecimal() <- angka saja
 isspace() <- spasi, tab, newline \n
 istitle() < semua kata dimulai dengan huruf besar

10. pengecekan dengan komponen startswith() dan endswith()
 contoh
 cek_start = "Madu Kelopo".startswith("madu")
 print(cek_start)
 maka hasilnya 
 False 
 kalua mau true harusnya
 cek_start = "Madu Kelopo".startswith("Madu")

 contoh
 cek_end = "Madu Kelopo".endswith("Kelopo")
 print(cek_end)
 maka hasilnya 
 True

11. Penggabungan komponen join() dan pemisahan komponen split()
 misal tipe data list (list itu kumpulan data)
 pisah = ['aku','sayang','kamu']
 gabung = ','.join(pisah)
 print(pisah)
 print(gabung)
 setelah dieksekusi hasilnya 

 ['aku','sayang','kamu']
 aku,sayang,kamu
 
 komanya diganti jadi spasi maka gabung = ' '.join(pisah)

 nah kalo split
 semisal 
 gabungan = "akuehmsayangehmkamu"
 pisah = gabungan.split('ehm')
 print(pisah)
 maka hasilnya akan menjadi data list
 ['aku', 'sayang', 'kamu']

12. Alokasi karakter menggunakan rjust(), ljust(), center()
 semisal 
 kanan="kanan".rjust(10)
 print("'"+kanan+"'")
 hasilnya akan
 '     kanan'
 yang mana total karakternya jadi 10 dan karakter sebelumnya nya jadi pindah ke kanan
 kalo ljust() string sama sama seperti rjust() tapi di kiri
 kalo center() di tengah
 nah kalo mau hasilnya nya bukan spasi aja pakai kyk "kanan".rjust(10,"=") maka hasilnya
 '=====kanan'



   
 
