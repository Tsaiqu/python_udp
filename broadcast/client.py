import socket
import sys


def start_broadcast_client(broadcast_address):
    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Allow the socket to send broadcasts
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f'Client started. Sending messages to {
          broadcast_address[0]}:{broadcast_address[1]}')

    while True:
        message = input('Enter message: ')
        try:
            # Send the message to the broadcast address
            sock.sendto(message.encode(), broadcast_address)
        except Exception as e:
            print(f"Error: {e}")


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

    start_broadcast_client((broadcast_ip, port))
