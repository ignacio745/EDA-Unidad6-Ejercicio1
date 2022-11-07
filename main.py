from GrafoEncadenado import GrafoEncadenado

if __name__ == "__main__":
    unGrafo = GrafoEncadenado(7, [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 0, 5), (3, 4, 6), (5, 4, 2), (5, 6, 1), (0, 4, 5)])
    # print(unGrafo.camino(1,1))
    # print(unGrafo.adyacentes(0))
    # print(unGrafo.get_arco(1,1))
    # print(unGrafo.get_arco(0,1))
    # print(unGrafo.get_arco(0,2))
    # print(unGrafo.get_arco(0,3))
    otroGrafo = unGrafo.arbol_recubrimiento()
    print(unGrafo.camino_mas_corto(0, 5))
    print(unGrafo)
    print("\n\n")
    print(otroGrafo)