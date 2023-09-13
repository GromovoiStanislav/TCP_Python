import socket

# Создаем сокет клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем хост и порт сервера, к которому клиент будет подключаться
host = '127.0.0.1'  # localhost
port = 12345

# Подключаемся к серверу
client_socket.connect((host, port))

# Отправляем сообщение серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Принимаем ответ от сервера
response = client_socket.recv(1024)
print(f"Получен ответ от сервера: {response.decode()}")

# Закрываем соединение
client_socket.close()