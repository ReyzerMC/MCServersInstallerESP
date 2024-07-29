from serverTypes import spigot, vanilla

seleccion = 0

print("seleccione el tipo de servidor que desea:\n1: Spigot\n2: Vanilla (Solo version mas reciente)")

seleccion = int(input('>>> '))

if seleccion == 1:
    print("Seleccionaste Spigot")
    mkelua = open('eula.txt', 'x')
    mkelua.write('eula=true')
    spigot.spigot()
elif seleccion == 2:
    print("Seleccionaste Vanilla")
    mkelua = open('eula.txt', 'x')
    mkelua.write('eula=true')
    vanilla.vanilla()