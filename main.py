from IP import IP


ip_instance = IP()

ip_list = ip_instance.scanIp("192.168.0.41")

print("Liste des adresses IP trouvées :", ip_list)
