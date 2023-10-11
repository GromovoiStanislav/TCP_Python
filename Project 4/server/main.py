import socket

# Порт, на котором будет работать сервер TSP
SERVER_PORT = 12345

DOWNLOAD_FOLDER = 'download'  # Имя папки для сохранения файлов

# Создаем сокет и начинаем прослушивание на указанном порту
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', SERVER_PORT))
server.listen(1)  # Максимальное количество подключений

print(f'Сервер TSP запущен на порту {SERVER_PORT}')

while True:
    connection, address = server.accept()
    print(f'Клиент {address} подключился')

    # Получаем имя файла от клиента
    file_name = connection.recv(1024).decode()

    print(f'Принимаем файл: {file_name}')
    file_path = DOWNLOAD_FOLDER + '/' + file_name

    with open(file_path, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

    print(f'Файл "{file_name}" успешно принят')
    connection.close()