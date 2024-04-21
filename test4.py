import nmap

def scan_network(target_ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments='-sP')

    for host in nm.all_hosts():
        print(f"Adresse IP : {host}")
        hostname = nm[host]
        print(f"Nom d'hôte : {hostname}")

# Utilisation de la fonction pour scanner une adresse IP précise
target_ip = "192.168.0.41"
scan_network(target_ip)
