import csv

class Cosecha:

    __ListaCosechas = []

    def __init__(self):
        archivo2 = open("archivoCosechas.csv")
        reader = csv.reader(archivo2, delimiter=",")
        for fila in reader:
            d0 = int(fila[0])  # Id
            d1 = int(fila[1])  # Dia
            d2 = int(fila[2])  # Peso
            if type(d0) == int and type(d1) == int and type(d2) == int:
                self.__ListaCosechas.append([d0, d1, d2])
        archivo2.close()

    def getID(self, dia):
        i = 0
        cant = 0
        listaId = []
        listaId.append(cant)
        while i < 25:
            if dia == self.__ListaCosechas[i][1]:
                cant += 1
                listaId.append([self.__ListaCosechas[i][0], self.__ListaCosechas[i][2]])
            i += 1
        if cant != 0:
            listaId[0] = cant
        return(listaId)

    def getPeso(self, id):
        cant = 0
        retorna = []
        retorna.append(cant)
        i = 0
        while i < 25:
            if id == self.__ListaCosechas[i][0]:
                retorna.append(self.__ListaCosechas[i][2])
                cant = cant + 1
            i += 1
        if cant == 0:
            print(f"La ID {id} no fue encontrada en la lista de cosechas")
        else:
            retorna[0] = cant
            print(f"La ID {id} fue encontrada en la lista de cosechas")
        return (retorna)