import socket
import threading

# Порты для серверов TCP и UDP
TCP_PORT = 12345
UDP_PORT = 54321

def handle_tcp_client(tcp_client_socket,tcp_addr):
    while True:
        message = tcp_client_socket.recv(1024).decode()
        if not message:
            break
        print(f'Получено TCP-сообщение от {tcp_addr}: {message}')
        
        # Ваш код для обработки сообщения, например, отправить ответ
        response = f'Принято сообщение от TCP-клиента: {message}'.encode()
        tcp_client_socket.send(response)
    
    tcp_client_socket.close()

def tcp_server():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('0.0.0.0', TCP_PORT))
    tcp_server_socket.listen(5)  # Поддерживаем несколько клиентов

    print(f'TCP-сервер запущен на порту {TCP_PORT}')

    while True:
        tcp_client_socket, tcp_addr = tcp_server_socket.accept()
        print(f'Принято соединение от TCP-клиента {tcp_addr}')
        
        tcp_client_handler = threading.Thread(target=handle_tcp_client, args=(tcp_client_socket,tcp_addr,))
        tcp_client_handler.start()

def udp_server():
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(('0.0.0.0', UDP_PORT))

    print(f'UDP-сервер запущен на порту {UDP_PORT}')

    while True:
        data, udp_addr = udp_server_socket.recvfrom(1024)
        print(f'Получено UDP-сообщение от {udp_addr}: {data.decode()}')

        # Ваш код для обработки UDP-сообщения, например, отправить ответ
        response = f'Принято UDP-сообщение: {data.decode()}'.encode()
        udp_server_socket.sendto(response, udp_addr)

if __name__ == "__main__":
    # Создаем отдельные потоки для TCP и UDP серверов
    tcp_thread = threading.Thread(target=tcp_server)
    udp_thread = threading.Thread(target=udp_server)

    tcp_thread.start()
    udp_thread.start()

    tcp_thread.join()
    udp_thread.join()
