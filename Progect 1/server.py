import socket

# Создаем сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем хост и порт, на котором сервер будет слушать
host = '127.0.0.1'  # localhost
port = 12345

# Привязываем сокет к хосту и порту
server_socket.bind((host, port))

# Начинаем слушать входящие соединения (максимальное количество клиентов: 5)
server_socket.listen(5)

print(f"Сервер слушает на {host}:{port}")

while True:
    # Принимаем входящее соединение
    client_socket, client_address = server_socket.accept()
    print(f"Получено соединение от {client_address}")

    # Принимаем данные от клиента
    data = client_socket.recv(1024)
    print(f"Получено сообщение от клиента: {data.decode()}")

    # Отправляем ответ клиенту
    response = "Привет, клиент!"
    client_socket.send(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()
