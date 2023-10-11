import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # localhost
port = 12345
client.connect((host, port))


print('[x] To exit type "exit" or press CTRL+C')
print('Type a message...')


done = False
while not done:
    msg = input('Message: ')
    if msg == 'quit':
        done = True
    else:
        client.send(msg.encode('utf-8'))


client.close()