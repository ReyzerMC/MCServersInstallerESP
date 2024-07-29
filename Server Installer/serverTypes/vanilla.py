from sys import exit
import requests
from subprocess import run

def vanilla():

    url = ''
    seleccion = 0


    def download():
        response = requests.get(url)

        with open('server.jar', 'wb') as file:
            file.write(response.content)
        
    print("Seleccione la version del servidor Java:\n1: 1.21\n-1 para salir")
    seleccion = int(input('>>> '))
        
    if seleccion == 1:
        print("Has seleccionado version 1.21")
        url = 'https://piston-data.mojang.com/v1/objects/450698d1863ab5180c25d7c804ef0fe6369dd1ba/server.jar'
        download()
        mkstart = open("start.bat", "x")
        mkstart.write("java -Xmx20480M -Xms512M -jar server.jar nogui pause")
    elif seleccion == -1:
        exit()