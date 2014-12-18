import socket
def splitdata(data):
	lines = data.split('\n')
	mystring = ''
	for x in lines:
		if 'key:' in x:
			mylist = x.split("'")
			mystring += mylist[1]+" "+mylist[3]+'\n'
		if 'name:' in x:
			x = x.split(': ')
			mystring += x[1].rstrip('\n')
		if 'Uploaded File:' in x:
			mystring += ' ' + x[13:] + '\n'
			buff = 0
	return mystring
def getreq(REQUEST,server):
	s=socket.socket()
	ip = socket.gethostbyname(server)
	s.connect((ip,80))
	print ip, 'prisijunge'
	s.sendall(REQUEST)
	fw = open('getresponse','w')
	while True:
		msg =  s.recv(1000)
		alldata = splitdata(msg)
	        if not msg:
			break
		fw.write(alldata)
	fw.close()
	s.close()
	return
Req1 = ("GET /data/2014/12/17/04.30.53533087991 HTTP/1.1\r\nHost: www.posttestserver.com\r\nConnection: close\r\n\r\n")
servak1='www.posttestserver.com'
Req = ("GET /files/2014/12/17/f_04.30.53483051638 HTTP:1.1\r\nHost: www.posttestserver.com\r\nConnection: close\r\n\r\n")
getreq(Req1,servak1)
