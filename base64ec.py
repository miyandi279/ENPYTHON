from base64 import *
import os

os.system('clear')
#Membuat input data
msk = raw_input("Masukkan Text : ")
#Membuat Encrypt Code base64
enc = b64encode(msk)
#Membuat Output
print "Hasilnya adalah:",enc
