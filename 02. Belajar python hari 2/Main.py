import time

print("Ini adalah program untuk mengukur kasur kamu")
jenis=input("Masukan jenis kasur kamu: ")
panjang=float(input("Panjang Kasur kamu: "))
lebar=float(input("Lebar kasur kamu: "))
tebal=float(input("Tebal kasur kamu: "))

mulai=time.perf_counter()
luas = panjang*lebar
volume = panjang*lebar*tebal
print("Kasur ", jenis, "kamu memiliki luas ", luas, " dan volume ", volume)

end=time.perf_counter()-mulai
print("waktu pemrosesan: ", end)