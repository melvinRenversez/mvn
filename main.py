import os
from IP import IP

run  = True

ip_instance = IP()

while run:
    choise = input('~# ')
    choiseSlipt = choise.split(" ")
    print(choiseSlipt)
    if choiseSlipt[0] == "ip":
        if choiseSlipt[1] == "-show":
            list_ip = ip_instance.GetAllIp(choiseSlipt[2])
            if choiseSlipt[3] == "-sv":
                print(list_ip)
                with open (choiseSlipt[4], 'w') as file:
                    file.write('\n'.join(list_ip))
        if choiseSlipt[1] == "-inf":
            ip_instance.scanIp(choiseSlipt[2])
    if choiseSlipt[0] == "bye":
        run = False 

os.system("pause")