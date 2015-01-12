import bitarray
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
	bitarr = bitarray.bitarray()
        fw = open("binfile.bin","wb")
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
				bitarr = bitarray.bitarray(dict.get(mystr))
				#for x in range(0,len(newstr)):
				#	fw.write(newstr[x])
				bitarr.tofile(fw)
                                mystr = ""
                        elif y in dict:
				bitarr = bitarray.bitarray(dict.get(mystr))

				bitarr.tofile(fw)
                                mystr = ""

        f.close()
        fw.close()

