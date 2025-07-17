import os
#fungsinya
def header():
    '''HEADER'''
    print("SELAMAT DATANG".center(50,"="))
    print("PROGRAM MENGHITUNG LUAS & KELILING PERSEGI".center(50))
    print("'".center(50))

def input_user():
    '''buat input panjang dan lebar'''
    PANJANG = int(input("Masukan Panjang Persegi : "))
    LEBAR = int(input("Masukan Lebar Persegi : "))
    return PANJANG,LEBAR

def keliling(p,l):
    ''''buat nentuin keliling persegi'''
    keliling = p*2+l*2
    return keliling

def luas(p,l):
    ''''buat nentuin luas persegi'''
    luas = p*l
    return luas

def opsi():
    ''''buat nentuin mau user mau itung luas atau keliling'''
    hitungmana = input("Kamu mau tahu luas atau kelilingnya: (k/l) ")
    return hitungmana

def display(message,hitung):
    print(f"Hasil perhitungan {message}-nya yaitu : {hitung}")
#programnya
while True:
    os.system('clear')
    header()
    PANJANG,LEBAR = input_user()
    pl= opsi()
    if pl == 'k':
        hitung = keliling(PANJANG,LEBAR)
        display('keliling',hitung)
    elif pl == 'l':
        hitung = luas(PANJANG,LEBAR)
        display('luas',hitung)
    isContinue = input("Apakah masih mau menghitung lagi? (y/n)")
    if isContinue == "n":
        break

print("Program Berakhir")