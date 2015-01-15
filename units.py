# Suranda daugiausiai atitinkancias sekas
# Pabaigti sudaryti filogenetini medi is seku
# Didziausia reikisme tai arciausias maziausia toliausias
# sekai D: A = 300 B= 400 C =5000
# newick format (((D,C),B),A))
import re
import random 
def medynas(fastas,Pam,zeromatrix):## Pabaigt 
	fd = open('medynas','w')
	mymatrix=[[0 for x in xrange(len(fastas))] for x in xrange(len(fastas))]
	minnr = 0
	xnr = 0
	ynr = 0	
	a= 0
	for x in fastas:
		x = x.rstrip('\n')
		ynr = 0
		fd.write('\n')
		for y in fastas:
			y = y.rstrip('\n')
			if ynr > xnr:
				ats = matrix(Pam,matrica,x,y,zeromatrix,True)
				print xnr,ynr,ats
				fd.write(str(xnr)+' '+str(ynr)+' '+str(ats)+' ')
			#	ats = atsitiktine(Pam,matrica,x,y,zeromatrix,1)
				try:
					mymatrix[xnr][ynr]= ats
					mymatrix[ynr][xnr] = mymatrix[xnr][ynr]
				except IndexError:
					print 'xnr ynr: ',xnr, ynr ,'Fastas ', len(fastas)
			else:
				mymatrix[xnr][ynr] = 0
			ynr += 1
		xnr += 1
		#writein(fastas, mymatrix)
	return mymatrix
	writein(fastas, mymatrix)
def writein(fast, matr):
	fw = open("Matrica",'w')
	i = 0
	j = 0
	for x in fast:
		for y in fast:
			fw.write(str(matr[i][j])+" ")
			
		fw.write('\n')
		print 'klaida'
	return
def atsitiktine(Pam,matrica,myeil1, myeil2,zeromatrix): # Randomizina mutacijas
							# fastos 2 eilutej.
    n = 1000
    mutac = len(myeil2)*0.5
    suma = 0
    sumlist = []
    for i in range(0,n):
        l  = list(myeil2)
        for j in range(0,int(mutac)):
            r1 = random.randrange(0,len(myeil2))
            r2 = random.randrange(0,len(myeil2))
            temp = l[r2]
            l[r2] = l[r1]
            l[r1] = temp
        eil2m = "".join(l)
        maxas = matrix(Pam,matrica,myeil1, eil2m,zeromatrix, False)
	#print maxas
        suma += maxas
        sumlist.append(maxas)
    return sumlist # (1.0*suma/n), sumlist
def mymass(others,lists):    
    mass = {}
    for x in others:
        count=0
        mix = x.split()
        for y in mix:
            if re.match('[0-9]',y)  or re.match('-[0-9]',y):
                mass[(amino,lists[count])] = y
                mass[(lists[count],amino)] = y     
                count += 1
            else:
                amino = y
    return mass
def matrix(mass,Matrix,first,second,zero1,expr):#Generuoja kintamuosius ir didz						     #atitikima randa is Fasta eilutes
    	maxas = 0
	suma = 0
    	for i in range(0,int(len(first)-1)):
		for z in range(0,int(len(second)-1)):
			try:	
				score = max(0,int(int(mass.get((second[z],first[i])))+Matrix[i-1][z-1]),int(Matrix[i][z-1]-8),int(Matrix[i-1][z]-8))
			except TypeError:
				score = 0
			suma += score
			if score > maxas:
				maxas = score
			Matrix[i][z] = score 	
	if expr:
		return suma	
    	return maxas

def writing(mass,Matrix,first,second,zero1,listas): #Tiesiog suraso duomenys.
    fw = open('local','w') 
    #print (listas[1], listas[2])
    if listas[2] == len(first):
	print "yahoo~"

    for i in range(0,int(listas[1])+1):
	for z in range(0,int(listas[2])+1):
            if i > 0 or z > 0 :
                string = ''
                if int(int(mass.get((second[z],first[i])))+Matrix[i-1][z-1]) > int(Matrix[i][z-1]-8) and int(int(mass.get((second[z],first[i])))+Matrix[i-1][z-1]) > int(Matrix[i-1][z]-8):
                    string = ("\\")
                elif int(Matrix[i][z-1]-8)> int(Matrix[i-1][z]-8):
                    string = ("<")
                else:
                    string = ('^')
            else:
                string = ("\\")

            #if i == 1 and z == 2:'
            if re.match('[0-9]$',str(int(Matrix[i][z]))):
                fw.write('  '+string+str(int(Matrix[i][z])))               
            elif re.match('[0-9][0-9]',str(int(Matrix[i][z]))):
                fw.write(' '+string+str(int(Matrix[i][z])))
	fw.write('\n')
def diagram(maxdist):
	import matplotlib.pyplot as plt
	from numpy.random import normal
	plt.hist(sumlst, bins=40)
	plt.title("atsitiktiniu atstumu histograma")
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	plt.show()
 	return

print "prasideda kodas"
f = open("PAM10.txt","r")
first = f.readline()
listas = first.split()
Pam = {}
fr = open('fasta','r')
fastas = fr.readlines()
matrica = [[0 for x in xrange(len(first))] for x in xrange(len(first))] 
i = 1
zeromatrix = [[0 for x in xrange(len(first))] for x in xrange(len(first))] 
zothers = f.readlines()
distmatr = [[0 for x in xrange(len(fastas))] for x in xrange(len(fastas))] 
mylist = []
f.close()
Pam = mymass(zothers, listas)
#didz = matrix(Pam,matrica,fastas[0].rstrip('\n'),fastas[1].rstrip('\n'),zeromatrix)
distmatr = medynas(fastas,Pam,zeromatrix)
#ylist = matrix(Pam,matrica,fastas[0].rstrip('\n'),fastas[1].rstrip('\n'),zeromatrix)
sumlst = atsitiktine(Pam,matrica,fastas[0].rstrip('\n'),fastas[1].rstrip('\n'),zeromatrix)
#print sumlst
diagram(sumlst)

