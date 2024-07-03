import socket
import struct
import sys


def start_multicast_server(multicast_group, server_address):
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Allow multiple sockets to use the same port number
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the server address
    sock.bind(server_address)

    # Tell operating system to add the socket to the multicast group
    # on all interfaces
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sl', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(f'Server started on {server_address[0]}:{server_address[1]}'
          f'in multicast group {multicast_group}')

    while True:
        data, address = sock.recvfrom(1024)
        print(f'REceived {data.decode()} from {address}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: python {sys.argv[0]} <Multicast IP> <Port>')
        sys.exit(1)

    multicast_ip = sys.argv[1]
    port = int(sys.argv[2])

    try:
        start_multicast_server(multicast_ip, ('', port))
    except ValueError:
        print("Invalid port number.")
    except Exception as e:
        print(f'Error: {e}')
