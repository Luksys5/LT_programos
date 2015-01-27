def simplediff(pavlst,alfal,betal,firsta,firstb,out):
	atst = pavlst[0]
        out.write(atst+'\n'+bcolors.FAIL+'--------atstovo seka-------------\n'+bcolors.RESET)
        pavlist = pavlst[1:(len(pavlst)-1)]
        out.write(firsta+'\n')
        out.write(firstb+'\n')
        out.write(bcolors.FAIL+'---------------------------------\n'+bcolors.RESET)
        for i in range(0,len(pavlist)):
                out.write(pavlist[i]+'\n')
                out.write(alfal[i])
                if firsta.rstrip('\n') != alfal[i].rstrip('\n'):
                        out.write(bcolors.FAIL+' <---\n'+bcolors.RESET)
                else:
                        out.write('\n')
                out.write(betal[i])
                if firstb.rstrip('\n') != betal[i].rstrip('\n'):
                        out.write(bcolors.FAIL+' <---\n'+bcolors.RESET)
                else:
                        out.write('\n')

        return
def wherediff(pavlst,alfalst,betalst,falfa,fbeta,out):
	import re
	mystr = ''
	write = 0
	atst = pavlst[0]
        out.write(atst+'\n'+bcolors.FAIL+'--------atstovo seka-------------\n'+bcolors.RESET)
        pavlist = pavlst[1:(len(pavlst)-1)]
        out.write(falfa+'\n')
        out.write(fbeta+'\n')
        out.write(bcolors.FAIL+'---------------------------------\n'+bcolors.RESET)
	for i in range(0,len(pavlist)):
		if betalst[i] != fbeta:
                        #mystr = ''
                        out.write(pavlist[i]+'\n')
                        if len(betalst[i]) == len(fbeta):
                                #out.write(alfalst[i]+'\n')
                                out.write(bcolors.YELLOW+'beta'+bcolors.RESET)
                                for x in range(0,len(betalst[i])):
                                        if betalst[i][x] == ' ':
                                                if 'beta' in mystr:
                                                        mystr = ''
                                                if write == 1:
                                                        out.write(' '+mystr)
                                                write = 0
                                                mystr = ''
                                        else:
                                                mystr += betalst[i][x]
                                        if fbeta[x] != betalst[i][x]:
                                                write = 1
                                        if x == (len(betalst[i])-1):
                                                out.write(bcolors.RESET+'\n')
                                mystr = ''
                        else:
                                out.write(betalst[i]+'\n')
		if alfalst[i] != fbeta:
			#mystr = ''
			out.write(pavlist[i]+'\n')
			if len(alfalst[i]) == len(falfa):
				#out.write(alfalst[i]+'\n')
				out.write(bcolors.GREEN+'alfa '+bcolors.RESET)
				for x in range(0,len(alfalst[i])):
					if alfalst[i][x] == ' ':
						if 'alfa' in mystr:
							mystr = ''
						if write == 1:
							out.write(mystr+' ')
						write = 0
						mystr = ''
					else:
						mystr += alfalst[i][x]
					if falfa[x] != alfalst[i][x]:
						write = 1
					if x == (len(alfalst[i])-1):
						out.write(bcolors.RESET+'\n')
				mystr = ''
			else:
				out.write(alfalst[i]+'\n')
	return
#Nurodo pdb strukturos alfa beta strukturas pakeiciant spalva 

#Skirtingi failai perduodami ciklui

#vieni trumpi tik vieno baltymo, kiti keliu baltymu
def spalv(dssp,notdssp,output,count,outkons,outch):
	import os, subprocess
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
					if( y[i-1] == 'E' and i > 0):
						betastr += ('-'+str(length+i))
					if( y[i-1] == 'H' and i >0):
						alfastr += ('-'+str(int(length+i))) 
					beta = 0
					alfa = 0
                		elif( y[i]=='E'):
					if(alfa==1):
                                        	alfastr += ('-'+str(int(length+i)))
					if beta == 0:
						blen += 1
						beta = 1
						betastr += ' ' + str(length+i+1)
                	        	output.write(bcolors.YELLOW)
					alfa = 0
                	       	else:
					if(beta==1):
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
	alfastr += bcolors.RESET
	betastr += bcolors.RESET
	pavlist = pavadinimas.split('\n')
	alfal = alfastr.split('\n')
	betal = betastr.split('\n')
	alfal = alfal[1:]
	betal = betal[1:]
	firstb = betal[0]
	firsta = alfal[0]
	simplediff(pavlist,alfal[1:],betal[1:],firsta,firstb,outkons)
	wherediff(pavlist,alfal[1:],betal[1:],firsta,firstb,outch)
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
atstch = open('atst.ch','w')
atstout.write(bcolors.GREEN + ' Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+'\n')
spalv(fdssp,fdnot,atstout,0,atstkons,atstch)
for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outkons = open(str(x)+'.kons','w')
	outch = open(str(x)+'.ch','w')
	outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	spalv(f1,f2,outdssp,x,outkons,outch)
