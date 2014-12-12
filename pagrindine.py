from koduoja, rasofile, check import *
arr={}
maxas = 0
lengtha = 0
somefile = ""
arr, lengtha, somefile = readncalc(arr,lengtha)
arr, maxas = shannon(arr,lengtha,maxas)
pailgina(arr,maxas)
#ftotextf(somefile,arr)
checkfile(somefile)
