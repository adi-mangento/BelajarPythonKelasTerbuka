Pada hari ke-27 saya belajar mengenai global dan local scope

jadi global dan local scope di python itu apa sih?
Intinya:
- Global: Variabel "umum" yang bisa dipakai di mana saja (tapi risiko side effect).
- Local: Variabel "privat" yang hanya hidup di dalam fungsi.
- global: Keyword untuk modifikasi menjadi variable global di dalam fungsi.
contoh scriptnya
kalo global
nilai = 100  # Global

def cek_nilai():
    print(nilai)  # Bisa dibaca

cek_nilai()  # Output: 100

intinya si varibel nilai bisa diakses

kalo local
def hitung():
    angka = 10  # Variabel lokal
    print(angka)

hitung()  # Output: 10
print(angka)  # Error! Variabel lokal tidak bisa diakses di luar fungsi

nah kalo mau buat variable local jadi global contoh scriptnya:
total = 0  # Global

def tambah():
    global total  # Deklarasi akses ke variabel global
    total += 5

tambah()
print(total)  # Output: 0 kalo semisal gk ada key word global pada fungsi
print(total)  # Output: 5 karena outputnya 5

