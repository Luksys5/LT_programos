import socket
def readpng(pth):
	f = open(pth,'r')
	duom = ''
	lines = f.readlines()
	for x in lines:
		duom+=x	
	return duom
def readdata(bound):
	Name = raw_input("Irasykite varda: ")
	Surname = raw_input("Irasykite pavarde: ")
	Year = raw_input("Irasykite amziu: ")
	path = raw_input("Failo path(kelias): ")
	myfile = readpng(path)
	data = bound+'\r\nContent-Disposition: form-data; name="vardas"\r\nContent-Type: text/plain\r\n\r\n'+Name+'\r\n'+bound+'\r\n'
	data += bound+'\r\nContent-Disposition: form-data; name="pavarde"\r\nContent-Type: text/plain\r\n\r\n'+Surname+'\r\n'+bound+'\r\n'
	data += bound+'\r\nContent-Disposition: form-data; name="amzius"\r\nContent-Type: text/plain\r\n\r\n'+Year+'\r\n'+bound+'\r\n'
	data += bound+'\r\nContent-Disposition: form-data; name="path"; filename="myphoto.png"\r\nContent-Type: image/png\r\n\r\n'+myfile+'\r\n'+bound+'--\r\n'
	return data
def send(data,bound):
	s = socket.socket()
	REQUEST = ('POST /post.php HTTP/1.1\r\nHost: posttestserver.com\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nContent-Length: '+str(len(data))+'\r\nKeep-Alive: 300\r\nConnection: keep-alive\r\nContent-Type: multipart/form-data; boundary=AaB03x\r\n\r\n'+data+'\r\n')
	ip = socket.gethostbyname('posttestserver.com')
	s.connect((ip,80))
	print ip, 'prisijunge'
	s.sendall(REQUEST)
	fw = open('response','w')
	while True:
	        msg =  s.recv(1000)
	        if not msg:
	                break
	        fw.write(msg)
	fw.close()
	s.close()
bound = "--AaB03x"
adata = readdata(bound)
send(adata,bound)
