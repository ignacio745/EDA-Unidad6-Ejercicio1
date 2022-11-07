from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Nodo import Nodo

class Nodo:
    __sig: Nodo
    __elemento: None

    def __init__(self, elemento):
        self.__sig = None
        self.__elemento = elemento
    
    def getSig(self) -> Nodo:
        return self.__sig
    
    def setSig(self, sig:Nodo):
        self.__sig = sig
    
    def getElemento(self):
        return self.__elemento
    
    def setElemento(self, elemento):
        self.__elemento = elemento