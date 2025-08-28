with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny ")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append")


with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("otong") # menimpa isi text sesuai dengan panjang data

