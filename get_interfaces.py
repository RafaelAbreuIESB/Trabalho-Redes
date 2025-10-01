from scapy.all import conf

print("Placas de rede encontradas pelo Scapy:")
conf.ifaces.show()