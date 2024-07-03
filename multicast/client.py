import socket
import struct
import sys


def start_multicast_client(multicast_group, server_address):
    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP)

    # Set a TTL of 1s for the message
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    print('Client started. Sending messages to '
          f'{multicast_group}:{server_address[1]}')

    while True:
        message = input('Enter message: ')
        try:
            # Send the message to the multicast group
            sock.sendto(message.encode(), server_address)
        except Exception as e:
            print(f'Error: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: python {sys.argv[0]} <Multicast IP> <Port>')
        sys.exit(1)

    multicast_ip = sys.argv[1]
    port = int(sys.argv[2])

    try:
        start_multicast_client(multicast_ip, (multicast_ip, port))
    except ValueError:
        print("Invalid port number.")
    except Exception as e:
        print(f"Error: {e}")
