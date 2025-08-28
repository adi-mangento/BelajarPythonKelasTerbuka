from . import version  #ngambil dari __init__
from . import operasi
print('ini main')

# alternatif kalo mau __init__.py nya kosong
# from .matematika import operasi
# from .sains import fisika

print(operasi.kali(1,3))
print(version)