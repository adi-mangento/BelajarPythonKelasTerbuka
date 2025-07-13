print("Tantangan 1".center(40,"="))
print("Operasi CRUD Dictionary")
buku = {
    'judul':"Belajar Python",
    'harga':50000
        }

print(f"Buku: \n{buku}")
buku.update({
    'harga':75000,
    'stok':10
})
print(f"1. Update harga jadi 7500 dan tambah key stok dengan nilai 10:\n{buku}")
del buku["harga"]
print(f"""2. Hpus key 'harga': \n {buku}""")

print("Tantangan 2".center(40,"="))
print("Cek Key & Handle Missing Key")
user = {"id": "U123", "level": "basic"} 
print(user)
IsAdaEmail = "email" in user
print(f"1. Apakah ada key email pada dictionary: {IsAdaEmail}")
user.update({"email": "default@mail.com"})
print(f"2. Sekarang udh ada key email: \n{user}")

print("Tantangan 3".center(40,"="))
print("Merge Dua Dictionary")
default_setting = {"theme": "light", "font": "Arial"}  
user_setting = {"font": "Roboto", "notif": True}  
print(default_setting)
print(user_setting)
default_setting.update(user_setting)
print(f"Sudah diupdate: \n {default_setting}")

print("Tantangan 4".center(40,"="))
print("Akses Value dengan .get()")
stock = {"pensil": 20, "penghapus": 5}  
print(stock)
cek_pensil = stock.get("pensil",0)
cek_spidol = stock.get("spidol","Barang tidak ada")

print(f"Stok Pensil: {cek_pensil}")
print(f"Stok Spidol: {cek_spidol}")


print("Tantangan 5".center(40,"="))
print("Dictionary dari Dua List")
keys = ["nama", "umur", "kota"]  
values = ["Dina", 25, "Bandung"]  

data = {keys[0]:values[0],
        keys[1]:values[1],
        keys[2]:values[2]
        }

print(data)