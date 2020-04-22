import os
from win10toast import ToastNotifier
toaster = ToastNotifier()
i = 1
while i<10:
    file = open("IPs.txt","r+")
    with open("IPs.txt","r+") as file:
            for line in file:
                response =  os.system("ping   " + line)
            if response == 0:
                print(line + "Связь есть!")
            else:
                with open("cam.txt","a+") as file:
                    aunt1 = line
                    toaster.show_toast("IP-адрес не доступен",aunt1,icon_path="custom.ico",duration=2)
                    print(line + "IP-адрес не доступен")
                    file.write("IP-адрес не доступен:")
                    file.write(line)

