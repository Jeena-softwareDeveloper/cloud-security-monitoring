import scapy.all as scapy

def scan(target):
    arp_request = scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

if __name__ == "__main__":
    target_ip = input("Enter the target IP range (e.g., 192.168.1.0/24): ")
    scan(target_ip)
