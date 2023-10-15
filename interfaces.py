import psutil

def get_network_interfaces():
    interfaces_data = {}
    network_interfaces = psutil.net_if_addrs()
    interface_names = list(network_interfaces.keys())
    for i in interface_names:
        interfaces_data[i] = {}
        for j in network_interfaces[i]:
            if j.family == 2:
                interfaces_data[i]['ipv4'] = j.address
                interfaces_data[i]['netmask'] = j.netmask
            elif j.family == 17:
                interfaces_data[i]['mac'] = j.address
    return interfaces_data


