from scapy.all import sniff, IP
from aggregator import add_packet
from config import SERVER_IP

def handle_packet(pkt):
    if not pkt.haslayer(IP):
        return
    ip = pkt[IP]
    size = len(pkt)

    if ip.dst == SERVER_IP:
        add_packet(ip.src, "in", size)
    elif ip.src == SERVER_IP:
        add_packet(ip.dst, "out", size)

def start_sniffer():
    sniff(prn=handle_packet, store=False, iface="Wi-Fi")



