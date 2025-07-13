Di Hari ke 4 saya belajar Bitwise operator (Operasi Biner), operator assignment

Jadi gini bitwise itu operasi pada masing2 bit
misalkan ada angka integer:
2,bit nya         _ _ _ _ _ _ _ _ ada 8 bit
untuk bitnya jadi 0 0 0 0 0 0 1 0 , kenapa begitu
karena tiap indexnya(dalam hal ini di lambangkan underscore)  itu ada pangkatnya
                  7 6 5 4 3 2 1 0 jadi kalua dua berarti 2^1
Kalau int-nya 1 berarti
                  0 0 0 0 0 0 0 1 itu berarti 2^0, nah 2^0 itu 1
kalau int-nya 9 berarti
                  0 0 0 0 1 0 0 1 itu berarti
                         2^3   2^0 jadi 2^3 + 2^0 = 8 + 1 = 9
Jadi bitwise itu operasi biner semisal
ada or (|), or yang disini penggunaanna beda untuk yang Boolean contohnya:

2 | 1 --> 0 0 0 0 0 0 1 0 ini untuk dua
          0 0 0 0 0 0 0 1 ini untuk satu, nah data di or kan, disini logika or-nya sama seperti diboolean jika salah satu true atau dalam hal ini 1 maka hasilnya 1
         __________________ or  |
          0 0 0 0 0 0 1 1  jadi nya 2^1 + 2^0 = 3
nah untuk melihat binary int objek caranya yaitu format(objek,'08b')

untuk operator bitwise selain OR (|), ada juga AND (&), logika nya seperti di Boolean, contoh
a = 9     0 0 0 0 1 0 0 1
b = 5     0 0 0 0 0 1 0 1
         _________________ &
a & b     0 0 0 0 0 0 0 1   hasil dari a & b adalah 1, karena 2^0

ada juga XOR (^), logikanya sama seperti di Boolean, contoh
a = 9     0 0 0 0 1 0 0 1
b = 5     0 0 0 0 0 1 0 1
          _________________ ^
a ^ b     0 0 0 0 1 1 0 0   hasil dari a ^ b adalah 12 karena 2^3 + 2^2 = 12

ada juga bitwise not (~) logikanya nya yaitu bukan "not logika", tapi "balik semua bit"

Karena Python pakai two's complement, maka hasilnya otomatis jadi negatif/positif sesuai bit paling kiri kalau 1 negative kalau 0 positif. untuk lengkapnya bisa tanya ChatGPT
untuk contohnya
x	~x	Penjelasan
0	-1	~0 = -0 - 1 = -1
1	-2	~1 = -1 - 1 = -2
9	-10	~9 = -9 - 1 = -10
-5	4	~(-5) = -(-5) - 1 = 5 - 1 = 4 

Lalu di bitwsise operator ada shifting yaitu menggeser bit di indexnya
ada shift right (>>), semisal 
a = 9   0 0 0 0 1 0 0 1
b = 9 >> 1 , itu artinya geser 1 kali ke kanan, maka hasilnya adalah
        0 0 0 0 0 1 0 0 yang mana nilanya adalah 4
kalau 9 >> 2, itu artinya gesernya 2 kali ke kanan, maka hasilnya adalah
        0 0 0 0 0 0 1 0 yang mana nilaunya adalah 2
kemudian ado shift left (<<), semisal
a = 9   0 0 0 0 1 0 0 1
b = 9 << 2 , itu artinya geser 2 kali ke kiri, maka hasilnya adalah
        0 0 1 0 0 1 0 0 yang mana nilainya adalah 36

Operator assignment, jadi operasi yang dilakukan dengan penyingkatan atau operasi ditambah dengan assignment 

kalau assignment biaskana biasanya
a = 5 
nah kalau assignment operator
a += 1 #ini artinya adalah a = a + 1 
a -= 2 #ini artinya adalah a = a -2
operator assignment tidak hanya untuk + dan - saja tapi, bisa untuk operasi aritmatika lain yang sudah dipelajari di hari sebelumnya. Assignment ke bitwise ataupun biner, contoh
c = True
c |= false, maka berdasarkan logikanya hasilnya True, karena or

atau semisal
d = 0b0100 , ini nilainya 4 
lalu di shift ke kanan
d >>= 2 
maka hasilnya 0001 , karena geser 2 kali, dan nilainya ada 1

Tantangan
Masukkan angka a: 9
Masukkan angka b: 5

a (dec): 9  → biner: 00001001
b (dec): 5  → biner: 00000101

a & b : 1   → 00000001
a | b : 13  → 00001101
a ^ b : 12  → 00001100
~a    : -10 → 11110110
~b    : -6  → 11111010

=======
Masukkan angka: 6

Langkah 1: a |= 1  → 00000111 (7)
Langkah 2: a &= 15 → 00000111 (7)
Langkah 3: a ^= 3  → 00000100 (4)
Langkah 4: a <<= 1 → 00001000 (8)
Langkah 5: a >>= 2 → 00000010 (2)


