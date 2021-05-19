import sys
import socket
from domino import *

if "__main__" == __name__ and sys.argv[3:]:
  ### Client
  client_data = encode_data_850(sys.argv[2],sys.argv[3:])
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ### Create a TCP/IP socket
  sock.connect((sys.argv[1],9100,))                         ### Connnect socket to localhost port 9100
  data = sock.sendall(client_data)                          ### Send client data
  data = sock.recv(1024)                                    ### Receive server data
  sock.close()                                              ### Close connection and exit
