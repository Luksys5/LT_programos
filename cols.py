#Nurodo pdb strukturos alfa beta strukturas pakeiciant spalva 
#Skirtingi failai perduodami ciklui
#vieni trumpi tik vieno baltymo, kiti keliu baltymu
def spalv(dssp,notdssp,output,count):
	lines = dssp.readlines()
	oneline =''
	mt = 0
	alfa = []
	beta = []
	for y in lines:
               	y = y.rstrip('\n')
               	read = notdssp.readline()
               	if('>' in read):
			length = 0
			mt = 0
			if beta != []:
				output.write(x for x in beta )
				output.write('\n')
				return
			output.write('\n')
                       	output.write(bcolors.RESET+read)
			alfa = []
			beta = []
               	else:
			output.write('\n')
			for i in range(0,len(y)):
				output.write(bcolors.BLUE)
				output.write(str(i+length)+" "*len(str(i)))
				output.write(bcolors.RESET)
			read = read.rstrip('\n')
			output.write('\n')
        		for i in range(0,len(y)):
                	        if( y[i] == '-'):
                			output.write(bcolors.RESET)
					if len(beta) % 2 == 1:
					#	beta[len(beta)-1] = str(beta[len(beta)-1]) + str(mt-1)
						beta.append(str(mt-1)+" ")
                		elif( y[i]=='E'):
					if len(beta) % 2 == 0:
						beta.append(str(mt)+"-")
                	        	output.write(bcolors.YELLOW)
                	       	else:
                	        	output.write(bcolors.GREEN)
				#	if len(beta) % 2 == 1:
                                 #               beta[len(beta)-1] = str(beta[len(beta)-1]) + str(mt)
				mt +=1 
				output.write(read[i]+" "*(len(str(i+length))+(len(str(i))-len(read[i]))))
			length += len(y)
		oneline = ''
              	output.write('\n')
	return
class bcolors:
	FAIL = '\033[91m'
	BOLD = '\033[95m'
    	BLUE = '\033[94m'
    	GREEN = '\033[92m'
    	YELLOW = '\033[93m'
    	RESET = '\033[0m'
	#YELLOW='\e[0;33m'
	#BOLD='\e[4;36m'
	#GREEN='\e[0;32m'
	#RESET='\e[0m'
fdssp = open('../atst/atst.dssp','r')
fdnot = open('../atst/atst.notdssp','r')
atstout = open('atst.colored','w')
atstout.write(bcolors.GREEN + ' Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+'\n')
spalv(fdssp,fdnot,atstout,0)
for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	spalv(f1,f2,outdssp,x)
	"""
	for y in shortdssp:
		y = y.rstrip('\n')
		read = fdnot.readline()
		if('>' in read):
			outdssp.write(bcolors.RESET+read)
		else:
			read = read.rstrip('\n')
			print 'yikas '+y+' length '+str(len(y))+'\nreads '+read+' length '+str(len(read))
			for i in range(0,len(y)):
				if( y[i] == '-'):
					outdssp.write(bcolors.RESET)
				elif( y[i]=='E'):
					outdssp.write(bcolors.YELLOW)
				else:
					outdssp.write(bcolors.GREEN)
				outdssp.write(read[i])
			outdssp.write('\n')
	for y in longdssp:
	        y = y.rstrip('\n')
		read = f2.readline()
	        if('>' in y):
			outdssp.write('\n'+ bcolors.RESET + read)
	        else:   
			read = read.rstrip('\n')
	                for i in range(0,len(y)):
	                        if( y[i] == '-'):
	                                outdssp.write(bcolors.RESET)
	                        elif( y[i]=='E'):
	                                outdssp.write(bcolors.YELLOW)
	                        else:
	                                outdssp.write(bcolors.GREEN)
				outdssp.write(read[i]) 
			outdssp.write('\n')
	outdssp.close()
	"""
