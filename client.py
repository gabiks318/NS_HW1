import sys
import socket


if __name__ == '__main__':
    # Get Args
    host: str = sys.argv[1]
    port: int = int(sys.argv[2])

    # Create connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send request and wait for result
    get_request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client_socket.send(get_request.encode())

    response = client_socket.recv(1024).decode()
    print(response)
