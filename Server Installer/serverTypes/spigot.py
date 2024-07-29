from sys import exit
import requests
from subprocess import run
from time import sleep as pause

def spigot():

    url = ''
    seleccion = 0


    def download():
        response = requests.get(url)

        with open('server.jar', 'wb') as file:
            file.write(response.content)
        
    print("Seleccione la version del servidor Java:\n1: 1.20.1\n2: 1.16.5\n3: 1.8\n-1 para salir")
    seleccion = int(input('>>> '))
        
    if seleccion == 1:
        print("Has seleccionado version 1.20.1")
        url = 'https://download.getbukkit.org/spigot/spigot-1.20.1.jar'
        download()
        mkstart = open("start.bat", "x")
        mkstart.write("java -Xmx20480M -Xms512M -jar server.jar nogui pause")
        pause(3)
        run([".\\start.bat"])
    elif seleccion == 2:
        print("Has seleccionado version 1.16.5")
        url = 'https://download.getbukkit.org/spigot/spigot-1.16.5.jar'
        download()
        mkstart = open("start.bat", "x")
        mkstart.write("java -Xmx20480M -Xms512M -jar server.jar nogui pause")
    elif seleccion == 3:
        print("Has seleccionado version 1.8")
        url = 'https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar'
        download()
        mkstart = open("start.bat", "x")
        mkstart.write("java -Xmx20480M -Xms512M -jar server.jar nogui pause")
    elif seleccion == -1:
        exit()