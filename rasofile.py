import bitarray
import os, subprocess
def irasokodus(dict):
        f = open("kodai","w")
        for x in dict:
                f.write(x+"+"+dict.get(x)+"\n")
        f.close()
def ftotextf(mf,dict):
        mystr = ""
        fw = open("newfile","w")
        with open(mf) as f:
                while True:
                        y = f.read(1)
                        if not y:
                                return
                        try :
                                mystr += y
                        except TypeError:
                                mystr += str(y)
                        if mystr in dict:
                                fw.write(dict.get(mystr))
                                mystr = ""
                        elif y in dict:
                                fw.write(dict.get(y))
                                mystr = ""

        f.close()
        fw.close()

def mkbinfile(mf,dict):
        mystr = ""
	stop = 0
	os.system('rm -f binfile.bin')
	longstring = ''
        with open(mf) as f:
                while True:
                        y = f.read(1)
                        if not y:
                        	stop=1
			try :
                                mystr += y
                        except TypeError:
                                mystr += str(y)
                        if mystr in dict:
				#bitarr += bitarray.bitarray(dict.get(mystr))
				#for x in range(0,len(newstr)):
				#	fw.write(newstr[x])
                                longstring += dict.get(mystr)
				mystr = ""
                        elif y in dict:
				longstring += dict.get(y)
                                mystr = ""
			if stop == 1:
				bitarr = bitarray.bitarray(longstring)
				with open('binfile.bin','wb') as fw:
					bitarr.tofile(fw)
				return
        f.close()
        fw.close()

