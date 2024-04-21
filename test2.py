import dns.resolver

def get_hostname(ip_address):
    try:
        # Effectuer une requête DNS inverse pour obtenir le nom d'hôte
        result = dns.resolver.resolve_address(ip_address, 'PTR')
        # Récupérer le nom d'hôte à partir du résultat de la requête DNS
        hostname = str(result[0])[:-1]  # Retirer le point à la fin du nom d'hôte
        return hostname
    except dns.resolver.NXDOMAIN:
        return "Nom d'hôte non disponible"
    except dns.resolver.NoAnswer:
        return "Aucune réponse trouvée"
    except dns.exception.Timeout:
        return "Délai d'attente dépassé"

# Adresse IP pour laquelle vous voulez récupérer le nom d'hôte
ip_address = "192.168.0.41"

# Récupération du nom d'hôte associé à l'adresse IP
hostname = get_hostname(ip_address)
print(f"Nom d'hôte associé à l'adresse IP {ip_address} : {hostname}")
