from Aparato import Aparato
class Lavarropas ( Aparato):
    __capacidadLavado=""
    __velocidad=""
    __cantProgramas =""
    __tipoCarga=""

    def __init__(self, marca, modelo, color, pf, precio,capLav, velocidad, cantProgramas,tipoCarga):
        super().__init__(marca, modelo, color, pf, precio)
        self.__capacidadLavado=capLav
        self.__velocidad=velocidad
        self.__cantProgramas=cantProgramas
        self.__tipoCarga=tipoCarga
    
    def getCapacidadLav(self):
        return self.__capacidadLavado
    
    def getVelocidad(self):
        return self.__velocidad
    
    def getCantidadP(self):
        return self.__cantProgramas
    
    def getTipoCarga(self):
        return self.__tipoCarga

    def getImporte(self):
        importe = self.getPrecio()
        if self.__capacidadLavado <= 5:
            importe += self.getPrecio() * 0.01
        else: 







Importe de venta de los Lavarropas es el precio base, mas: 
el 1% si la capacidad de lavado es menor o igual a 5 kg , 
3% si la capacidad de lavado supera los 5 kg. 




