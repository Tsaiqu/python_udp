import socket
import sys


def start_broadcast_server(server_address):
    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Allow multiple sockets to use the same PORT number
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the server address
    try:
        sock.bind(server_address)
    except socket.error as e:
        print(f"Failed to bind socket: {e}")
        sys.exit(1)

    print(f'Server started on {server_address[0]}:{server_address[1]}')

    while True:
        data, address = sock.recvfrom(1024)
        print(f'Received {data.decode()} from {address}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: python {sys.argv[0]} <Broadcast IP> <Port>')
        sys.exit(1)

    broadcast_ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
        if not (0 <= port <= 65535):
            raise ValueError
    except ValueError:
        print("Invalid port number. Port must be an integer between "
              "0 and 65535.")
        sys.exit(1)

    start_broadcast_server((broadcast_ip, port))
