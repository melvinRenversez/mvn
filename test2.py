import threading
import nmap

def scan_network(i):
    nm = nmap.PortScanner()
    nm.scan(hosts=f'10.244.{i}.1/24', arguments='-sn')  # Utilisez f-string pour formater l'adresse IP avec la valeur de i

    for host in nm.all_hosts():
        print(f"Adresse IP : {host}")
        if 'mac' in nm[host]['addresses']:
            print(f"Adresse MAC : {nm[host]['addresses']['mac']}")
        print(f"État : {nm[host].state()}")

        if 'vendor' in nm[host]:
            print(f"Fabricant : {nm[host]['vendor']}")

        print()

for i in range( 255):
    print(i)
    thread = threading.Thread(target=scan_network, args=(i,))
    thread.start()

print("Attente de la fin des threads...")

main_thread = threading.currentThread()
for thread in threading.enumerate():
    if thread is not main_thread:
        thread.join()
