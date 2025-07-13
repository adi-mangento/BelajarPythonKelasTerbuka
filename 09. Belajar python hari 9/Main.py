print("""
 NILAI          MUTU
90 - 100         A
80 - 89          B
70 - 79          C
60 - 69          D
  <60            E      
""")
 
masukan = int(input("Masukan nilai kamu!!! nanti aku tentuin nilainya = "))

if masukan < 0:
    print("Gak tau mutunya berapa, soalnya kamu masukinnya di bawah 0")
elif masukan < 60:
    print("Nilai kamu E")
elif masukan <= 69:
    print("Nilai kamu D")
elif masukan <= 79:
    print("Nilai kamu C")
elif masukan <= 89:
    print("Nilai kamu B")
elif masukan <= 100:
    print("Nilai kamu A")
else:
    print("kamu gk masukin nilai dengan rentang 0 - 100")

print("Program Berakhir")