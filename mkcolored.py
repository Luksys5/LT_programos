#programa pakeicia antrines strukturos spalva
# E - Beta lakstai pazym geltonai
# H - alfa spirale pazym zaliai
# reikalingi failai:
#	visu grupiu dssp ir ne dssp failai pvz ./dssp/1 ir ./notdssp/1 
# 	atstovu dssp ir nedssp failai atst/atst.dssp
# programos rezultatai matomi tik cat programoje pvz : $ cat 1.colored matysime pirmos grupes nariu nudazytas alfa beta spirales
# Norint pakeisti spalva reikia ideti i funkcija spalv()
def spalv(dssp,notdssp,output,count):
	lines = dssp.readlines()
	for y in lines:
               	y = y.rstrip('\n')
               	read = notdssp.readline()
               	if('>' in read):
                       	output.write('\n'+bcolors.RESET+read.rstrip('\n'))
               	else:
                       	read = read.rstrip('\n')
        		for i in range(0,len(y)):
                	        if( y[i] == '-'):
                			output.write(bcolors.RESET)
                		elif( y[i]=='E'):
                	        	output.write(bcolors.YELLOW)
                	       	else:
                	        	output.write(bcolors.GREEN)
                	        output.write(read[i])
              	output.write('\n')
	return
class bcolors:
  	GREEN = '\033[92m'
  	YELLOW = '\033[93m'
  	BOLD = '\033[91m'
  	RESET = '\033[0m'
fdssp = open('/home/studentas/Downloads/luko/projectx/atst/atst.dssp','r')
fdnot = open('/home/studentas/Downloads/luko/projectx/atst/atst.notdssp','r')
atstout = open('atst.colored','w')
atstout.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
spalv(fdssp,fdnot,atstout,0)
for x in range(1,16):
        f1 = open('/home/studentas/Downloads/luko/projectx/dssp/'+str(x),'r')
        f2 = open('/home/studentas/Downloads/luko/projectx/notdssp/'+str(x),'r')
        outdssp = open(str(x)+'.colored','w')
        outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
        spalv(f1,f2,outdssp,x)
