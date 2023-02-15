import socket
import os
from faker import Faker

# ソケットの作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

# ファイルが既に存在しないことを確認する
try:
   os.unlink(server_address)
except FileNotFoundError:
   pass

# ソケットをアドレスに紐付ける 
print('Starting up on {}'.format(server_address))
sock.bind(server_address)

sock.listen(1)
connection, client_address = sock.accept()

# fakerの作成
fake = Faker('ja-JP')
print('connection from', str(client_address))

# サーバが常に接続を待ち受けるためのループ
while True:    
    data = connection.recv(1024) 
    data_str =  data.decode('utf-8')
    print('from connected user: ' + data_str)

    if not data:
        print('no data from', str(client_address))
        break

    # fakerのテキストを作成
    response = fake.text()
    print(' -> ' + response)
    connection.sendall(response.encode())
    

print("Closing current connection")
connection.close()