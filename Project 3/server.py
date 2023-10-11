import socket
import threading

# Порт для сервера TCP
TCP_PORT = 12345

def handle_client(client_socket, addr):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f'Получено сообщение от {addr}: {message}')
        
        # Ваш код для обработки сообщения, например, отправить ответ
        response = f'Принято сообщение: {message}'.encode()
        client_socket.send(response)
    
    client_socket.close()

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', TCP_PORT))
    server.listen(5)  # Поддерживаем несколько клиентов

    print(f'TCP-сервер запущен на порту {TCP_PORT}')

    while True:
        client_socket, addr = server.accept()
        print(f'Принято соединение от клиента {addr}')
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,addr,))
        client_handler.start()

if __name__ == "__main__":
    tcp_server()
