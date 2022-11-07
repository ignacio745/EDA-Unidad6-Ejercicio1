from Nodo import Nodo

class Lista:
    __cabeza: (Nodo | None)

    def __init__(self):
        self.__cabeza = None
    
    def set_arco(self, unArco:tuple[int]):
        if self.__cabeza != None:
            actual = self.__cabeza
            while actual != None and actual.getElemento()[0] != unArco[0]:
                actual = actual.getSig()
            if actual == None:
                un_nodo = Nodo(unArco)
                un_nodo.setSig(self.__cabeza)
                self.__cabeza = un_nodo
            else:
                actual.setElemento(unArco)
        else:
            un_nodo = Nodo(unArco)
            un_nodo.setSig(self.__cabeza)
            self.__cabeza = un_nodo
    
    def get_arco(self, unNodo:int):
        retorno = 0
        if self.__cabeza != None:
            actual = self.__cabeza
            while actual != None and actual.getElemento()[0] != unNodo:
                actual = actual.getSig()
            if actual != None:
                retorno = actual.getElemento()[1]
        return retorno