print("Kalkulator Sederhana".center(50,"="))
print("\n Masukan angka dan operasinya ( + , - , * , / )")
a = float(input("Masukan Angka\t:\t\t"))
b = float(input("Masukan Angka\t:\t\t"))
print("_".center(50,"_"))
operasi = input("Masukan Operasi\t:\t\t\t ")

if operasi=="+":
    hasil = a + b
    print(f"{a} + {b} = {hasil}")
elif operasi=="-":
    hasil = a - b
    print(f"{a} - {b} = {hasil}")
elif operasi=="*":
    hasil = a * b
    print(f"{a} * {b} = {hasil}")
elif operasi=="*":
    hasil = a * b
    print(f"{a} * {b} = {hasil}")
else:
    print("Kamu gk masukan operasi yang sesuai")
print("program berakhir")