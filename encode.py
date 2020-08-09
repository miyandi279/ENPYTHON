#bin/python
#bin/python2
#bin/base64
#code by mr.riskis7
#yt : riskis7 channel
#team : bengkulu cyber team security


#baca_sistem
#open("C:\\hasil.py")
#with open("hasil.py") as f:
  
  
import base64,marshal,os,click
from uncompyle6 import main

class Zurus:
	def __init__(self,fil,jum):
		self.file=fil
		self.cout=0
		self.jml=jum
		self.mars(open(fil,'r').read())

	def mars(self,strg):
		risep=compile(strg,'<script>','exec')
		risepsep=marshal.dumps(risep)
		xxx=f"#code by mr.riskis7\n\nimport marshal\nexec(marshal.loads({risepsep}))"
		if self.cout == self.jml:
			with open(self.file.replace('.py','encode.py'),'w') as com:
				com.write(xxx)
			print(f"[+] File tersimpan: {self.file.replace('.py','encode.py')}")
			return True
		self.bes(xxx)

	def bes(self,strg):
		en=base64.b64encode(bytes(strg,'utf-8'))
		de=f"import base64\nexec(base64.b64decode({en}).decode('utf-8','ignore'))"
		self.cout+=1
		self.mars(de)

os.system('clear')
print("""code by mr.riskis7""")
try:
	ofile=input("[?] File : ")
	juml=int(input("[?] Jumlah encode: "))
	if juml > 10:
		click.pause("[WARM] selesai [ENTER]")
	Com(ofile,juml)
	pil=input("[?] Encode ke sistem bytes  (y/n) ")
	if pil.lower() == 'y':
		main.compile_file(ofile.replace('.py','encode.py'))
		print("[selesai gan]")
	else:
		print("[coba dibuka #lihat perintah diatas]")
except KeyboardInterrupt:
	print("[Key Interrupt]")
except Exception as F:
	print(f"[Err] {str(F)}")
  
  
  
  
