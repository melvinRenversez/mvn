import socket

def get_hostname(ip_address):
    try:
        # Effectuer une résolution DNS inverse à l'aide de socket
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return "Nom d'hôte non disponible"

# Adresse IP pour laquelle vous voulez récupérer le nom d'hôte
ip_address = "10.244.105.167"

# Récupération du nom d'hôte associé à l'adresse IP
hostname = get_hostname(ip_address)
print(f"Nom d'hôte associé à l'adresse IP {ip_address} : {hostname}")
