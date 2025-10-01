from scapy.all import sniff, IP, TCP, UDP, ICMP
from aggregator import add_packet
from config import SERVER_IP, CAPTURE_INTERFACE

def handle_packet(pkt):
    if not pkt.haslayer(IP):
        return
    ip = pkt[IP]
    size = len(pkt)
    proto = "OTHER"
    if pkt.haslayer(TCP):
        proto = "TCP"
    elif pkt.haslayer(UDP):
        proto = "UDP"
    elif pkt.haslayer(ICMP):
        proto = "ICMP"

    if ip.dst == SERVER_IP:
        add_packet(ip.src, "in", size, proto)
    elif ip.src == SERVER_IP:
        add_packet(ip.dst, "out", size, proto)

def start_sniffer():
    sniff(prn=handle_packet, store=False, iface=CAPTURE_INTERFACE)



