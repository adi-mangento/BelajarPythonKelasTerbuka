list_member=[]
while True:
    nama = input("Masukan Nama : ")
    hobi = input("Masukan Hobi : ")
    member = [nama,hobi]
    list_member.append(member)
    for index,member in enumerate(list_member):
        print(f"Yang ke-{index+1} Namanya si {member[0]} dan hobinya {member[1]}")
    
    isLanjut = input("Masih Mau lanjut (y/n): ")

    if isLanjut == "n":
        break

print("program berakhir".upper())
