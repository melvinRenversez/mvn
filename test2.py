import nmap

addres = "192.168.0"

liste_ip = []

def scan_network(host_ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=f'{host_ip}.1/24', arguments='-sn')

    for host in nm.all_hosts():
        print(f"Adresse IP : {host}")
        if 'mac' in nm[host]['addresses']:
            print(f"Adresse MAC : {nm[host]['addresses']['mac']}")
        print(f"État : {nm[host].state()}")

        if 'vendor' in nm[host]:
            print(f"Fabricant : {nm[host]['vendor']}")
        liste_ip.append(host)
        print()
        
    print("list: ", liste_ip)

scan_network(addres)
