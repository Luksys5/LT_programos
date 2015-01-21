#Nurodo pdb strukturos alfa beta strukturas pakeiciant spalva 
#Skirtingi failai perduodami ciklui
#vieni trumpi tik vieno baltymo, kiti keliu baltymu
def spalv(dssp,notdssp,output,count,outkons):
	lines = dssp.readlines()
	betastr = ''
	alfastr = ''
	pavadinimas=''
	alen = 0
	blen = 0
	for y in lines:
               	y = y.rstrip('\n')
               	read = notdssp.readline()
               	if('>' in read):
		#if alfastr != 0 and betastr != 0:
		#	betastr += ' '+str(blen)
		#	alfastr += ' '+str(alen)
			blen = 0
			alen = 0
			pavadinimas += read[1:]
			betastr += bcolors.RESET+'\n'+bcolors.YELLOW+'beta'
			alfastr += bcolors.RESET+'\n'+bcolors.GREEN+'alfa'
			length = 0
			output.write('\n')
                       	output.write(bcolors.RESET+read[1:].rstrip('\n'))
               		beta = 0
			alfa = 0
		else:
			for i in range(0,len(y)):
				output.write(bcolors.BLUE)
				output.write(str(i+1+length)+" "*len(str(i)))
				output.write(bcolors.RESET)
			read = read.rstrip('\n')
        		output.write('\n')
			for i in range(0,len(y)):
                	        if( y[i] == '-'):
                			output.write(bcolors.RESET)
					if( y[i-1] == 'E'):
						betastr += ('-'+str(length+i))
					if( y[i-1] == 'H' and i >0):
						alfastr += ('-'+str(int(length+i))) 
					beta = 0
					alfa = 0
                		elif( y[i]=='E'):
					if(y[i-1]=='H'):
                                        	alfastr += ('-'+str(int(length+i)))
					if beta == 0:
						blen += 1
						beta = 1
						betastr += ' ' + str(length+i+1)
                	        	output.write(bcolors.YELLOW)
					alfa = 0
                	       	else:
					if(y[i-1]=='E'):
                                        	betastr += ('-'+str(int(length+i)))
					beta = 0
                	        	output.write(bcolors.GREEN)
					if alfa == 0:
						alen += 1
						alfa = 1
						alfastr += ' ' + str(length+i+1)
				output.write(read[i]+" "*(len(str(i+length))+(len(str(i+1))-len(read[i]))))
			length += len(y)
		output.write('\n')
	alfal = alfastr.split('\n')
	betal = betastr.split('\n')
	alfal = alfal[1:]
	betal = betal[1:]
	pavlist = pavadinimas.split('\n')
	for i in range(0, len(betal)):
		try:
			outkons.write(pavlist[i]+'\n')
			outkons.write(betal[i]+'\n')
			outkons.write(alfal[i]+'\n')
			output.write(pavlist[i]+'\n')
			output.write(betal[i]+'\n')
			output.write(alfal[i]+'\n')
		except IndexError:
			catch = 1
	return
class bcolors:
	FAIL = '\033[91m'
	BOLD = '\033[95m'
    	BLUE = '\033[94m'
    	GREEN = '\033[92m'
    	YELLOW = '\033[93m'
    	RESET = '\033[0m'
fdssp = open('../atst/atst.dssp','r')
fdnot = open('../atst/atst.notdssp','r')
atstout = open('atst.colored','w')
atstkons = open('atst.kons','w')
atstout.write(bcolors.GREEN + ' Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+'\n')
spalv(fdssp,fdnot,atstout,0,atstkons)
for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outkons = open(str(x)+'.kons','w')
	outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	spalv(f1,f2,outdssp,x,outkons)
