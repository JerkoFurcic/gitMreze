import sys
sys.path.append('C:/Users/Jerko Furcic/Desktop/Mrežno Programiranje/gitMreze/lab1')

import socket
import datetime

from local_machine_info import print_machine_info

print (datetime.datetime.now())
print_machine_info()

host= socket.gethostname()
port = 9999

client_socket = socket.socket()

client_socket.connect((host,port))
client_socket.sendall('Tekst za srever'.encode)
data = client_socket.recv(1024)

print(data.encode)
client_socket.close()
