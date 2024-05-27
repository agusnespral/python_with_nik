tramosYCantidades = {}
cantidadBoletos = 0
cantidadRestante = 0
sacarMasBoletos = True
def eligeTramoYCantidad():
    global cantidadBoletos, tramo, tramosYCantidades, cantidadPorTramo, sacarMasBoletos

    while sacarMasBoletos and cantidadBoletos < 10:

        tramo = input('Elija el tramo para el cual quiere sacar boletos')
        checkTramo()

        cantidadPorTramo = int(input('Indique la cantidad de boletos que desea para el tramo seleccionado'))
        cantidadBoletos += cantidadPorTramo
        checkLimiteBoletos()

        tramosYCantidades["tramo {0}".format(tramo)] = cantidadPorTramo
        print('Su compra:', tramosYCantidades)

        if cantidadBoletos < 10:
            masBoletos()
def checkTramo():
    if tramo != 'a' and tramo != 'b' and tramo != 'c':
        print('El tramo seleccionado no existe.')
        eligeTramoYCantidad()
    if 'tramo ' + tramo in tramosYCantidades:
        print('Usted ya saco pasajes para el tramo seleccionado. No joda.')
        eligeTramoYCantidad()
def checkLimiteBoletos():
    global cantidadBoletos
    if cantidadBoletos > 10:
        print('La cantidad de boletos excede el limite de 10 boletos por compra')
        cantidadBoletos -= cantidadPorTramo
        eligeTramoYCantidad()
def masBoletos():
    global sacarMasBoletos
    masBoletos = input('Presione s si desea sacar mas boletos o enter para salir')
    if masBoletos == 's':
        sacarMasBoletos = True
    else:
        sacarMasBoletos = False

#main flow
mensaje_bienvenida = ("Bienvenido a la linea de colectivos 21. \nAl momento contamos con tres tramos: \n"
                      "TRAMO a: $4.25\n"
                      "TRAMO b: $8.75\n"
                      "TRAMO c: $12.50\n"
                      "El maximo de pasajes que puede sacar son 10")

print(mensaje_bienvenida)
eligeTramoYCantidad()

