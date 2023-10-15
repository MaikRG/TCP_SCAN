from scapy.all import *
from scapy.layers.inet import TCP, IP



        
def sniff_iface(iface, ip_dst):
    
    def packet_callback(packet):
        if packet.haslayer(TCP):
            if packet[IP].dst == '192.168.3.24' or packet[IP].src == '192.168.3.24':
                if packet[TCP].flags == 'S':
                    print("Paquete SYN")
                elif packet[TCP].flags == 'SA':
                    print(f"Paquete SYN-ACK")
                elif packet[TCP].flags == 'A':
                    print(f"Paquete ACK")
                else:
                    print(packet[TCP].flags)
                print(f"{packet[IP].src}:{packet[TCP].sport} ---> {packet[IP].dst}:{packet[TCP].dport}")
                print(packet.show())
                print("--------------------------------------------------")
                
            
    # Empieza a capturar paquetes en la interfaz de red seleccionada
    sniff( prn=packet_callback, iface=iface)
