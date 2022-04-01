import sys
import socket

if __name__ == '__main__':
    # Get Args
    host: str = "127.0.0.1"
    port: int = int(sys.argv[1])

    # Create Server and listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    connection, address = server_socket.accept()

    # Send data to connection
    data = connection.recv(1024)

    with open("example.html", "r") as f:
        content = f.read()

    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{content}"
    connection.send(response.encode())

    # Close sockets
    connection.close()
    server_socket.close()
