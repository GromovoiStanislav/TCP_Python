import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Используем SOCK_DGRAM для UDP

host = '127.0.0.1'  # localhost
port = 54321  # Порт UDP сервера

print('[x] To exit type "exit" or press CTRL+C')
print('Type a message...')

done = False
while not done:
    msg = input('Message: ')
    if msg == 'exit':
        done = True
    else:
        # Отправляем сообщение на сервер по UDP
        client.sendto(msg.encode('utf-8'), (host, port))

client.close()  # Клиент не требует закрытия соединения, но мы закрываем сокет