from IP import IP

# Créez une instance de la classe IP
ip_instance = IP()

# Appelez la méthode GetAllIp sur l'instance de la classe IP en fournissant l'argument host_ip
ip_list = ip_instance.GetAllIp("192.168.0")

# Affichez la liste des adresses IP trouvées
print("Liste des adresses IP trouvées :", ip_list)
