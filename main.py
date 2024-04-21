import threading
from pythonping import ping

def ping_and_append(host, results):
    response = ping(host, count=1)
    if response.success():
        print("Ping réussi vers", host)
        for reply in response:
            print("Réponse :", reply)
        results.append(host)
    else:
        print("Échec du ping vers", host)

list_ip = []

for i in range(1, 255):
        host = f"192.168.0.{i}"
        thread = threading.Thread(target=ping_and_append, args=(host, list_ip))
        thread.start()

print("Attente de la fin des threads...")

# Attendre que tous les threads se terminent
main_thread = threading.currentThread()
for thread in threading.enumerate():
    if thread is not main_thread:
        thread.join()

print("Liste des adresses IP avec ping réussi :", list_ip)
