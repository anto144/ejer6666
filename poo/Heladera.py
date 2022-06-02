from Aparato import Aparato
class Heladera (Aparato):
    __capacidadL=""
    __freezer=""
    __ciclica=""

    def __init__(self, marca, modelo, color, pf, precio, capL, freezer, ciclica):
        super().__init__(marca, modelo, color, pf, precio)
        self.__capacidadL = capL
        self.__freezer = freezer
        self.__ciclica = ciclica

    def getCapacidadL(self):
        return self.__capacidadL

    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica

    def getImporte(self):
        importe = self.getPrecio()
        if self.__freezer:
            importe += self.getPrecio() * 0.05
        else:
            importe += self.getPrecio() * 0.01
        if self.__ciclica:
            importe += self.getPrecio() * 0.1
        return importe

