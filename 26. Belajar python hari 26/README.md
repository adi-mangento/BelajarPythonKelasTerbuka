Di hari ke-26, saya belajar mengenai lambda dan anonymous function dan currying.
Jadi Lambda function adalah fungsi mini tanpa nama (anonymous function) yang:
- Dibuat dengan kata kunci lambda
- Hanya bisa berisi 1 ekspresi
- Sangat cocok untuk operasi sederhana
beda dengan fungsi seperti menggunakan def yang ada Namanya contoh def fungsi():

struktur dasar dari lambda function itu seperti dibawah:
lambda arguments: expression

contoh penggunaannya
# Fungsi biasa
def kuadrat(x):
    return x ** 2

# Lambda version
kuadrat = lambda x: x ** 2

print(kuadrat(5))  # Output: 25

atau semisal untuk sorting (.sort()), si sort() ini kan fungsinya buat ngurutin data dalam list, ataupun tipe data koleksi lainnya
trus struktur dari sort itu aslinya kyk dibawah
list.sort(key=function)
nah function nya bisa pake fungsi biasa (def) atau lambda

nah contoh pemakaian dengan lambda seperti dibawah

siswa = [("Budi", 90), ("Ani", 85), ("Citra", 95)]
siswa.sort(key=lambda x: x[1])  # Sort berdasarkan nilai
print(siswa)
# Output: [('Ani', 85), ('Budi', 90), ('Citra', 95)

contoh lain penggunaan lambda function biasanya dipakai di method map(), filter(), dan reduce().

Pada function suatu konsep yang Namanya currying 
Currying itu tujuannya mengubah fungsi multi-argumen menjadi rantai fungsi satu argumen yang saling terkait.
contohnya kyk dibawah 
semisal fungsi biasa kan

def buat_makanan(nasi, lauk, sayur):
    return f"Nasi: {nasi}, Lauk: {lauk}, Sayur: {sayur}"

print(buat_makanan("putih", "ayam", "bayam"))  
# Output: "Nasi: putih, Lauk: ayam, Sayur: bayam"

nah kalo pake currying
def mesin_makanan(nasi):
    def tambah_lauk(lauk):
        def tambah_sayur(sayur):
            return f"Nasi: {nasi}, Lauk: {lauk}, Sayur: {sayur}"
        return tambah_sayur
    return tambah_lauk

# Dipanggil bertahap:
makanan = mesin_makanan("merah")("ikan")("kangkung")
print(makanan)  
# Output: "Nasi: merah, Lauk: ikan, Sayur: kangkung"

Setiap fungsi hanya menerima 1 input dan mengembalikan fungsi berikutnya.

currying bisa juga dipakai untuk function lambda, contohnya:

mesin = lambda nasi: lambda lauk: lambda sayur: f"Nasi: {nasi}, Lauk: {lauk}, Sayur: {sayur}"

# Eksekusi:
makanan = mesin("hitam")("tempe")("toge")
print(makanan)  
# Output: "Nasi: hitam, Lauk: tempe, Sayur: toge"
Alur Eksekusi:
- mesin("hitam") → Mengunci argumen nasi="hitam", mengembalikan fungsi lambda lauk: ...
- ("tempe") → Mengunci lauk="tempe", mengembalikan lambda sayur: ...
- ("toge") → Mengisi argumen terakhir, menghasilkan string akhir.

bisa juga gabungan dari fungsi biasa dan lambda:
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}") #ini sama kyk pangkat(2)(5)
pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")

jadi currying ini berguna ketika Anda ingin:
- Membuat fungsi spesifik dari fungsi umum (partial application).
- Menyusun operasi bertahap seperti alur produksi pabrik.
- Menulis kode yang lebih modular dan terisolasi.

Contoh praktis:
# Currying untuk konfigurasi API
def api_client(base_url):
    def set_auth(token):
        def send_request(endpoint):
            print(f"GET {base_url}/{endpoint} [Auth: {token}]")
        return send_request
    return set_auth

# Pakai
production_api = api_client("https://api.example.com")
auth_api = production_api("TOKEN123")
auth_api("users")  # GET https://api.example.com/users [Auth: TOKEN123]

pada currying jgn lupa tiap fungsinya diberi return karena logika kyk dibawah ini

def kotak_ajaib_1(input1):          # Kotak 1: Terima input1
    def kotak_ajaib_2(input2):      # Kotak 2: Terima input2
        def kotak_ajaib_3(input3):  # Kotak 3: Terima input3
            return f"Hasil: {input1}+{input2}+{input3}"
        return kotak_ajaib_3  # ⭐ Keluarkan Kotak 3
    return kotak_ajaib_2      # ⭐ Keluarkan Kotak 2

Tidak ada return kotak_ajaib_1 karena:
Kotak 1 langsung dipanggil sebagai fungsi utama, bukan dihasilkan oleh fungsi lain.
