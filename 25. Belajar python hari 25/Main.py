import os
def header():
    print("SELAMAT DATANG".center(60,"="))
    print("PROGRAM PERHITUNGAN".center(60))
    print("Tentukan perhitunan apa yang ingin kamu lakukan dari semua angka masukan".center(60))
    print("""
        - Jumlahin
        - Rata-rata
        - kaliin semua
          """)
def perhitungan(*args:int,**kwargs:str)->int:
    '''Ini fungsi untuk menghitung penjumlahan, rata2, & Perkalian dari semua angka dalam argumen'''
    if kwargs['option'] == 'Jumlahin':
        output = 0
        for angka in args:
           output += angka
    elif kwargs['option'] == 'Rata-rata':
        jumlah = 0
        panjang = len(perhitungan(args))
        for angka in args:
            jumlah += angka
        output = jumlah/panjang
    elif kwargs['option'] == 'kaliin semua':
        output = 1
        for angka in args:
            awal *= angka
    else:
        print(f"Perhitungan tidak ada dalam parameter")
    
    return output
        


def input_user():
    perhitungan = input("Perhitungan apa yang ingin kamu lakukan : (pilih satu dari ketiga di atas)")
    data = []
    while True:
        masukan = int(input("Masukan angkanya: "))
        data.append(masukan)
        cukup = input("Cukup: (y/n)")
        if cukup == 'y':
            break
    
    return data, perhitungan
    
def display(message,data,hasil):
    print(f"Hasil {message} dari {data} adalah {hasil}")

while True:
    os.system('clear')
    header()
    DATA,PERHITUNGAN = input_user()
    print(PERHITUNGAN)
    OUTPUT = perhitungan(*DATA,option=PERHITUNGAN) #kalo semisal data inputnya list dan inputnya *args yang mana hanya menerima kumpulan angka saja maka inputnya ditambah * agar sudah terunpack
    display(PERHITUNGAN,DATA,OUTPUT)
    isContinue = input("Mau akhiri program: (y/n)")
    if isContinue == 'n':
        break