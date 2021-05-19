import socket
from domino import *

### Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               ### Create a TCP/IP socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)             ### Keep TIME_WAIT socket from hanging
sock.bind(('',9100,))                                         ### Bind socket to port 9100
sock.listen(1)                                                         ### Listen on that port
connection,client_address = sock.accept()                              ### Accept client connection
data = connection.recv(1024)                                           ### Receive client data
print('Client data [{0}] received from {1}'.format(decode_data_850(data),client_address))
connection.sendall(b'This is the server')                              ### Send server data
connection.close()                                                     ### Close connection and exit
