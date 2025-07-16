import datetime
import os #library operating system fungsinya ngejalanin perintah di terminal 
# Alasan value dari templatenya lengkap dikarenakan 
# agar membantu memahami tipe data yang diharapkan, 
# meskipun nantinya jika menggunakan .fromkeys, yang diduplikat hanya key dari dict-nya saja tidak 
# dengan valuenya, value hasil dari duplikat dengan from keys itu isinya none
mahasiswa_template = {  
    'nama':'nama',  
    'nim':'00000000',
    'sks_lulus':0,
    'lahir': datetime.datetime(1111,1,11)
}

data_mahasiswa={}#

#membersihkan layar, menghilangkan 
#semua teks yang ditampilkan dan memberikan tampilan baru yang bersih



# dict.fromkeys()
# Membuat dictionary baru dengan:
KEY = 0
# Value: Default None (karena tidak ditentukan)
while True:
    os.system('clear')
    KEY += 1
    mahasiswa = dict.fromkeys(mahasiswa_template.keys()) 
# Apa yang Terjadi?
# mahasiswa_template.keys()
# Mengambil semua key dari template: 
# ['nama', 'nim', 'sks_lulus', 'lahir']
    print("SELAMAT DATANG".center(40,"="))
    print(f"{'Program Database Mahasiswa':^40}")
    print("-"*40)  
    mahasiswa['nama'] = input("Masukan nama Mahasiswa: ")
    mahasiswa['nim'] = input("Masukan NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("Masukan SKS lulus Mahasiswa: "))
    TAHUN = int(input("Masukan tahun lahir mahasiswa (YYYY): "))
    while len(str(TAHUN)) > 4:
        TAHUN = int(input("Masukan lagi tahun lahir mahasiswa (YYYY): "))
        while len(str(TAHUN)) < 4:
            TAHUN = int(input("Masukan lagi tahun lahir mahasiswa (YYYY): "))
            if len(str(TAHUN)) == 4:
                break
    while len(str(TAHUN)) < 4:
        TAHUN = int(input("Masukan lagi tahun lahir mahasiswa (YYYY): "))
        while len(str(TAHUN)) > 4:
            TAHUN = int(input("Masukan lagi tahun lahir mahasiswa (YYYY): "))
            if len(str(TAHUN)) == 4:
                break
    BULAN = int(input("Masukan bulan lahir mahasiswa (MM): "))
    TANGGAL = int(input("Masukan tanggal lahir mahasiswa (DD): "))
    mahasiswa['lahir'] = str(datetime.date(TAHUN,BULAN,TANGGAL))
    data_mahasiswa.update({KEY:mahasiswa})
    
    # for id in data_mahasiswa:
    #     KEY = id
    #     data_mahasiswa[]

    print(f"{'Id':<6}| {'Nama':<20}| {'NIM':<13}| {'SKL lulus':<11}| {'Kelahiran':<13}")
    print("-"*75)
    for id_mahasiswa in data_mahasiswa:
        KEY = id_mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKL = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir']
        print(f"{KEY:<6}| {NAMA:<20}| {NIM:<13}| {SKL:<11}| {LAHIR:<13}")
    isInput = input("Mau input data lagi? (y/n)")
    if isInput == 'n':
        break
print("Program Berakhir")