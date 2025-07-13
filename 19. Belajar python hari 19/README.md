Di hari 19 saya belajar ada data tipe collection selain list, yaitu tuples dan set
kalo list kan
data = [5,21,2,5,2] #pake kurung siku
datanya punya index dan bisa dimanipulasi

kalo tuples
data = (3,12,5,2,1)
sama seperti list tapi gk bisa dimanipulasi seperti pake append, data[0]= "das", dsb. intinya gk bisa dimanipulasi/dirubah isinya. 
Trus fungsinya buat apa? biar datanya gk berubah semisal kalo dikirim ke program lain, ini nanti ketemu kalo kita make Django, ML, dll

Kalo Set
data = {5,21,2,5,2} #himpunan data
sama kyk list tapi gk ada index, jadi gk ada urutannya. Ini dipake semisal buat statistik
- Menghilangkan duplikat dari sebuah list:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)  # {1, 2, 3, 4, 5}

- Operasi himpunan
A = {1, 2, 3}
B = {3, 4, 5}

# Gabungan (union)
print(A | B)  # {1, 2, 3, 4, 5}

# Irisan (intersection)
print(A & B)  # {3}

# Selisih (difference)
print(A - B)  # {1, 2}

- Pengecekan keanggotaan yang cepat:
if item in my_set:  # Lebih cepat daripada list untuk koleksi besar
    print("Item ditemukan")

