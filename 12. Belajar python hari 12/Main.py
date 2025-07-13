print("Mari masukan password kamu\n")
pw=input("Bikin Password kamu: ")
pw_login=input("Masukan ulang Password kamu : ")

while pw_login != pw: # != itu kebalikan ==, jadi kalo isinya gk mirip hasilnya true
    print("Password yang kamu masukan salah, masukan ulang")
    pw_login=input("Password : ")

print("Password yang kamu masukan sudah benar")
