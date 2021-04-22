from ClaseManejadorListaCamiones import ManejadorCamiones
from ClaseCamion import Camion
from ClaseCosecha import Cosecha
import os

def Opcion0():
    print("Ingrese numero de identificacion del camion")
    id = int(input("ID: "))
    tara = ListaCamiones.getTara(id)
    if tara != 0:
        pesoycant = MCosechas.getPeso(id)
        if pesoycant[0] != 0:
            peso = 0
            cant = (pesoycant[0])
            i = 1
            while i < cant+1:
                peso += pesoycant[i]
                i += 1
            result = int(peso - tara * pesoycant[0])
            os.system ("cls")
            print(f"El peso descargado por el camion de ID {id} es de {result}")
        else:
            print(f"error en la busqueda, ID {id} no encontrada")
    else:
        print(f"error en la busqueda, ID {id} no encontrada")

def Opcion1():
    print("Ingrese un numero de dia para obtener resultados")
    dia = int(input("Dia: "))
    ListaID = MCosechas.getID(dia)
    ListaCamiones.Muestra(ListaID)

switcher = {
    0: Opcion0,
    1: Opcion1
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__=='__main__':
    ListaCamiones = ManejadorCamiones()
    MCamiones = Camion()
    ListaCamiones = MCamiones.Carga()

    MCosechas = Cosecha()

    bandera = False
    while not bandera:
        print("MENU DE OPCIONES")
        print("0: Ingrese numero de camion para obtener la cantidad de peso descargado")
        print("1: Ingrese numero de un dia para obener la cosecha del dia")
        print("2: Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 2:
            bandera = True
        else:
            os.system ("cls")
            switch(opcion)
            os.system("pause")
            os.system ("cls")