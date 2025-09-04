from . import Operasi
from . import Database

def delete_console():
    read_console()
    print("Pilih data yang mau dihapus berdasarkan key_id")
    kunci = input("Masukan key_id: ")
    while True:
        if kunci in Database.database:
            with open("data.txt",'r') as file:
                lsdata = file.readlines()
                for a,b in enumerate(lsdata):
                    if kunci in b:
                        data=lsdata[a]
                        data_break = data.split(";")
                        PENULIS = data_break[2]
                        JUDUL = data_break[3]
                        TAHUN = data_break[4]
            break
        else:
            print("Key_id tidak ditemukan")
            kunci = input("masukan Key_id lagi: ")
    print(f"""Berikut data yang mau dihapus
Penulis      : {PENULIS}
Judul        : {JUDUL}
Tahun terbit : {TAHUN}
""")
    isDone= input("Yakin ingin menghapus data tersebut (y/n): ")
    if isDone == "y":
        Operasi.delete_database(kunci)

def create_console():
    print("Masukan data penulis, judul, dan tahun\nuntuk menambahkan ke database")
    penulis = input("Masukan nama penulis: ")
    judul = input("Masukan judul Buku: ")
    tahun = input("Masukan tahun terbit Buku: ")
    Operasi.create(penulis,judul,tahun)

def update_console():
    read_console()
    print("Pilih key_id mana yang mau diupdate")
    kunci = input("Masukan key_id-nya (pastikan karakternya sesuai): ")
    while True:
        if kunci in Database.database:
            with open('data.txt','r') as file:
                lsdata = file.readlines()
                for a,b in enumerate(lsdata):
                    if kunci in b:
                        data=lsdata[a]
                        data_break=data.split(";")
                        PENULIS = data_break[2]
                        JUDUL = data_break[3]
                        TAHUN = data_break[4]
            break
        else:
            print("Key_id tidak ditemukan")
            kunci = input("Masukan lagi key_idnya: ")
    while True:
        print(f"""Penulis      : {PENULIS}
Judul        : {JUDUL}
Tahun terbit : {TAHUN}
""")    
        print("Pilih opsi yang mau diupdate")
        print("1. Penulis\n2. Judul\n3. Tahun terbit")
        OPSI = input("Opsi : ")
        try:
            match OPSI:
                case "1": PENULIS = input("Masukan penulis: ")
                case "2": JUDUL = input("Masukan judul: ")
                case "3": TAHUN = input("Masukan tahun terbit: ")
                case _:
                    raise TypeError
        except TypeError:
            print("Masukan opsi lagi")
            continue
        isDone = input("Sudah selesai updatenya (y/n): ")
        if isDone == "y":
            break
    Operasi.update_database(kunci,PENULIS,JUDUL,TAHUN)


def read_console():
    content=Operasi.read_database()
    print(f"Key_Id".ljust(9),"Waktu terakhir diubah".ljust(26),"Penulis".ljust(20),"  ","Judul".ljust(40),"  ","Tahun Terbit")
    print("-"*120)
    for i in content:
        content_pisah = i.split(";")
        pk = content_pisah[0]
        dateadd = content_pisah[1]
        penulis = content_pisah[2]
        judul = content_pisah[3]
        tahun = content_pisah[4]
        print(f"{pk.ljust(10)}{dateadd.ljust(25)}  {penulis[:30].ljust(20)}    {judul[:30].ljust(40)}    {tahun}") #text[:30] ambil 30 karakter pertama 