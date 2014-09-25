import glob
fh=open('txt/3seka.txt', 'r')
filenames = glob.glob('*.pdb')
lines=fh.readlines()
visil=0
visif=0
z=0
for y in filenames:
	yikas=y.split('.')
	yra=0
	for x in lines:
        	xikas=x.rstrip('\n')
		if xikas==yikas[0]:
			print 'Yra '+xikas
			visif+=1
			yra=1
		
		z+=1	
		if z==199 and yra==0:
			print 'NERA'
print visif
