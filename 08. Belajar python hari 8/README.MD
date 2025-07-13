Di hari ke 8 ini saya belajar if dan else statement
kan sebelumnya bikin program linear aja, alurnya kyk

    input
      |
      v
    aksi
      |
      v
akhir program

nah disini saya belajar bikin program yang gk linear tapi bercabang, alurnya kyk:

Alur 1
    input
      |
      v      true
   kondisi ------->aksi
      |             |
false |             |
      |             |
      v             |
akhir program <-----


ataupun 

alur2
    input
      |
      v      true
   kondisi ------->aksi 1
      |             |
false |             |
      |             |
     aksi 2         |
      |             |
      v             |
akhir program <-----

nah cara untuk bikin program seperti alur 1 yaitu
semisal
input = input("masukan kata apapun")
if input=="monokorobo": #ini pengkondisian, jadi if kondisi:aksi
   print("inputnya monokorobo") #ini aksinya, lalu si print ini ada didalam kondisi si if ini, kalo semisal print-nya tidak ada indentansinya(tab-nya itu loh) maka dia diluar si if-nya 
   print("monokorobo bagus")
print(f"program berakhir {input}")

Ketika di eksekusi jika kamu masukan inputnya monokorobo, maka hasilnya

inputnya monokorobo
monokorobo bagus
program berakhir monokorobo

cuman kalo kamu masukan inputnya selain monokorobo semisal udang, maka hasilnya

program berakhir udang

nah dia gk ngejalanin perintah perintah yang ada di dalem si ifnya itu, langsung ke akhir program



nah cara untuk bikin program seperti alur 2 yaitu
semisal
input = input("masukan kata apapun")
if input=="monokorobo": #ini pengkondisian, jadi if kondisi:aksi
   print("inputnya monokorobo") #ini aksi 1
   print("monokorobo bagus")

else:            #ini pengkondisiannya langsung else:aksi
  print("kata ini bukan monokorobo")
  print("tana pegi")
    
print(f"program berakhir {input}")

Ketika di eksekusi jika kamu masukan inputnya monokorobo, maka hasilnya

inputnya monokorobo
monokorobo bagus
program berakhir monokorobo

nah dia ngejalanin aksi 1
cuman kalo kamu masukan inputnya selain monokorobo semisal udang, maka hasilnya

kata ini bukan monokorobo
tana pegi
program berakhir udang

nah dia gk ngejalanin perintah di aksi 1 tapi, yang di aksi 2




