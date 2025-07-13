print("Tantangan 1".center(30,"="))
print("Duplikasi List dengan Modifikasi \n")
asli = [10,20,30,40]
duplikat = asli.copy()
duplikat[0] = 100
asli.append(50)
print(f"List asli \t: {asli}")
print(f"List duplikat \t: {duplikat}\n\n")

print("Tantangan 2".center(30,"="))
print('Nested List & Deep Copy\n')
data_2D = [
    ["Budi", 25, "Programmer"],
    ["Ani", 30, "Designer"],
    ["Citra", 22, "Analyst"]
]

from copy import deepcopy
data_2D_copy = deepcopy(data_2D)
data_2D_copy[1][0] = "Dewi"
member_baru = ["Rudi", 35, "Manager"]
data_2D.append(member_baru)

print(f"asli : {data_2D}")
print(f"duplikat : {data_2D_copy}\n\n")

print("Tantangan 3".center(30,"="))
print("List Comprehension Challenge\n")

angka = [3, 1, 7, 4, 9, 2, 6]
print(f"angka = {angka}")
print([i if i == 7 else 'Ganjil' if i%2 != 0 else i*3 if i%2 == 0 else i for i in angka])
print("\n\n")

print("Tantangan 4".center(30,"="))
print("Looping & Enumerate\n")

buah = ["Apel", "Mangga", "Jeruk", "Anggur"]
for index,item in enumerate(buah):
    if index%2 != 0:
        print(f"Buah {item} ada di posisi ganjil")
    else :
        print(f"buah {item} ada di posisi genap".upper())

print("\n\n")

print("Tantangan 5".center(30,"="))
print("Advanced: Filter Nested List\n")

nilai_siswa = [
    ["Alice", 85, 90],
    ["Bob", 70, 65],
    ["Charlie", 90, 95]
]
#list Comprehension
lulus = [siswa[0]
         for siswa in nilai_siswa
         if (siswa[1]+siswa[2])/2 >= 80
]

print(lulus)

#loop
lulus1=[]
for siswa in nilai_siswa:
    if (siswa[1]+siswa[2])/2 >= 80:
        lulus1.append(siswa[0])

print(lulus1)