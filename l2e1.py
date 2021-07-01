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
