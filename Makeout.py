import os, subprocess
def grupiulyg(target, listas):
        print target+' ir listas:'+listas
        os.system('perl dali_sp.pl -i '+target+" -l "+listas+" -o pdbs -m "+target+'.out')
def atstovulyg(target, listas):
        os.system('mkdir pdbsatstovai')
        os.system('perl dali_sp.pl -i '+target+" -l "+listas+" -o pdbsatstovai -m "+target+'1.out')
fz = open('atstovai', 'w')
for x in xrange(1,15):
	fh=open(str(x)+'.txt','r')
	document = fh.readline()
	atstovas = document.split()
	if x > 1:
                fz.write(str(atstovas[0])+'\n')
        else:
                atstovingiausias = atstovas[0]
	atstovas = str(atstovas[0])+".pdb"
	target = str(x)+'atstovas'
	fh = open(target,  'w')
	fh.write(atstovas)
	others = str(x)+"alt"
	grupiulyg(target, others)
