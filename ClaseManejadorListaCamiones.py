

class ManejadorCamiones:

    __ListaCamiones = []

    def __init__(self):
        self.__ListaCamiones = []

    def Agregar(self, v1):
        self.__ListaCamiones.append(v1)

    def getTara(self, id):
        i = 0
        retorna = 0
        while i < 20:
            if id == self.__ListaCamiones[i][0]:
                retorna = self.__ListaCamiones[i][4]
                i = 20
            else:
                i += 1
        if retorna == 0:
            print(f"La ID {id} no fue encontrada en la lista de camiones")
        else:
            print(f"La ID {id} fue encontrada en la lista de camiones")
        return (retorna)

    def Muestra(self, listaID):
        j = 1
        print("PATENTE     NOMBRE     PESO")
        cant = listaID[0]
        while j < cant+1:
            i = 0
            while i < 20:
                if listaID[j][0] == self.__ListaCamiones[i][0]:
                    print(f"{self.__ListaCamiones[i][2]} {self.__ListaCamiones[i][1]} {listaID[j][1]-self.__ListaCamiones[i][4]}")
                i += 1
            j += 1