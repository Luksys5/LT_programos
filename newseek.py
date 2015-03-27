def print_to_STDOUT(Names, gama, gempty, alfa, aempty, beta, bempty, word, count, atst):
	for x in range(0,len(Names)):
		nonemptyline = gempty[x]+aempty[x]+bempty[x]
		if nonemptyline > 0:
			if atst != "":
				print bcolors.FAIL, '----------- Atstovas + '+atst+' + nr'+str(count)+' --------------', bcolors.RESET
			print bcolors.FAIL+"---------------"+word+"seeks------------------"+bcolors.RESET
			print Names[x].rstrip('\n')
			if gempty[x] == 1:
				print bcolors.FAIL, "Kilpos"+bcolors.RESET, gama[x]
			if aempty[x] == 1:
				print bcolors.GREEN, "alfa", alfa[x], bcolors.RESET
			if bempty[x] == 1:
				print bcolors.YELLOW, "beta", beta[x], bcolors.RESET

	return
def check_values(tikr, ztikr, interval, zinterval):
	print "Checking", tikr
	print "Interval", interval
	print "next Check", ztikr
	print "next Interval", zinterval
	return

def minimum(one,two):
	if two > one:
		return str(one), str(two)
	return str(two), str(one)

def placing(one, two,s):
	diff = ''
	min1, min2 = minimum(one, two)
	if s == 1:
		diff += str(min1)+'-'+str(min2)+' '
	elif min1 != min2:
		diff += str(min1)+'-'+str(min2)+' '
	return diff

def lyginu(check, zcheck,interv,zinterv):
	chk = check.split('-')
	ints = interv.split('-')
	zchk = zcheck.split('-')
	zints = zinterv.split('-')
	diff = ''
	signal = 0

	if int(chk[1]) <  int(ints[0]):
		return check+' ', check+' ', 3, 1, 0
	elif int(ints[1]) < int(chk[0]):
		return interv+' ', interv+' ', 4, 0, 1
	else:
		diff += placing(int(ints[0]),int(chk[0]),0)
		diff += placing(int(ints[1]),int(chk[1]),0)
		if zinterv == ['']:
			return diff, '', 1, 1, 1
		elif zcheck == ['']:
			return diff, '', 2, 1, 1
		return diff, '', signal, 1, 1

def last(op1, op2, opc):
	differ = ''
	if op1 == [''] and opc != ['']:
		differ += op2[0]+'-'+op2[1]+' '+opc[0]+'-'+opc[1]+' '
	elif op1 == ['']:
		differ += op2[0]+'-'+op2[1]+' '
	elif op1 == op2 and opc != ['']: 
		differ += opc[0]+'-'+opc[1]+' '
		return diff
	elif op1 < op2 or op2 < op1:
		if op2[0] > op1[1]:
			differ += op1[0]+'-'+op1[1]+' '+op2[0]+'-'+op2[1]+' '
			return differ
		differ += op2[0]+'-'+op2[1]+' '+op1[0]+'-'+op1[1]+' '
	return differ
