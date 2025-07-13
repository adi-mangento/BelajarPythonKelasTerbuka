import datetime as dt

print("Masukan tanggal lahir kamu".center(50,"="))
tanggal = int(input("Masukan tanggal \t: "))
bulan = int(input("Masukan bulan \t\t: "))
tahun = int(input("Masukan tahun \t\t: "))

ttl = dt.date(tahun,bulan,tanggal)
print(ttl)
print(f"Tanggal lahir anda {ttl}")
print(f"Harinya adalah {ttl:%A}")
tanggal_ini = dt.date.today()
print(f"Hari ini adalah {tanggal_ini}")
umur=tanggal_ini-ttl
umur_hari=umur.days
umur_tahun=umur_hari//365
sisa_bulan_umur=(umur_hari%365)//30
print(f"Umur kamu sekarang {umur_tahun} tahun, {sisa_bulan_umur} bulan")