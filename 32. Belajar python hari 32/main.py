try:
    a1=int(input("Masukan angka Pertama : "))
    operator = input("Masukan Operator (+,-,*,/): ")
    a2=int(input("Masukan angka Kedua : "))
    match operator:
        case "+":
            print(f"Hasilnya {a1+a2}")
        case "-":
            print(f"Hasilnya {a1-a2}")
        case "*":
            print(f"Hasilnya {a1*a2}")
        case "/":
            print(f"Hasilnya {a1/a2}")
        case _:
            raise TypeError("Operator tidak valid")

except ZeroDivisionError:
    print("Error: Tidak bisa bagi dengan nol")

except (ValueError,TypeError) as error:
    print(f"Error : {error}")
        