import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # localhost
port = 9999
server.bind((host, port))

server.listen()

print(f"Сервер слушает на {host}:{port}")

client, addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print(msg)
        client.send(input('Message: ').encode('utf-8'))

client.close()
server.close()