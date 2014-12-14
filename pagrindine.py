from koduoja import *
from atkoduoja import decode
from rasofile import *
from check import *
channel = raw_input("Uzkoduoti 1 \nDekoduoti 2\n")
channel = int(channel)
if channel == 1:
	arr={}
	maxas = 0
	lengtha = 0 
	arr,somefile = viskas(arr,lengtha)
	check(arr)
	irasokodus(arr)
	ftotextf(somefile,arr)
	mkbinfile(somefile,arr)
elif channel == 2:
	decode()	
else:
	print 'Netinkamas simbolis.Rasykite 1 arba 2'
#pailgina(arr,maxas)

#mkbinfile(somefile,arr)
#writetofile(arr)
