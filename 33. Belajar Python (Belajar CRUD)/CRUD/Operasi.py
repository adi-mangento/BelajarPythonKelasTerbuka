from . import Database
from .utils import random_string
import time


def delete_database(kunci):
    with open('data.txt','r+') as file:
        lsdata = file.readlines()
        for a,b in enumerate(lsdata):
            if kunci in b:
                del lsdata[a]
                file.seek(0)
                file.writelines(lsdata)
                file.truncate()

def update_database(kunci,penulis,judul,tahun):
    data_buku = Database.template.copy()
    data_buku["pk"] = kunci
    data_buku["date_add"] = time.strftime("%d-%m-%y (%H:%M:%S)")
    data_buku["Penulis"] = penulis
    data_buku["Judul"] = judul
    data_buku["Tahun"] = tahun
    data_str = f'{data_buku["pk"]};{data_buku["date_add"]};{data_buku["Penulis"]};{data_buku["Judul"]};{data_buku["Tahun"]}\n'
    with open('data.txt','r+') as file:
        lsdata = file.readlines()
        for a,b in enumerate(lsdata):
            if kunci in b:
                lsdata[a]=data_str
                break
        file.seek(0) #mindahin posisi pointer open ke awal karakter kalo file.seek(5) berarti mindahin pointer ke 5 karakter awal
        file.writelines(lsdata) #setelah write lines pointer pindah ilustrasinya kyk dibawah
     # [DATA BARU][SISA DATA LAMA YANG MASIH ADA]
    #            ↑ Pointer di sini
        file.truncate()  # POTONG di posisi pointer (akhir data baru)
    ubah_data2database()

def create(penulis:str,judul:str,tahun:str):
    data_buku = Database.template.copy()
    data_buku["pk"] = random_string(6) #bikin string acak dengan len 6
    data_buku["date_add"] = time.strftime("%d-%m-%y (%H:%M:%S)")
    data_buku["Penulis"] = penulis
    data_buku["Judul"] = judul
    data_buku["Tahun"] = tahun
    data_str = f'{data_buku["pk"]};{data_buku["date_add"]};{data_buku["Penulis"]};{data_buku["Judul"]};{data_buku["Tahun"]}\n'
    try:
        with open(Database.DB_NAME,'a',encoding='utf-8') as file:
            file.write(data_str)
        ubah_data2database()
    except:
        print("Gagal boss") 

def create_first_time():
    print("Database tidak ditemukan\nmasukan data di bawah ini untuk membuat database baru")
    penulis = input("Masukan nama Penulis: ")
    judul = input("Masukan judul buku: ")
    tahun = input("Masukan tahun terbit buku: ")
    data_buku = Database.template.copy()
    data_buku["pk"] = random_string(6) #bikin string acak dengan len 6
    data_buku["date_add"] = time.strftime("%d-%m-%y (%H:%M:%S)")
    data_buku["Penulis"] = penulis
    data_buku["Judul"] = judul
    data_buku["Tahun"] = tahun
    data_str = f'{data_buku["pk"]};{data_buku["date_add"]};{data_buku["Penulis"]};{data_buku["Judul"]};{data_buku["Tahun"]}\n'
    try:
        with open(Database.DB_NAME,'w',encoding='utf-8') as file:
            file.write(data_str)
        ubah_data2database()
    except:
        print("Gagal boss")


def read_database():
    try:
        apus_end()
        with open('data.txt','r') as file:
            content=file.readlines() #hasilnya list tiap baris
            ubah_data2database()
            return content

    except:
        print("Gagal baca file")



def ubah_data2database():
    try:
        apus_end()
        with open('data.txt','r') as file:
            content=file.readlines() #hasilnya list tiap baris
            #Update Database
            for buku in content:
                data_buku = Database.template.copy()
                atribut_buku_break = buku.split(";")
                KEY = atribut_buku_break[0]
                data_buku["pk"] = atribut_buku_break[0]
                data_buku["date_add"] = atribut_buku_break[1]
                data_buku["Penulis"] = atribut_buku_break[2]
                data_buku["Judul"] = atribut_buku_break[3]
                data_buku["Tahun"] = atribut_buku_break[4]
                Database.database.update({KEY:data_buku})
            
    except:
        print("Gagal ubah data ke database")

def apus_end():
    with open('data.txt',mode="r+") as file:
        lsdata=file.readlines()
        if lsdata[-1] == "\n":
            del lsdata[-1]
            file.seek(0)
            file.writelines(lsdata)
            file.truncate()