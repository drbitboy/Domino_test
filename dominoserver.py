import socket
from domino import *

### Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               ### Create a TCP/IP socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)             ### Keep TIME_WAIT socket from hanging
sock.bind(('',9100,))                                                  ### Bind socket to port 9100
sock.listen(1)                                                         ### Listen on that port
connection,client_address = sock.accept()                              ### Accept client connection
encoded_data = connection.recv(1024)                                   ### Receive client data
civ,src,calc = checksum_is_valid(encoded_data)
print('Client data [{0}] received from {1}; checksum {2} valid {3}/{4}'.format(
       decode_data_850(encoded_data)
      ,client_address
      ,civ and 'is' or 'is not'
      ,src
      ,calc
      ,))
connection.sendall(b'This is the server')                              ### Send server data
connection.close()                                                     ### Close connection and exit
