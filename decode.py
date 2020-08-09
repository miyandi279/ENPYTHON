#code by : Miyandi Riski A
#Team    : Bengkulu Cyber Team Sec

from uncompyle6.main import decompile
import marshal,time,sys,os,marcode

def Ey3():
	c=input("[*] decompile marshal python 3.7.X\n[?] File output: ")
	x=marshal.loads(marcode.py3)
	xx=decompile(3.7,x,sys.stdout)
	with open(c+".py","w") as f:
		f.write(xxx)
	print("\n\n[result] Saved as \033[95m%s.py"%(c))

try:
	os.system('clear')
	print("""code by : Miyandi Riski A
		""")
	if sys.version[0] in '3':
		Py3()
except Exception as F:
	print("Err: %s"%(F))
