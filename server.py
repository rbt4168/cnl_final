import socket
import random
# Set up the UDP client
UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 5005     # The port to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    rand = random.getrandbits(32)
    print(f"Received message: {data.decode()} from {addr}, number {rand}")

    # Send a response back to the sender
    response_message = f"Hello, UDP server! Number {rand}"
    print("My response message is:", response_message)
    sock.sendto(response_message.encode(), addr)
    print(f"Sent response to {addr}")
