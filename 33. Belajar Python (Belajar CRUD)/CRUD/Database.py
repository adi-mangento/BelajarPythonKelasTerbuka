from . import Operasi

DB_NAME = 'data.txt'
template = {
    "pk" : "xxxxxx", #keyid
    "date_add" : "xx-xx-xxxx",
    "Penulis" : ""*255,
    "Judul" : ""*255,
    "Tahun" : "xxxx"
    }

database = {}

def init_console():
    try:
        with open(DB_NAME,'r') as file:
            print(file.readlines())
    except:
        Operasi.create_first_time()
