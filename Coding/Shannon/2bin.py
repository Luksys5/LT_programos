#!/usr/local/bin/python
import codecs
#from koduoja import *
#from check import *
arr={}
maxas = 0
lengtha = 0
somefile = ""
#arr, somefile = viskas(arr,maxas,lengtha)
#check(arr)
myint = int('100100100010110',2)
mystr = '\u'+str(myint)
f = codecs.open("lol", "w", "utf-8")
f.write(mystr.decode('unicode-escape'))
f.close()
