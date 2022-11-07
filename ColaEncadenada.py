from Celda import Celda

class ColaEncadenada:
    __primero:Celda = None
    __ultimo:Celda = None

    def __init__(self) -> None:
        self.__primero = None
        self.__ultimo = None
    

    def insertar(self, elemento):
        celda = Celda(elemento)
        if self.__ultimo == None:
            self.__primero = celda
            self.__ultimo = celda
        else:
            self.__ultimo.setSiguiente(celda)
            self.__ultimo = celda
    

    def suprimir(self):
        if self.__primero == None:
            raise Exception("No quedan elementos en la cola")
        elemento = self.__primero.getElemento()
        self.__primero = self.__primero.getSiguiente()
        if self.__primero == None:
            self.__ultimo = None
        return elemento
    
    def vacia(self):
        return self.__primero == None