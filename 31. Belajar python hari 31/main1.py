#===============Tantangan 1==============
with open('data.txt', mode= 'w', encoding='utf-8') as file1:
    file1.write("Ini baris 1\n"
                "ini baris 2\n" \
                "ini baris 3\n" \
                "ini baris 4\n" \
                "ini baris 5"
    )

with open('data.txt', mode= 'r') as file1:
    file1 = file1.readlines()
    jumlah_baris = len(file1)
    print(f"Jumlah baris: {jumlah_baris}")
    if jumlah_baris >3:
        print(f"Baris ke-3: {file1[2]}")

#============== Tantangan 2 ============
with open('source.txt','w', encoding='utf-8') as source:
    source.write("Saya belajar python\n" \
    "Java juga keren\n"
    "python menyenangkan"
    )

with open('filtered.txt', 'w', encoding='utf-8') as filtered:
    source=open('source.txt', 'r')
    list_source=source.readlines()
    source.close()
    duplikat_source= list_source.copy()
    list_filtered=[i for i in duplikat_source if "python" in i]
    for index in list_filtered:
        filtered.write(index)

#========== Tantangan 3 ==========
import datetime as dt
with open('log.txt','w',encoding='utf-8') as log:
    print("Masukan nama dan jam")
while True:
    nama = input('masukan nama kamu: ')
    jam = input('masukan jam: (1-23)')
    menit = input('masukan menit: (1-59)')
    with open('log.txt','a',encoding='utf-8') as log:
        log.write(f"{dt.time(int(jam),int(menit))} {nama} \n")
    isStop = input("Masih mau lanjut: (y/n)")
    if isStop == 'n':
        break

#========= Tantangan 5 ==========
for i in range(1,5):
    with open(f"file{i}.txt", "w", encoding = "utf-8") as file:
        file.write(f'isi file ke-{i}')

for i in range(1,5):
    with open('merged.txt','a', encoding='utf-8') as merged:
        with open(f'file{i}.txt', 'r') as dummy:
            data= dummy.read()
        merged.write(f"===== File {i} =====\n")
        merged.write(f'{data}\n')


            