def cloop(cbind,binds, chval, name):
	a = b = 0    ## raides nurodancios pozicija intervalam paimti
        differs = '' ## Irasomi besiskiriantys intervalai, sekos
        notf = ''    ## Nerasti intervalai
	s = 0
        x = y = 0    ## tas ats kas a,b tik naudojama funkcijai "lyginu()".
        chint = cbind[a].split('-')       ## Tikrinimo intervalas.
        interval = binds[b].split('-')    ## Vienas is grupes atstovo intervalas.
	s = 0
	
	## Trimming seek start when there aren't any elements
	if int(interval[1]) > 200:
		b+=1
		while (int(chint[0]) <= int(interval[1])):
			a += 1
			chint = cbind[a].split('-')
			zchint = cbind[a+1].split('-')
			if zchint == ['']:
				return differs, notf
	
        while interval != [''] or chint != [''] :
		
                if interval == [''] or chint == ['']:
			if cbind[a] != binds[b]:
				if chint == ['']:
					differs += interval[0] +'-'+interval[1]
				if interval == ['']:
					differs += chint[0] + '-'+ chint[1]
			return differs, notf
		zinterval = binds[b+1].split('-')
		zchint = cbind[a+1].split('-')

		if b == len(binds)-2:
			mystr1, mystr2, s, x, y = lyginu(cbind[a],cbind[a+1], binds[b], binds[b+1])
			if (int(interval[1])-int(interval[0])) < 200:
				differs += mystr1
				notf += mystr2
				a += x
			tmp = cbind[len(cbind)-2].split('-')
			if (int(interval[1])-int(interval[0])) > 200:
				return differs, notf
			elif (int(tmp[1]) - int(interval[1])) > 200:
				return differs, notf
		#if (a == len(cbind)-2 ):
			#mystr1, mystr2, s, x, y = lyginu(cbind[a],cbind[a+1], binds[b], binds[b+1])
			#differs += mystr1
			
		
		#check_values(chint, zchint, interval, zinterval)
		
		if zinterval == [''] or zchint == ['']:
			'''	Tuo atveju jei intervalas tarp bruksnio yra tuscias ['']'''
			if binds[b] == cbind[a]:
				if zinterval == [''] and zchint != ['']:
					for x in range(a+1, len(cbind)):
						differs += cbind[x]+' '
						notf += cbind[x]+' '
				elif zchint == [''] and zinterval != ['']:
					for x in range(b+1, len(binds)):
						differs += binds[x]+' '
						notf += binds[x]+' '
			else:
				if zinterval == [''] and zchint == ['']:
					if int(chint[1]) < int(interval[0]):
						differs += cbind[a]+' '
						notf += cbind[a]+' '
						differs += last(zchint,interval,zinterval)
					elif int(interval[1]) < int(chint[0]):
						notf += binds[b]+' '
						differs += binds[b]+' '
						differs += last(zinterval, chint,zchint)
				
				else:
					if zinterval == [''] and zchint != ['']:
						if int(chint[1]) >= int(interval[0]) and int(interval[1]) >= int(zchint[0]):
							differs += placing(int(chint[0]),int(interval[0]),0)
							notf += cbind[a]+' '
							i = 0
							while int(interval[1]) >= int(zchint[0]):

								differs += chint[1]+'-'+zchint[0]+' '
								#notf += cbind[a]+' '
								a += 1
								chint = cbind[a].split('-')
								zchint = cbind[a+1].split('-')
								if zchint == ['']:
									differs += placing(int(chint[1]),int(interval[1]),0)
									notf += cbind[a]+' '
									return differs, notf

							if int(chint[1]) > int(interval[1]):
								notf += cbind[a]+' '
							differs += placing(int(chint[1]),int(interval[1]), 0) 
							for x in range(a+1, len(cbind)):
								differs += cbind[x]+' '
								notf += cbind[x]+' '

						else:
							mystr1, mystr2, s, x, y = lyginu(cbind[a],cbind[a+1], binds[b], binds[b+1])
							differs += mystr1
							notf += mystr2
							a += x
							b += y
							chint = cbind[a].split('-')
							interval = binds[b].split('-')
							morethandat = 1
							if s == 1:
								for x in range(b+1, len(binds)):
									differs += binds[x]+' ' 
									notf += binds[x]+' '
							elif s == 3:
								while( a+1 < len(cbind)):
									#check_values(chint, zchint, interval, zinterval)
									if int(interval[0]) <= int(chint[0]) and int(chint[0]) <= int(interval[1]):
										differs += placing(int(interval[1]), int(chint[1]),0)
										morethandat = 0
									elif int(interval[0]) <= int(chint[1]) and int(chint[1]) <= int(interval[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										morethandat = 0
									elif int(interval[0]) <= int(chint[0]) and int(chint[1]) <= int(interval[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0 
									elif int(chint[0]) <= int(interval[0]) and int(interval[1]) <= int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									else:
										differs += cbind[a]+' '
										notf += cbind[a]+' '
									a += 1
									chint = cbind[a].split('-')
								if morethandat: 
									differs += binds[b]+' '
									notf += binds[b]+' '
							elif s == 4:
								for x in range(a+1, len(cbind)):
									differs += cbind[x]+' '
									notf += cbind[x]+' '
							elif s == 0:
								differs += cbind[a]+' '	
								notf += cbind[a]+' '							
					
					elif zchint == [''] and zinterval != ['']:
						if int(interval[1]) >= int(chint[0]) and int(chint[1]) >= int(zinterval[0]):
							differs += placing(int(interval[0]),int(chint[0]),0)
							notf += binds[b]+' '
							i = 0
                					while int(chint[1]) >= int(zinterval[0]):

								differs += interval[1]+'-'+zinterval[0]+' '
								#notf += binds[b]+' '
								b += 1
								interval = binds[b].split('-')
								zinterval = binds[b+1].split('-')
								if zinterval == ['']:
									notf += binds[b]+' '
									differs += placing(int(chint[1]), int(interval[1]), 0)
									return differs, notf
							if int(interval[1]) > int(chint[1]):
								notf += binds[b]+' '
							differs += placing(int(chint[1]), int(interval[1]), 0)
							for x in range(b+1, len(binds)):
								differs += binds[x]+' '
								notf += binds[x]+' '

						else:
							mystr1, mystr2, s, x, y = lyginu(cbind[a],cbind[a+1], binds[b], binds[b+1])
							differs += mystr1
							notf += mystr2
							a += x
							b += y
							chint = cbind[a].split('-')
							interval = binds[b].split('-')
							morethandat = 1
							if s == 2:
								for x in range(a+1, len(cbind)):
									differs += cbind[x]+' '
									notf += cbind[x]+' '
							elif s == 4:
								while( b+1< len(binds)):
									if int(chint[0]) < int(interval[0]) and int(interval[0]) < int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									elif int(chint[0]) < int(interval[1]) and int(interval[1]) < int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									elif int(chint[0]) <= int(interval[0]) and int(interval[1]) <= int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									elif int(interval[0]) <= int(chint[0]) and int(chint[1]) <= int(interval[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									else:
										differs += binds[b]+' '
										notf += binds[b]+' '
									b += 1
									interval = binds[b].split('-')
								if morethandat: 
									differs += cbind[a]+' '
									notf += cbind[a]+' '
							elif s == 3:
								for x in range(b, len(binds)):
									differs += binds[x]+' '
									notf += binds[x]+' '
							elif s == 0:
								differs += binds[b]+' '
								notf += binds[b]+' '
					
			return differs, notf
		
		if int(interval[0]) > int(zchint[1]):
			# Intervalas didesnis uz tikrinama intervala. INT > CHECK
			while int(interval[0]) > int(zchint[1]):  
				differs += cbind[a]+' '
				notf += cbind[a]+' '
				if zchint == ['']:
					for x in range(b,len(binds)):
						differs += binds[x]+' '
						notf += binds[x]+' '
					return differs, notf
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')
		
		# Tikrinimo intervalas didesni uz intervala. CHECK > INT
		elif int(chint[0]) > int(zinterval[1]):		
			while int(chint[0]) > int(interval[1]):
				differs += binds[b]+' '
				notf += binds[b]+' '
				if zinterval == ['']:
					for x in range(a,len(cbind)):
						differs +=  cbind[x]+' '
						notf += cbind[x]+' '
					return differs, notf
				b+=1
				interval = binds[b].split('-')
				zinterval = binds[b+1].split('-')

		elif (int(chint[1]) >= int(interval[0])) and (int(interval[1]) >= int(zchint[0])):
			differs += placing(int(chint[0]),int(interval[0]),0)
			i = 0
			while int(interval[1]) >= int(zchint[0]):
				i += 1
				differs += chint[1]+'-'+zchint[0]+' '
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')
				##Jei paskutinis tikrinimo intervalas mazesnis uz lyginama
				if zchint == ['']:		
					differs += placing(int(chint[1]),int(interval[1]),0)
					for x in range(b+1,len(binds)):
						differs += binds[x]+' '
						notf += binds[x]+' '
					return differs, notf

			differs += placing(int(chint[1]),int(interval[1]),0)
			if int(chint[1]) > int(interval[1]):
				notf += cbind[a]+' '
			a += 1
			b += 1

		elif (int(interval[1]) >= int(chint[0])) and (int(chint[1]) >= int(zinterval[0])):
			differs += placing(int(interval[0]),int(chint[0]),0)
			i = 0
			while int(chint[1]) >= int(zinterval[0]):
				differs += interval[1]+'-'+zinterval[0]+' '
				b += 1
				interval = binds[b].split('-')
				zinterval = binds[b+1].split('-')
				## Jei paskutinis intervalas uzejo uz ribu.
				if zinterval == ['']:			
					differs += placing(int(chint[1]),int(interval[1]),0)
					for x in range(a+1,len(cbind)):
						differs += cbind[x]+' '
						notf += cbind[x]+' '
					return differs, notf
			differs += placing(int(chint[1]),int(interval[1]),0)
			if int(interval[1]) > int(chint[1]):
				notf += binds[b]+' '
			a += 1
			b += 1

		elif cbind[a] != binds[b]:
			mystr1, mystr2, s, x, y = lyginu(cbind[a],cbind[a+1],binds[b],binds[b+1])
			differs += mystr1
			notf += mystr2
			a += x
			b += y
		else:
			a += 1
			b += 1
                chint = cbind[a].split('-')
                interval = binds[b].split('-')

def Changes(bindl,dval,check, protas):
	import re
	#print '---------------check:'+str(check)+'-------------------'
	Diflist = []
	checkseek = bindl[0].split(' ')
	groupseek = bindl[1:]
	## Diferences and not found seeks lists 
	nfoundlenghts = []
	diffempty = []
	nfoundval = []
	DiffmsList = []   ## List that contains Difference by measure
	count = 0
        for x in groupseek:
		count += 1
		diffms = ''
		mylist = x.split(' ')
		diff = ''
		nfound = ''
		if count == 1:
			'''
			# 			For Testing
			tstchk = ['1-6', '9-12', '20-28', '35-37', '69-96', '113-114', '195-205', '208-214', '222-223']
			tstlst = ['1-5', '18-100', '129-136', '150-167', '200-212', '']
			print tstchk,'\n', tstlst 
			diff, nfound = cloop(tstchk, tstlst, dval,'Test') 
			'''
		#print checkseek
		#print "-------"+str(count)+'-a seka--------------------'
			print protas[count]
			diff, nfound = cloop(checkseek, mylist,dval,protas[count-1])
			print diff
			print nfound
			return nfoundlenghts, nfoundval, DiffmsList, diffempty
		
		### checking if in diff seek difference between each seek element is major than measurement value
		lengths = diff.split(' ')
		z = 0
		for y in lengths:
			nr = y.split('-')
			try:
				if abs(int(nr[1])-int(nr[0])) >= dval:
					diffms += nr[0] + '-' + nr[1]+' '
					z += 1
			except IndexError:
				z += 0
		if z == 0:
			diffempty.append(0)
		else:
			diffempty.append(1)
		DiffmsList.append(diffms)

		### checking if not found elements difference is major than measurement value
		nfoundlen = ''
                lengths = nfound.split(' ')
		z = 0
                for y in lengths:
                        nr = y.split('-')
                        try:
                                if abs(int(nr[1])- int(nr[0]) ) >= dval:
                                        nfoundlen += nr[0] + '-' + nr[1]+' '
                			z += 1
		        except IndexError:
                                z += 0
		if z == 0:
			nfoundval.append(0)
		else:
			nfoundval.append(1)
                nfoundlenghts.append(nfoundlen)
        return nfoundlenghts, nfoundval, DiffmsList, diffempty

def finddiff(Nameslst, alfalst, betalst, gamalst, m, count):
	nfgama, nfgempty, DiffgamaLen, diffgempty = Changes(gamalst, m, count,Nameslst)
	#nfalfa, nfaempty, DiffalfaLen, diffaempty = Changes(alfalst, m, count, Nameslst)
	#nfbeta, nfbempty, DiffbetaLen, diffbempty = Changes(betalst, m, count, Nameslst)
	#print_to_STDOUT(Nameslst[1:], DiffgamaLen, diffgempty, DiffalfaLen, diffaempty, DiffbetaLen, diffbempty, "Diference in ", count, Nameslst[0].rstrip('\n'))
	#print_to_STDOUT(Nameslst[1:], nfgama, nfgempty, nfalfa, nfaempty, nfbeta, nfbempty, "Not found ", count, "")
	
	return	

def spalv(dssp,notdssp,output,count,outdiff,outch,flag,measure):
        import os, subprocess
        lines = dssp.readlines()
        betal = [] # Antrines beta str
        alfal = [] # Antrines alfa str
        gamal = [] # kilpos
        length = 0
        baltlist = []
        glen = 0
        blen = 0
        alen = 0
        for y in lines:
                y = y.rstrip('\n')
                read = notdssp.readline()
                if('>' in read):
                        baltlist.append(read[1:])
			if length != 0:
				if glen > 0:
					gamastr += str(length-glen)+'-'+str(length-1)+' '
					glen = 0
                                if blen > 0:
                                        betastr += str(length-blen)+'-'+str(length-1)+' '
                                        blen = 0
                                if alen > 0:
                                        alfastr += str(length-alen)+'-'+str(length-1)+' '
                                        alen = 0
                                alfal.append(alfastr)
                                betal.append(betastr)
                                gamal.append(gamastr)
                        glen = 0
                        blen = 0
                        alen = 0
                        alfastr = ''
                        betastr = ''
                        gamastr = ''
                        length = 0
                else:
                        for i in range(0,len(y)):
                                length += 1
                                if( y[i] == '-'):
                                        if alen > 0:
                                                alfastr += str(length-alen)+'-'+str(length-1)+' '
                                                alen = 0
                                        if blen > 0:
                                                betastr += str(length-blen)+'-'+str(length-1)+' '
                                                blen = 0
                                        glen += 1
                                        output.write(bcolors.RESET)
                                elif( y[i]=='E'):
                                        blen += 1
                                        if alen > 0:
                                                alfastr += str(length-alen)+'-'+str(length-1)+' '
                                                alen = 0
                                        if glen > 0:
                                                gamastr += str(length-glen)+'-'+str(length-1)+' '
                                                glen = 0
                                        output.write(bcolors.YELLOW)
                                else:
                                        alen += 1
                                        if blen > 0:
                                                betastr += str(length-blen)+'-'+str(length-1)+' '
                                                blen = 0
                                        if glen > 0:
                                                gamastr += str(length-glen)+'-'+str(length-1)+' '
                                                glen = 0
                                        output.write(bcolors.GREEN)
	alfal.append(alfastr)
	betal.append(betastr)
	gamal.append(gamastr)
	if count == 12:
		finddiff(baltlist, alfal, betal, gamal, measure, count)
        
	'''#Check 
        for x in range(0,len(alfal)):
                print 'printing', count
                print baltlist[x].rstrip('\n')
		print gamal[x]
                print betal[x]
                print alfal[x],'\n'
        '''
	# Write io output file *.colored
        for x in range(0,len(gamal)):
                output.write(baltlist[x])
                output.write(bcolors.FAIL+'kilpos '+bcolors.RESET+gamal[x])
                if gamal[x] != gamal[0]:
                        output.write(bcolors.FAIL+' <---'+bcolors.RESET)
                output.write('\n')

                output.write(bcolors.YELLOW+'beta '+betal[x]+bcolors.RESET)
                if betal[x] != betal[0]:
                        output.write(bcolors.FAIL+' <---'+bcolors.RESET)
                output.write('\n')

                output.write(bcolors.GREEN+'alfa '+alfal[x]+bcolors.RESET)
                if alfal[x] != alfal[0]:
                        output.write(bcolors.FAIL+' <---'+bcolors.RESET)
                output.write('\n\n')
	return

import re
class bcolors:
        FAIL = '\033[91m'
        BOLD = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RESET = '\033[0m'
fdssp = open('../atst/atst.dssp','r')
fdnot = open('../atst/atst.notdssp','r')
m = 0
# int(raw_input('Panasumo ivertis: '))

#   Atstovu atstovai
atstout = open('atst.colored','w')
atstdiff = open('atst.diff','w')
atstch = open('atst.ch','w')
atstout.write(bcolors.GREEN + '                Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+' Bend -'+'\n')
spalv(fdssp,fdnot,atstout,0,atstdiff,atstch,1,m)
print bcolors.YELLOW+'\n\t\tNe-atstovu sekos\n'+bcolors.RESET

##   Grupes su atstovais
for x in range(1,16):
        f1 = open('../dssp/'+str(x),'r')
        f2 = open('../notdssp/'+str(x),'r')
        outdssp = open(str(x)+'.colored','w')
        outdiff = open(str(x)+'.diff','w')
        outch = open(str(x)+'.ch','w')
        outdssp.write(bcolors.GREEN + '                 Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
        spalv(f1,f2,outdssp,x,outdiff,outch,0,m)

