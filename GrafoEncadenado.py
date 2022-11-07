import numpy as np
from Lista import Lista

class GrafoEncadenado:
    __cant_nodos: int
    __arreglo: np.ndarray
    
    
    def __init__(self, nodos:int, arcos:list[tuple[int]]) -> None:
        self.__cant_nodos = nodos
        self.__arreglo = np.empty(self.__cant_nodos, Lista)
        for i in range(self.__cant_nodos):
            self.__arreglo[i] = Lista()
        for i, j, k in arcos:
            self.__arreglo[i].set_arco((j, k))
        
    
    
    def set_arco(self,  nodo_origen:int, nodo_destino:int, valor:int):
        self.__arreglo[nodo_origen].set_arco((nodo_destino, valor))
        
    
    def get_arco(self, nodo_origen:int, nodo_destino:int):
        return self.__arreglo[nodo_origen].get_arco(nodo_destino)
    
    
    def adyacentes(self, un_nodo) -> list[int]:
        nodos:list[int] = []
        for i in range(self.__cant_nodos):
            if  self.get_arco(un_nodo, i) != 0:
                nodos.append(i)
        return nodos
    
    

    def camino(self, nodo_origen:int, nodo_destino:int):
        d = np.empty(self.__cant_nodos, int)
        d.fill(0)
        resultado = self.camino_aux(nodo_origen, nodo_destino, d)
        if isinstance(resultado,list):
            resultado.insert(0,nodo_origen)
        return resultado
         
            

    
    def camino_aux(self, nodo_origen:int, nodo_destino:int, d:np.ndarray):
        d[nodo_origen] = 1
        adys = self.adyacentes(nodo_origen)
        band = False
        i = 0
        while i < len(adys) and adys[i] != nodo_destino and not band:
            un_nodo = adys[i]
            i += 1
            if d[un_nodo] == 0:
                retorno = self.camino_aux(un_nodo, nodo_destino, d)
                if isinstance(retorno, list):
                    band = True

        if i < len(adys) and adys[i] == nodo_destino:
            retorno = [nodo_destino]
        elif band:
            retorno.insert(0, un_nodo)
        else:
            retorno = 0
        
        return retorno



    

    def get_corto_desconocido(self, distancias:np.ndarray, conocidos:np.ndarray):
        mas_corto = 0
        for i in range(self.__cant_nodos):
            if conocidos[i] == False:
                mas_corto = i
                break
        for i in range(self.__cant_nodos):
            if conocidos[i] == False and distancias[i] < distancias[mas_corto]:
                mas_corto = i
        return mas_corto
    

    def camino_mas_corto(self, nodo_origen:int, nodo_destino:int):
        distancias = np.empty(self.__cant_nodos, int)
        conocidos = np.empty(self.__cant_nodos, bool)
        caminos = np.empty(self.__cant_nodos, int)
        distancias.fill(10000000000)
        for i in range(self.__cant_nodos):
            conocidos[i] = False
        caminos.fill(-1)
        distancias[nodo_origen] = 0
        for i in range(self.__cant_nodos):
            v = self.get_corto_desconocido(distancias, conocidos)
            conocidos[v] = True
            adys = self.adyacentes(v)
            for w in adys:
                if conocidos[w] == False:
                    if distancias[v] + self.get_arco(v, w) < distancias[w]:
                        distancias[w] = distancias[v] + self.get_arco(v, w)
                        caminos[w] = v
        if caminos[nodo_destino]==-1:
            raise Exception("No hay camino")
        i = caminos[nodo_destino]
        nodos_camino = [nodo_destino]
        while i != nodo_origen:
            nodos_camino.insert(0, i)
            i = caminos[i]
        nodos_camino.insert(0, nodo_origen)
        return nodos_camino



    

    def conexo(self) -> bool:
        matriz = np.empty((self.__cant_nodos, self.__cant_nodos), int)
        matriz_aux = np.empty((self.__cant_nodos, self.__cant_nodos), int)
        matriz_conectividad = np.empty((self.__cant_nodos, self.__cant_nodos), int)
        for i in range(self.__cant_nodos):
            for j in range(self.__cant_nodos):
                matriz[i, j] = self.get_arco(i, j)
                matriz_aux[i, j] = self.get_arco(i, j)
                matriz_conectividad[i, j] = self.get_arco(i, j)
        
        for i in range(self.__cant_nodos):
            matriz_aux = np.matmul(matriz, matriz_aux)
            matriz_conectividad = matriz_conectividad + matriz_aux
        
        i = 0
        j = 0

        while i < self.__cant_nodos and j < self.__cant_nodos and (matriz_conectividad[i, j] != 0 or i!=j):
            j = 0
            while j < self.__cant_nodos and matriz_conectividad[i, j] != 0:
                j += 1
            i += 1
        
        return i == self.__cant_nodos or j==self.__cant_nodos
    

    def arbol_recubrimiento(self):
        distancias = np.empty(self.__cant_nodos, int)
        conocidos = np.empty(self.__cant_nodos, bool)
        caminos = np.empty(self.__cant_nodos, int)
        distancias.fill(10000000000)
        for i in range(self.__cant_nodos):
            conocidos[i] = False
        caminos.fill(-1)
        distancias[0] = 0
        for i in range(self.__cant_nodos):
            v = self.get_corto_desconocido(distancias, conocidos)
            conocidos[v] = True
            adys = self.adyacentes(v)
            for w in adys:
                if conocidos[w] == False:
                    if self.get_arco(v, w) < distancias[w]:
                        distancias[w] = self.get_arco(v, w)
                        caminos[w] = v
        
        arcos = []
        for i in range(self.__cant_nodos):
            if caminos[i] != -1:
                arcos.append((i, caminos[i], distancias[i]))
        
        un_grafo = GrafoEncadenado(self.__cant_nodos, arcos)

        return un_grafo
    

    def __str__(self) -> str:
        cadena = ""
        for i in range(self.__cant_nodos):
            for j in range(i, self.__cant_nodos):
                if self.get_arco(i, j) > 0:
                    cadena += "({0}, {1}, {2})".format(i, j, self.get_arco(i,j))
        return cadena