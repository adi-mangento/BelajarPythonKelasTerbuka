a=int(input("Masukan angka a : "))
b=int(input("Masukan angka b : "))
print("\n")
print("a : ", a, " --> biner: ", format(a,'08b'))
print("b : ", b, " --> biner: ", format(b,'08b'))
print("\n")
c=a&b
print("a & b : ", c, "-->", format(c,'08b'))
d=a|b
print("a | b : ", d, "-->", format(d,'08b'))
e=a^b
print("a ^ b : ", e, "-->", format(e,'08b'))
f=~a
print("  ~a  : ", f, "-->", format(f,'08b'))
g=~b
print("  ~b  : ", g, "-->", format(g,'08b'))

##################################################

print(12*"=")
a=int(input("Masukan angka :"))
a|=1
print("Langkah 1: a|=1  -->", format(a,'08b'), "(",a,")")
a&=15
print("Langkah 2: a&=15 -->", format(a,'08b'), "(",a,")")
a^=3
print("Langkah 3: a^=3  -->", format(a,'08b'), "(",a,")")
a<<=1
print("Langkah 4: a<<=1 -->", format(a,'08b'), "(",a,")")
a>>=2
print("Langkah 5: a<<=2 -->", format(a,'08b'), "(",a,")")