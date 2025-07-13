sisi = int(input("Masukan nilai besaran ketupat yang kamu inginkan: "))
count = 1 #variabel dummy
spasi = int(sisi/2)
akhir = spasi
print(f"spasi {spasi}")

while True:
    if count%2: #Kalo ganjil hasilnya true
         print(" "*spasi,"+"*count)
         count +=1
         spasi -=1
         continue
    else:
         count +=1
    if count > sisi:
         break

spasi_1=spasi
while True:
    if count%2: #Kalo ganjil hasilnya true
        if spasi_1 == -1:
            print("+"*count)
        else:
            print(" "*spasi_1,"+"*count)
        count -=1
        spasi_1 +=1
        continue
    else:
         count -=1
    if spasi_1 > akhir:
        break