import datetime
member1={
    'nama':'Acep Nurmagedov',
    'wajah':'Seperti ayah fiona yang kodok di shrek',
    'role':'Pilot',
    'kelahiran':datetime.datetime(1987,3,12)
}
member2={
    'nama':'Faris Alfaridzi',
    'wajah':'Lonjong',
    'role':'GCS',
    'kelahiran':datetime.datetime(1999,4,4)
}

member3={
    'nama':'Jhon Cena',
    'wajah':'Biasa saja seperti bule',
    'role':'Rahasia',
    'kelahiran':datetime.datetime(2000,7,15)
}
data_tim = {
    'SR01':member1,
    'SR02':member2,
    'SR03':member3
}
print(f"{'ID':<6} {'Nama':<20} {'Wajah':<45} {'Role':<10} {'Kelahiran':<10}")
print("-"*100)
for member in data_tim:
    KEY = member
    NAMA = data_tim[KEY]['nama']
    WAJAH = data_tim[KEY]['wajah']
    ROLE = data_tim[KEY]['role']
    LAHIR = data_tim[KEY]['kelahiran'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<20} {WAJAH:<45} {ROLE:<10} {LAHIR:<10}")