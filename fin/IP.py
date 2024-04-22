import nmap

class IP:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def GetAllIp(self, host_ip):
        liste_ip = []
        nm = nmap.PortScanner()
        nm.scan(hosts=f'{host_ip}.1/24', arguments='-sn')

        for host in nm.all_hosts():
            print("~# ", host)
            liste_ip.append(host)
            
        return liste_ip
    
    def scanIp(self, target_ip):
        nm = nmap.PortScanner()
        nm.scan(hosts=target_ip, arguments='-sP')

        for host in nm.all_hosts():
            print(f"Adresse IP : {host}")
            if 'mac' in nm[host]['addresses']:
                print(f"~# Adresse MAC : {nm[host]['addresses']['mac']}")
            print(f"État : {nm[host].state()}")

            if 'vendor' in nm[host]:
                print(f"~# Fabricant : {nm[host]['vendor']}")
            print()