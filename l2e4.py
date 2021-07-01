algorithm = """
def getKeyFromArrayValueDict(array):
    keyFromArrayValueDict = {}
    for index, value in enumerate(array):
        keyFromArrayValueDict[value] = index
    return keyFromArrayValueDict
"""
print(algorithm)
explanation = "por cada arreglo de largo n que recibe de entrada, debe recorrerlo completo. Si consideramos que acceder al elemento del arreglo y la inserción dentro del diccionario con un costo de 1, podemos decir que, este algoritmo es O(n)"
print(explanation)
