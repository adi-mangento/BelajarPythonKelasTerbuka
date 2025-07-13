print("Masukan 5 hobi kamu".center(60,"="))
hobi=input("Coba Hobi kamu apa aja!!! tolong buat pemisahnya pake koma aja : ")
hobi_pisah=hobi.split(', ')
for i in hobi_pisah:
    print(f"Hobi kamu soal {i}, sangat cupu")