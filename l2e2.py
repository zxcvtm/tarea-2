algorithm = """
def calcula_interseccion_fixed(lista1,lista2):
    lista2Copy = lista2.copy()
    lista_comun = []
    for e1 in lista1:
        for e2 in lista2Copy:
            if(e1==e2):
                lista_comun.append(e1)
                lista2Copy.remove(e2)
                break
    return lista_comun
"""
print(algorithm)
explanation = "Suponiendo que el arreglo 1 es de largo n, el arreglo 2 es de largo m y acceder a cualquier posición del arreglo tiene un costo de 1. Dado que se tiene que recorrer el arreglo 1 completo y por cada elemento se recorrer el arreglo 2 hasta encontrar una igualdad. En el peor de los casos puede no existir una intersección, el arreglo se recorre nxm veces. Por lo que la complejidad seria O(nxm)"
print(explanation)
