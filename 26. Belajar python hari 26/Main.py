print("TANTANGAN 1".center(60,"="))
print(" Lambda Sederhana ".center(60,"="))
print("""
Buat lambda function untuk: 
• Mengalikan dua angka (kali = lambda x, y: ...). 
• Mengecek apakah angka genap (is_genap = lambda x: ...). 
""")

kali= lambda x,y: x*y
is_genap = lambda x: x%2 == 0

print(kali(3,4))
print(is_genap(1))

print("TANTANGAN 2".center(60,"="))
print(" Sorting dengan Lambda ".center(60,"="))
print("""
Diberikan list tuple: 
python 
siswa = [("Budi", 90), ("Ani", 85), ("Citra", 95)] 
1. Urutkan berdasarkan nama (ascending). 
2. Urutkan berdasarkan nilai (descending).
""")

siswa = [("Budi", 90), ("Ani", 85), ("Citra", 95)] 
siswa.sort(key= lambda x:x[0])
print(f"Ascending = {siswa}")

siswa.sort(key= lambda x:x[1], reverse = True)
print(f"Descending = {siswa}")


print("TANTANGAN 3".center(60,"="))
print(" Currying: Konverter Suhu ".center(60,"="))
print("""
Buat fungsi currying konverter_suhu yang: 
• Tahap 1: Pilih jenis konversi ("c2f" atau "f2c"). 
• Tahap 2: Masukkan nilai suhu. 
• Hasil: Konversi Celsius ↔ Fahrenheit. 
""")

def konverter_suhu(jenis):
    def konversi(x):
        if jenis == "c2f":
            return (x*9/5)+32
        elif jenis == "f2c":
            return (x-32)*5/9
    return konversi

celcius2Fahrenheit = konverter_suhu("c2f")
print(celcius2Fahrenheit(30))


print("TANTANGAN 4".center(60,"="))
print(" Lambda + Map/Filter ".center(60,"="))
print("""
Diberikan list: angka = [1, 2, 3, 4, 5] 
1. Gunakan map + lambda untuk kuadratkan semua angka. 
2. Gunakan filter + lambda untuk ambil angka > 3. 
Contoh Output: 
python 
[1, 4, 9, 16, 25]  # Hasil map 
[4, 5]             # Hasil filter 
""")

#method map() itu gunanya untuk nge apply fungsi kita item2 pada iterable dalam methodnya
#struktur dasar map(function, iterable data) dan tipe object berubah jadi map
#Hasil dari map() bukan langsung sebuah list atau tipe data lain, tetapi sebuah objek iterator. 
angka = [1, 2, 3, 4, 5] 
kuadrat = map(lambda x : x**2, angka)
print(list(kuadrat)) 

lebih3= filter(lambda x: x>3,angka)
print(list(lebih3))

print("TANTANGAN 5".center(60,"="))
print(" Currying: Pembuat Pesan ".center(60,"="))
print("""
Buat fungsi currying pembuat_pesan yang: 
• Tahap 1: Pilih template ("formal"/"casual"). 
• Tahap 2: Masukkan nama. 
• Hasil: 
o formal: "Kepada Yth. {nama}" 
o casual: "Hai {nama}!"          # Hasil filter 
""")

def pembuat_pesan(pesan):
    def nama(nama):
        if pesan == "formal":
            print(f"Kepada Yth. {nama}")
        if pesan == "casual":
            print(f"Hai {nama}")
        
    return nama

pesan_formal=pembuat_pesan("formal")
pesan_casual=pembuat_pesan("casual")

pesan_formal("Bagus")
pesan_casual("Bagus")