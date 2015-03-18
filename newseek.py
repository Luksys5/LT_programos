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
		diff += placing(int(chk[0]),int(chk[1]),1)
		return diff, 3 , 1, 0
	elif int(ints[1]) < int(chk[0]):
		diff += placing(int(ints[0]),int(ints[1]),1)
		return diff, 4,0 ,1
	else:
		diff += placing(int(ints[0]),int(chk[0]),0)
		diff += placing(int(ints[1]),int(chk[1]),0)
		if zinterv == ['']:
			return diff, 1, 1, 1
		elif zcheck == ['']:
			return diff, 2, 1, 1
		return diff, signal, 1, 1

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
def cloop(cbind,binds, chval,name):
	a = b = 0  ## raides nurodancios pozicija intervalam paimti
        differs = '' ## Irasomi besiskiriantys intervalai, sekos
        notf = ''    ## Nerasti intervalai
	s = 0
	print ' ------------------+Lyginama+'+name.rstrip('\n')+'+---------------------'
        x = y = 0       ## tas ats kas a,b tik naudojama funkcijai "lyginu".
        chint = cbind[a].split('-')       ## Tikrinimo intervalas.
        interval = binds[b].split('-')    ## Vienas is grupes atstovo intervalas.
        
	#return differs ,[]
	s = 0
        while interval != [''] or chint != [''] :
		dvalue = 0
                if interval == [''] or chint == ['']:
			if cbind[a] != binds[b]:
				if chint == ['']:
					differs += interval[0] +'-'+interval[1]
				if interval == ['']:
					differs += chint[0] + '-'+ chint[1]
			return differs, notf
		zinterval = binds[b+1].split('-')
		zchint = cbind[a+1].split('-')
		if zinterval == [''] or zchint == ['']:
			print "Tikrinama", chint
			print "Intervalas", interval
			'''	Tuo atveju jei intervalas tarp bruksnio yra tuscias ['']'''
			if binds[b] == cbind[a]:
				if zinterval == [''] and zchint != ['']:
					differs += cbind[a+1]+' '
				if zchint == [''] and zinterval != ['']:
					differs += binds[b+1]+' '
			else:
				if zinterval == [''] and zchint == ['']:
					if int(chint[1]) < int(interval[0]):
						differs += cbind[a]+' '
						differs += last(zchint,interval,zinterval)
					elif int(interval[1]) < int(chint[0]):
						differs += binds[b]+' '
						differs += last(zinterval, chint,zchint)

				else:
					if zinterval == [''] and zchint != ['']:
						print "Tikrinama", chint
                        			print "Intervalas", interval
						if int(chint[1]) >= int(interval[0]) and int(interval[1]) >= int(zchint[0]):
							differs += placing(int(chint[0]),int(interval[0]),0)
							differs += placing(int(chint[1]),int(zchint[0]),0)
							differs += placing(int(interval[1]), int(zchint[1]),0)
						
						else:
							mystr1, s, x, y = lyginu(cbind[a],cbind[a+1], binds[b], binds[b+1])
							differs += mystr1
							a += x
							b += y
							morethandat = 1
							if s == 1:
								for x in range(b+1, len(binds)):
									differs += binds[x]+' ' 
							elif s == 3:
								while( a+1 < len(cbind)):
									print 'check interval', cbind[a], binds[b]
									
									if int(interval[0]) < int(chint[0]) and int(chint[0]) < int(interval[1]):
										differs += placing(int(chint[0]), int(interval[0]))
										differs += placing(int(chint[1]), int(interval[1]))
										morethandat = 0
									elif int(interval[0]) < int(chint[1]) and int(chint[1]) < int(interval[1]):
										differs += placing(int(chint[0]), int(interval[0]))
										differs += placing(int(chint[1]), int(interval[1]))
										morethandat = 0
									elif int(interval[0]) <= int(chint[0]) and int(chint[1]) <= int(interval[1]):
										differs += placing(int(chint[0]), int(interval[0]))
										differs += placing(int(chint[1]), int(interval[1]))
										morethandat = 0 
									elif int(chint[0]) <= int(interval[0]) and int(interval[1]) <= int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									else:
										differs += cbind[a]+' '
									a += 1
									chint = cbind[a].split('-')
								if morethandat: differs += binds[b]+' '
							elif s == 4:
								for x in range(a+1, len(cbind)):
									differs += cbind[x]+' '
					
					elif zchint == [''] and zinterval != ['']:
						if int(interval[1]) >= int(chint[0]) and int(chint[1]) >= int(zinterval[0]):
							differs += placing(int(interval[0]),int(chint[0]),0)
							differs += placing(int(interval[1]),int(zinterval[0]),0)
							differs += placing(int(chint[1]), int(zinterval[1]),0)
						else:
							mystr1, s, x, y = lyginu(cbind[a],cbind[a+1], binds[b], binds[b+1])
							differs += mystr1
							a += x
							b += y
							morethandat = 1
							if s == 2:
								for x in range(a+1, len(cbind)):
									differs += cbind[x]+' '
							elif s == 3:
								while( b < len(binds)):
									if int(chint[0]) < int(interval[0]) and int(interval[0]) < int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
									elif int(chint[0]) < int(interval[1]) and int(interval[1]) < int(chint[1]):
										differs += placing(int(chint[0]), int(interval[0]),0)
										differs += placing(int(chint[1]), int(interval[1]),0)
										morethandat = 0
								if morethandat: differs += cbind[a]+' '
							elif s == 4:
								for x in range(b+1, len(binds)):
									differs += binds[x]+' '
					
			return differs, notf 
		if int(interval[0]) > int(zchint[1]):
			while int(interval[0]) > int(zchint[1]):    # Intervalas didesnis uz tikrinama intervala. INT > CHECK
				differs += cbind[a]+' '
				notf += chint[0]+'-'+chint[1]+' '
				if zchint == ['']:
					for x in range(b,len(binds)):
						differs += binds[x]+' '
					return differs, notf
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')	

		elif int(chint[0]) > int(zinterval[1]):		# Tikrinimo intervalas didesni uz intervala. CHECK > INT
			while int(chint[0]) > int(interval[1]):
				differs += binds[b]+' '
				if zinterval == ['']:
					for x in range(a,len(cbind)):
						differs +=  cbind[x]+' '
					return differs, notf
				b+=1
				interval = binds[b].split('-')
                                zinterval = binds[b+1].split('-')

		elif (int(chint[1]) >= int(interval[0])) and (int(interval[1]) >= int(zchint[0])):
			differs += placing(int(chint[0]),int(interval[0]),0)
			while int(interval[1]) >= int(zchint[0]):
				differs += chint[1]+'-'+zchint[0]+' '
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')
				if zchint == ['']:			##Jei paskutinis tikrinimo intervalas mazesnis uz lyginama
					differs += placing(int(chint[1]),int(interval[1]),0)
					for x in range(b+1,len(binds)):
						differs += binds[x]+' '
					return differs, notf
			differs += placing(int(chint[1]),int(interval[1]),0)
			a += 1
			b += 1

		elif (int(interval[1]) >= int(chint[0])) and (int(chint[1]) >= int(zinterval[0])):
			differs += placing(int(interval[0]),int(chint[0]),0)
			while int(chint[1]) >= int(zinterval[0]):
				differs += interval[1]+'-'+zinterval[0]+' '
				b += 1
				interval = binds[b].split('-')
				zinterval = binds[b+1].split('-')
				if zinterval == ['']:				## Jei paskutinis intervalas uzejo uz ribu.
					differs += placing(int(chint[1]),int(interval[1]),0)
					for x in range(a+1,len(cbind)):
						differs += cbind[x]+' '
					return differs, notf
			differs += placing(int(chint[1]),int(interval[1]),0)
			a += 1
			b += 1

		elif cbind[a] != binds[b]:
			mystr1, s, x, y = lyginu(cbind[a],cbind[a+1],binds[b],binds[b+1])
			differs += mystr1
			a += x
			b += y
		else:
			a += 1
			b += 1
                chint = cbind[a].split('-')
                interval = binds[b].split('-')

