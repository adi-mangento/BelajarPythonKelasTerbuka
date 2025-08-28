file = open("data.txt", mode="r")  
#mode ini menentukan data ini sebagai apa? Apakah read atau write
#nah cara printnya  
#print(file.read())
print(f"Status Read: {file.readable()}")
print(f"Status Write: {file.writable()}")

print(file.readline(), end="") #baris pertama
print(file.readline()) #baris ketiga

#print(file.readlines())
file.close() #Menutup file 
print(f"file ditutup : {file.closed}") #Mengecek apakah sudah tertutup

print('Membaca dengan with'.center(50, "="))
with open("data.txt", mode="r") as file: #artinya dengan saat ini membuka file data.txt sebagai file, apa yang akan kita lakukan (setelah tanda:)
    content = file.readline()
    print(content)

print(f"file ditutup : {file.closed}")