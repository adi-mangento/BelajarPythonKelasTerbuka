#disini saya belajar cara kerja program dan bedanya eksekusi file python tanpa dicompile dan tidak
#file Main.py ini filenya tidak dicompile
#perbedaan kalau di compile terlebih dahulu eksekusi file pythonnya akan lebih cepat
import time #library time fungsinya untuk ngukur waktu eksekusi file python
star_time=time.perf_counter()
print("Maramumaku")
print(20000-23123132)
print(time.perf_counter()-star_time)

# hasil yang gk di compile itu
# memakan waktu 0.0007463000001735054 detik
# cara compile file pythonnya ke bentuk bytecode caranya yaitu pakai library pycompile
# di terminal ketik python -m py_compile filepynya.py
# eksekusi file yang udh di compile caranya yaitu diterminal eksekusi file yang udh dicompile