def Changes(bindl,dval,check, protas):
        import re
        print '---------------check:'+str(check)+'-------------------'
        Diflist = []
        checkseek = bindl[0].split(' ')
        groupseek = bindl[1:]
        NotfLenList = []
        diffempty = []
        notfempty = []
        DiffLenList = []
        count = 0
        for x in groupseek:
                count += 1
                difflen = ''
                notflen = ''
                x = x.split(' ')
		diff, empty= cloop(x,checkseek,dval,protas[count-1])
		print diff
		diff = empty = ''
                lengths = diff.split(' ')
                for x in lengths:
                        mystr = x.split('-')
                        try:
                                if (int(mystr[1])- int(mystr[0]) ) >= dval:
                                        difflen += mystr[0] + '-' + mystr[1]+' '
                        except IndexError:
                                difflen += ''
                DiffLenList.append(difflen)

                lengths = empty.split(' ')
                for x in lengths:
                        mystr = x.split('-')
                        try:
                                if (int(mystr[1])- int(mystr[0]) ) > dval:
                                        notflen += mystr[0] + '-' + mystr[1]+' '
                        except IndexError:
                                notflen += ''
                NotfLenList.append(notflen)

                if re.match('\s',difflen):
                        diffempty.append(0)
                else:
                        diffempty.append(1)
                if re.match('\s',empty):
                        notfempty.append(0)
                else:
                        notfempty.append(1)
        return NotfLenList, notfempty, DiffLenList, diffempty

def spalv(dssp,notdssp,output,count,outdiff,outch,flag,measure):
        print bcolors.FAIL+'-----------limitless--------------'+bcolors.RESET
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
        pavadinimas = ''
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
        '''#Check 
        for x in range(0,len(gamal)):
                print 'printing', count
                print baltlist[x].rstrip('\n')
                print gamal[x]
                print betal[x]
                print alfal[x],'\n'
        '''

        # Write to output file *.colored
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

        
	Names = baltlist[1:]
#       print bcolors.FAIL+'kilpos '+bcolors.RESET
        #NotfgamaLen, notfgempty ,DiffgamaLen,diffgempty = Changes(gamal,measure,count,Names)

        print bcolors.GREEN+'alfa '+bcolors.RESET
        NotfalfaLen, notfaempty, DiffalfaLen, diffaempty = Changes(alfal,measure,count,Names)
        #print DiffalfaLen
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
atstout.write(bcolors.GREEN + '                 Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+' Bend -'+'\n')
spalv(fdssp,fdnot,atstout,0,atstdiff,atstch,1,m)
print bcolors.FAIL+'skirtinga seka'+bcolors.RESET
'''
#   Grupes 
for x in range(1,16):
        f1 = open('../dssp/'+str(x),'r')
        f2 = open('../notdssp/'+str(x),'r')
        outdssp = open(str(x)+'.colored','w')
        outdiff = open(str(x)+'.diff','w')
        outch = open(str(x)+'.ch','w')
        outdssp.write(bcolors.GREEN + '                 Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
        spalv(f1,f2,outdssp,x,outdiff,outch,0,m)
'''
