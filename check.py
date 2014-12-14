def checkfile(myfile):
        f=open(myfile,'r')
        lines = f.readlines()
        fw= open("checking","w")
        for x in lines:
                fw.write(x)
def check(dict):
        all = 0
        for x in dict:
                x = x.rstrip('\n')
                try:
                        all += dict.get(x)
                except TypeError:
                        all = -1
                print x,dict.get(x),len(str(dict.get(x)))
        if all != -1:
                print all
def printdict(dict):
        f = open('out','w')
        for x in dict:
                f.write(x+" "+str(dict.get(x))+str(len(dict.get(x)))+'\n')
        f.close()
        return
def keyval(dict,smth):
	if smth in dict.values():
		print smth, ' yra'
	for key, value in dict.iteritems():
		print 'key ', key, 'value ', value
	return
