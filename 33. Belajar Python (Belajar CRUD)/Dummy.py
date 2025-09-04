from CRUD.Database import template,database
import time
#Baca data.txt sebagai data
data_buku = template.copy()
kunci = "wdwda"
data_buku["pk"] = kunci
data_buku["date_add"] = time.strftime("%d-%m-%y (%H:%M:%S)")
data_buku["Penulis"] = "Mr baloba loba"
data_buku["Judul"] = "Loba"
data_buku["Tahun"] = "2014"
data_str = f'{data_buku["pk"]};{data_buku["date_add"]};{data_buku["Penulis"]};{data_buku["Judul"]};{data_buku["Tahun"]}\n'
with open('data.txt','r+') as file:
    lsdata = file.readlines()
    #print(lsdata)
    for a,b in enumerate(lsdata):
          if kunci in b:
            lsdata[a] = data_str
            break
    #print(lsdata)
    file.seek(0) #mindahin posisi pointer open ke awal karakter
    file.writelines(lsdata) #setelah write lines pointer pindah ilustrasinya kyk dibawah
     # [DATA BARU][SISA DATA LAMA YANG MASIH ADA]
    #            ↑ Pointer di sini
    file.truncate()  # POTONG di posisi pointer (akhir data baru)

#with open('data.txt',mode="r+") as file:
 #   lsdata=file.readlines()
  #  print(lsdata)
   # if lsdata[-1] == "\n":
    #    print("ada")
     #   del lsdata[-1]
      #  file.seek(0)
       # file.writelines(lsdata)
        #file.truncate()

kunci = "jbrqQz"
with open('data.txt','r+') as file:
    lsdata = file.readlines()
    for a,b in enumerate(lsdata):
        if kunci in b:
            del lsdata[a]
            file.seek(0)
            file.writelines(lsdata)
            file.truncate()