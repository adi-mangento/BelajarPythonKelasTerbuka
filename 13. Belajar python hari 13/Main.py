print("Tantangan".center(40,"="))
print("Kalo angka 4 dan 7 pasti dilewati")
angka = 0
berenti = int(input("mau berenti di angka berapa : "))
while True:
    angka += 1
    if angka == 4:
        print("nice")
        continue
    elif angka == 7:
        print("nice")
        continue
    elif angka == 1:
        pass
    elif angka == berenti:
        print(f"Angka Sekarang -> {angka}")
        break
    print(f"Angka Sekarang -> {angka}")

print("cukup")