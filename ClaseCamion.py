import csv
from ClaseManejadorListaCamiones import ManejadorCamiones

class Camion:

    __Id = 0
    __Nomb = ""
    __Patte = 0
    __Marca = ""
    __Tara = 0

    def __init__(self, v1 = 1, v2 = "Ejemplo", v3 = "AAA111", v4 = "Volkswagen", v5 = 500):
        self.__Id = v1
        self.__Nomb = v2
        self.__Patte = v3
        self.__Marca = v4
        self.__Tara = v5

    def Carga(self):
        MCamiones = ManejadorCamiones()
        archivo1 = open("archivoCamiones.csv")
        reader = csv.reader(archivo1, delimiter=",")
        for fila in reader:
            d0 = int(fila[0])  # Id
            d1 = str(fila[1])  # Nomb
            d2 = str(fila[2])  # Patte
            d3 = str(fila[3])  # Marca
            d4 = int(fila[4])  # Tara
            if type(d0) == int and type(d1) == str and type(d2) == str and type(d3) == str and type(d4) == int:
                v1 = [d0, d1, d2, d3, d4]
                MCamiones.Agregar(v1)
        archivo1.close()
        return (MCamiones)