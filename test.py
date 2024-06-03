from scapy.all import *
import time

# Configuration
victim_ip = '192.168.1.137'  # Victim's IP address
attacker_ip = '192.168.1.146'  # Attacker's IP address
iface = 'en0'  # Network interface to use

# Send a simple UDP packet from attacker to victim
while True:
    packet = IP(src=attacker_ip, dst=victim_ip) / UDP(dport=50617) / Raw(load="Hello, this is a test")
    send(packet, iface=iface)
    print(f"Sent UDP packet: {packet.summary()}")
    time.sleep(1)