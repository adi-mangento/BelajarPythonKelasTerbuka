print("TANTANGAN 1".center(60,"="))
print("Akses Variabel Global".center(60,"="))

print("""
Buat program dengan:  
- Variabel global `nama = "Budi"`.   
- Fungsi `sapa()` yang mencetak `"Halo, {nama}!"` (tanpa parameter).  
- Panggil fungsi dan cetak variabel `nama` di luar fungsi.  
      """)

nama = "budi"
def sapa():
    print(f"Halo, {nama}")

sapa()
print(nama, '\n')

print("TANTANGAN 2".center(60,"="))
print("Modifikasi Variabel Global".center(60,"="))

print("""
Diberikan:   
```python 
counter = 0  # Global 
```   
1. Buat fungsi `tambah_counter()` yang menambah `counter` dengan 1 (gunakan 
`global`).   
2. Panggil fungsi 3x, lalu cetak `counter`. 
      """)

counter = 0 
print(counter)
def tambah_counter():
    global counter
    counter += 1

tambah_counter()
tambah_counter()
tambah_counter()
print(counter, "\n")


print("TANTANGAN 3".center(60,"="))
print("Variabel Lokal vs Global".center(60,"="))

print("""
Buat program dengan:   
- Variabel global `x = 10`.   
- Fungsi `ubah_x()` yang membuat variabel lokal `x = 20` (tanpa `global`).   
- Cetak `x` sebelum, di dalam, dan setelah panggil fungsi.    
      """)

x = 10
def ubah_x():
    x = 20
print(f"sebelum : {x}")
print(x)
print("didalam fungsi x=20")
print(f"setelah : {x}")
ubah_x()
print(x, "\n")

print("TANTANGAN 4".center(60,"="))
print("Scope Bersarang".center(60,"="))

print("""
Buat fungsi `luar()` yang:   
1. Memiliki variabel lokal `y = 5`.   
2. Berisi fungsi `dalam()` yang mengakses `y` dan mencetaknya.   
3. Panggil `dalam()` dari `luar()`.      
      """)

def luar():
    y = 5
    def dalam ():
        print(y)
    dalam()

luar()
