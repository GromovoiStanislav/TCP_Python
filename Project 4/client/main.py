import socket

# Замените на IP-адрес и порт сервера TSP
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Путь к файлу, который вы хотите отправить
FILE_PATH = 'publicKey.pem'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_HOST, SERVER_PORT))
print(f'Соединение установлено с сервером TSP')

# Отправляем имя файла на сервер
client.send(FILE_PATH.encode())

# Отправляем содержимое файла на сервер
with open(FILE_PATH, 'rb') as file:
    data = file.read(1024)
    while data:
        client.send(data)
        data = file.read(1024)

print('Файл успешно отправлен')
client.close()