import socket

client_socket = socket.socket()

port = 80
host = socket.gethostbyname('www.google.com')

client_socket.connect((host, port))

print ('socket secc conn to google on port=',port,' and ip=',host)
client_socket.close()

#Pitanje: što radi linija koda client_socket.connect((host,port))?
#Odgovor: spajanje na server



