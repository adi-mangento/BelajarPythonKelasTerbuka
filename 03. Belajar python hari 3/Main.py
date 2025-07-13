import time
print("----0++++5----8++++11----")
angka1=float(input("tolong maasukan angka dengan rentang 0 sampai 5 atau 8 sampai 11: "))

mulai=time.perf_counter()
#----0++++5----
LebihDari_0= angka1 > 0
print("input lebih dari 0: ", LebihDari_0)
KurangDari_5= angka1< 5
print("input kurang dari 5: ", KurangDari_5)
Antara_0_dan_5= LebihDari_0 and KurangDari_5
print("input antara 0 sampai 5 :", Antara_0_dan_5)

#---8++++11----
LebihDari_8= angka1 > 8
print("input lebih dari 8: ", LebihDari_8)
KurangDari_11= angka1 < 11
print("input kurang dari 11:", KurangDari_11)
Antara_8_dan_11= LebihDari_8 and KurangDari_11
print("input antara 8 sampai 11:", Antara_8_dan_11)

#----0++++5----8++++11----
hasil1= Antara_0_dan_5 or Antara_8_dan_11
print(2*"\n",10*"=")
print("angka yang dimasukan: ", hasil1)

akhir=time.perf_counter()-mulai
print("waktu pemrosesan: ", akhir)

print(2*"\n",10*"=")

#++++0----5++++8----11++++
print("++++0----5++++8----11++++")
angka2= float(input("Masukan angka dibawah 0 atau rentang 5 sampai 8 atau lebih dari 11: "))

#++++0----
KurangDari_0= angka2 < 0
print("input kurang dari 0:", KurangDari_0)
#----5++++
LebihDari_5= angka2 > 5
print("input lebih dari 5:", LebihDari_5)
#++++0----5++++
KurangDari_0_atau_LebihDari_5= KurangDari_0 or LebihDari_5
print("input kurang dari 0 atah lebih dari 5: ", KurangDari_0_atau_LebihDari_5)

#+++8----
KurangDari_8= angka2 < 8
print("input kurang dari 8:", KurangDari_8)

#---11++++
LebihDari_11= angka2 > 11
print("input lebih dari 11: ",  LebihDari_11)

#+++8----11++++
KurangDari_8_atau_LebihDari_11= KurangDari_8 or LebihDari_11
print("Input kurang dari 8 atau lebih dari 11", KurangDari_8_atau_LebihDari_11)

#---5++++8----
Antara_5_dan_8= LebihDari_5 and KurangDari_8
print("input 5 sampai 8: ", Antara_5_dan_8)

#++++0----5++++8----
KurangDari_0_atau_Antara_5_dan_8=KurangDari_0 or Antara_5_dan_8
print("(Kurang Dari 0) atau (Antara 5 dan 8): ", KurangDari_0_atau_Antara_5_dan_8)

#---5++++8----11++++
LebihDari_5_atau_KurangDari_8_atau_LebihDari_11= LebihDari_5 or KurangDari_8_atau_LebihDari_11
print("(Lebih dari 5) atau (kurang dari 8 atau lebih dari 11): ", LebihDari_5_atau_KurangDari_8_atau_LebihDari_11)

#(++++0----5++++8--)(--11++++)
KurangDari_0_atau_Antara_5_dan_8_atw_LebihDari_11= KurangDari_0_atau_Antara_5_dan_8 or LebihDari_11
print("((Kurang Dari 0)atau (Antara 5 dan 8)) atw (Lebih Dari 11) :", KurangDari_0_atau_Antara_5_dan_8_atw_LebihDari_11)

#(++++0--)(--5++++8----11++++)
KurangDari_0_atw_LebihDari_5_atau_KurangDari_8_atau_LebihDari_11= KurangDari_0 or LebihDari_5_atau_KurangDari_8_atau_LebihDari_11
print("(kurang dari 0) atw ((Lebih dari 5) atau (kurang dari 8 atau lebih dari 11))", KurangDari_0_atw_LebihDari_5_atau_KurangDari_8_atau_LebihDari_11)

hasil2= KurangDari_0_atau_Antara_5_dan_8_atw_LebihDari_11 and KurangDari_0_atw_LebihDari_5_atau_KurangDari_8_atau_LebihDari_11
print(2*"\n",10*"=")

print("angka yang dimasukan: ", hasil2)