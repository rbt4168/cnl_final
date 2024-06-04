import socket

# Set up the UDP client
UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 5005     # The port to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}")

while True:
    try:
        # Receive data from the socket
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes

        # Ignore the received packet, don't send any response
    except socket.timeout:
        # If a timeout occurs, continue listening
        continue