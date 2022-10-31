from GrafoSecuencial import Grafo

if __name__ == "__main__":
    unGrafo = Grafo(7, [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 0, 5), (3, 4, 6)])
    print(unGrafo.camino(1,1))
    print(unGrafo.adyacentes(0))
    print(unGrafo.get_arco(1,1))
    print(unGrafo.get_arco(0,1))
    print(unGrafo.get_arco(0,2))
    print(unGrafo.get_arco(0,3))