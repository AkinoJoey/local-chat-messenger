import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

try:
   sock.connect(server_address)
except socket.error as err:
   print(err)
   sys.exit(1)

message = input(' -> ')

while message.lower().strip() != 'bye':
    sock.sendall(message.encode())

    try:
        data = sock.recv(4096).decode()
        print('Received from server: ' + data)
    except(TimeoutError):
      print('Socket timeout, ending listening for server messages')

    message = input(' -> ')

print('closing socket')
sock.close()