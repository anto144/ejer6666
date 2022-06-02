class Aparato:
    __marca=""
    __modelo=""
    __color=""
    __paisF=""
    __precio=""

    def __init__(self,marca,modelo,color,pf,precio):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisF=pf
        self.__precio=precio

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color

    def getPaisF(self):
        return self.__paisF

    def getPrecio(self):
        return self.__precio
        
    






