Di Hari ke 6 ini saya belajar format string dan date and time
contoh generic

#string
nama = "budi"
format_str = f"Hello {nama}" #f disini artinya format
print(format_str)
-nah kalo di eksekusi hasilnya-
Hello budi

#boolean
bool = False
format_str = f"boolean = {boolean}"
print(format_str)
-hasilnya adalah-
Boolean = False

#angka
angka = 2005.5
format_str= f"angka = {angka}"
print(format_str)
-hasilnya adalah-
angka = 2005.5

#bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}" #ini artinya adalah menenjukan bahwa si angka bilangan bulat
print (format_str)
hasilnya 
15 #kalau angkanya bilangan decimal kyk 15.5 itu pas dieksekusi hasilnya error

#bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka:,}" #pakai :, biar ada pemisanya
print(format_str)
hasilnya
2,000 

#bilangan decimal
angka = 2005.54321
format_str= f"angka = {angka:.2f}" #tujuannya buat mau berapa angka desimalnya
print(format_str)
-hasilnya adalah-
angka = 2005.54

#menammpilkan leading zero
angka = 2005.54321  #jumlah angka dari 2 sampai 4 kan ada 8
format_str= f"angka = {angka:09.2f}" #ini artinya jadi 0 di depan angka 2 supaya jadi 9 angka
print(format_str)
02005.54321

#menampilkan tanda + atau -
angka_plus = 10.1234
angka_minus = -10
format_minus = f"minus =  {angka_minus:+d}
format_plus = f"plus = {angka_plus:+.2f} 
print(format_minus)
print(format_plus)
hasilnya # itu dia hasilnya bakal keluar tandanya
minus = -10
plus = +10.12

#memformat Persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}" ini artinya hasil persennya cuman nampilin 2  angka dibelakang koma
print(format_persen)
hasilnya
4.50%

#melakukan operasi aritmatika didalam placeholder
Harga = 1000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)
hasilnya
5,0000

#format angka lain (binary,octal,hexadecimal)
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)
hasilnya adalah
binary = 0b11111111
octal = 377
hex = 0xff

#mengatur lebar (bikin jadi rata kanan
data_string =f"""
nama   = {data_nama:>5} #Bikin data string jadi rata kanan dengan jumlah karakter 5
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""""
print(data_string)

hasilnya adalah
nama   =  Ucup
umur   =    12
tinggi = 175.4 #karena tinggi badan jumlah karakernya 5 semuanya jadi keliatan sama rata
sepatu =    44

