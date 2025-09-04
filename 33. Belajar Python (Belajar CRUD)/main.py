import os
import CRUD as CRUD
if __name__ == "__main__":
    CRUD.init_console() #Cek database ada atau gk
    while True:
        operating_system = os.name
        match operating_system:
            case 'nt' : os.system("cls")
            case 'posix' : os.system('clear')
        print(f"SELAMAT DATANG DI PROGRAM\nDATABASE PERPUSTAKAAN")
        print("="*50)
        print(f"1. Read Data\n2. Create Data\n3. Update Data\n4. Delete Data\n")
        try:
            opsi = input("Masukan Opsi: ")
            match opsi:
                case '1':
                    print("="*120)
                    CRUD.read_console()
                    print("="*120)
                case '2':
                    print("="*120)
                    CRUD.create_console()
                    print("="*120)
                    CRUD.read_console()
                    print("="*120,"\n")
                case '3':
                    print("="*50,"\n")
                    CRUD.update_console()
                    print("="*50,"\n")
                case '4':
                    print("="*50,"\n")
                    CRUD.delete_console()
                    print("="*50,"\n")
                case _:
                    raise TypeError
        except TypeError as e:
            continue
        isDone = input("Program Berakhir? (y/n)")
        if isDone == "y" or isDone == "Y":
            break
    print("\nPROGRAM BERAKHIR")