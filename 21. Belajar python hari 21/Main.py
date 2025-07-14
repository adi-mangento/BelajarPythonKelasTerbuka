print("TANTANGAN 1".center(40,"="))
print("Looping Keys & Values")
buah = {"apel": 5000, 
        "mangga": 8000, 
        "jeruk": 6000}

key_buah = buah.keys()
print(key_buah)
print("1. Loop untuk mencetak key saja.")
for kb in key_buah:
    print(f"Buah : {kb}")

print("\n2. Loop untuk mencetak value saja.")
value_buah=buah.values()
for vb in value_buah:
    print(f"Harga Buah: {vb}")

print("""\n3. Loop untuk cetak format: "Harga {key} = Rp{value}""")

item_buah = buah.items()
for kb,vb in item_buah:
    print(f"Harga {kb} = Rp {vb}")

print("\n")
print("TANTANGAN 2".center(40,"="))
print("Copy & Pop")
siswa = {"andi": 90, 
         "budi": 85,
         "cindy": 95}
print(siswa,"\n")

print("""1. Duplikat dictionary siswa = {"andi": 90, "budi": 85, "cindy": 95} dengan .copy().""")
dupli_siswa = siswa.copy()
print(f"Asli Siswa :\n {siswa}")
print(f"Duplikat siswa :\n {dupli_siswa}")

print("""2. Hapus data "budi" dari dictionary asli menggunakan .pop().""")
Data_budi=siswa.pop("budi")
print(f"budi : {Data_budi}")
print(f"Asli Siswa :\n {siswa}")
print(f"Duplikat siswa :\n {dupli_siswa}")

print("\n")
print("TANTANGAN 3".center(40,"="))
print("PopItem Challenge")
inventory = {"laptop": 5, "mouse": 10, "keyboard": 7}
print(f"Inventory =\n{inventory}")
print("""
1.	Hapus item terakhir dengan .popitem().
2.	Simpan item yang dihapus ke variabel terakhir.
3.	Cetak inventory dan terakhir.
""")
ItemTerakhir= inventory.popitem()
print(f"Sisa inventory : {inventory}")
print(f"Item terakhir: {ItemTerakhir}")

print("\n")
print("TANTANGAN 4".center(40,"="))
print("Update & Merge Dictionary")
default = {"theme": "dark", "font": "Arial"}  
custom = {"font": "Roboto", "volume": 80}
print(f"Default:\n{default}")
print(f"Custom:\n{custom}")
print("""
1.	Gabungkan custom ke default dengan .update().
2.	Cetak hasilnya.
3.	Jelaskan apa yang terjadi pada key "font"!
""")

default.update(custom)
print(f"Default:\n{default}")

print("\n")
print("TANTANGAN 5".center(40,"="))
print("Items() Magic")
kode_akses = {"admin": "1234", "user": "5678", "guest": "0000"}
print(f"Kode Akses:\n{kode_akses}")
print("""
1.	Gunakan .items() untuk looping.
2.	Cetak format: "Role: {key} | Kode: {value}".
3.	Jika key = "guest", ganti valuenya jadi "9999".
""")
print("1-2")
item_kode = kode_akses.items()
for role,kode in item_kode:
    print(f"Role : {role} | Kode : {kode}")
    if role == "guest":
        kode_akses.update({"guest":9999})

print(kode_akses)