from interfaces import get_network_interfaces
from sniffer import sniff_iface

if __name__ == "__main__":

        interfaces = get_network_interfaces()
        interfaces_names = list(interfaces.keys())
        for idx, i in enumerate(interfaces_names):
            print(f"{idx} - {i} -> {interfaces[i]['ipv4']} / {interfaces[i]['netmask']}")

        interface_index_selected = int(input(f"Select network interface (0-{len(interfaces_names) - 1}):  "))
        interface_name_selected = interfaces_names[interface_index_selected]
        interface_ipv4_selected = interfaces[interface_name_selected]['ipv4']
        print("Selected: ", interface_name_selected)
        print("Starting sniffing...")
        sniff_iface(interface_name_selected, interface_ipv4_selected)
