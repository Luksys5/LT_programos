import socket
s = socket.socket()
ip = socket.gethostbyname("httpbin.org")
request = "GET /status/418 HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"
s.connect((ip, 80))
s.send(request)
result = s.recv(1000)
while (len(result) > 0):
    print(result)
    result = s.recv(0000) 
