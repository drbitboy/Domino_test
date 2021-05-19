"""
Usage:

  python dominoclient.py server_hostname layout_number variable-data[ variable-data[ ...]]

"""
import sys
import socket
from domino import *

if "__main__" == __name__ and sys.argv[3:]:
  ### Client
  server,layout = sys.argv[1:3]                             ### Server hostname; layout number (1-999999)
  client_data = encode_data_850(layout,sys.argv[3:])        ### Encode command-line arguments to Codepage 850

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ### Create a TCP/IP socket
  sock.connect((server,9100,))                              ### Connect socket to port 9100 of server host
  sock.sendall(client_data)                                 ### Send client data
  data = sock.recv(1024)                                    ### Receive and ignore server data
  sock.close()                                              ### Close connection before exit
