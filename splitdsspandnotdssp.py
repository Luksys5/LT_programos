def makenewfiles(f1):
	dssp = 0
	for x in range(1,16):
		f = open(f1+str(x)+'atstovas','r')
		fd = open('./dssp/'+str(x),'w')
		fn = open('./notdssp/'+str(x),'w')
		lines = f.readlines()	
		for line in lines:
			if '>' in line and 'dssp' not in line:
				dssp = 1
			elif '>' in line:
				dssp = 0
			if dssp == 1:
				fd.write(line)
			else:
				fn.write(line)
		f.close()
		fd.close()
		fn.close()
	f = open(f1+'allinone','r')
	fd = open('./atst/atst.dssp','w')
       	fn = open('./atst/atst.notdssp','w')
	lines = f.readlines()
	for line in lines:
         	if '>' in line and 'dssp' not in line:
                	dssp = 1
                elif '>' in line:
                	dssp = 0
                if dssp == 1:
                	fd.write(line)
            	else:
                	fn.write(line)
	f.close()
	fn.close()
	fd.close()
	return
		
filetocheck = raw_input('ivesti Fasta failu direktorijos kelia pvz: ./kelias/  : ')
makenewfiles(filetocheck)
