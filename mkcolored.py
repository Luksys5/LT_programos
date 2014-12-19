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
        oneline =''
        nr = 0
        mt = 0
        for y in lines:
                y = y.rstrip('\n')
                read = notdssp.readline()
                nr = 0
                if('>' in read):
                        length = 0
                        mt = 0
                        output.write('\n')
                        output.write(bcolors.RESET+read)
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

                                elif( y[i]=='E'):
                                        output.write(bcolors.YELLOW)
                                else:
                                        output.write(bcolors.GREEN)
                                output.write(read[i]+" "*(len(str(i+len(y)*mt))+(len(str(i))-len(read[i]))))
                        mt +=1
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
atstout.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
spalv(fdssp,fdnot,atstout,0)
for x in range(1,16):
        f1 = open('../dssp/'+str(x),'r')
        f2 = open('../notdssp/'+str(x),'r')
        outdssp = open(str(x)+'.colored','w')
        outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
        spalv(f1,f2,outdssp,x)

