import socket
s = socket.socket()
ip = socket.gethostbyname("www8.org")
request = "HEAD / HTTP/1.1\r\nConnection: close\r\n\r\n"
s.connect((ip, 80))
s.send(request)
result = s.recv(1000)
while (len(result) > 0):
    print(result)
    result = s.recv(0000) 
