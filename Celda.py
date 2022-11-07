class Celda:
    __elemento = None
    __sig = None

    def __init__(self, elemento) -> None:
        self.__elemento = elemento
        self.__sig = None
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente
    
    def getSiguiente(self):
        return self.__sig
    
    def getElemento(self):
        return self.__elemento