import pandas as pd
dataFrame = pd.read_csv('MAPF_Algorithms.csv', sep='\t', decimal=',')

description = {
    "Instance": "Contiene los nombres de las instancias de prueba",
    "Status [Nombre_Algoritmo]": "Indica el estado de solución del algoritmo Nombre_Algoritmo en la instancia correspondiente. El estado 0 significa que la instancia fue resuelta de manera óptima, el estado 1 significa que se pudo encontrar el makespan óptimo, pero no la solución SOC_Optima. El estado 2 significa que se encontró al menos una solución, mas no se pudo certificar su calidad y, finalmente, el estado 3 significa que no se pudo encontrar ninguna solución para la instancia.",
    "Cost SOC [Nombre_Algoritmo]": "Indica el mejor costo encontrado por el algoritmo Nombre_Algoritmo para cada instancia. En caso de que no se haya encontrado ninguna solución, el costo vale -1.",
    "Time SOC [Nombre_Algoritmo]":"Indica el tiempo de término del algoritmo Nombre_Algoritmo en cada instancia. Este tiempo será menor a 600 si la instancia fue resuelta a optimalidad. En caso contrario, el tiempo será de 600 segundos."
}

for key, value in description.items():
 print(key, ': ', value)

print(dataFrame.describe(include = 'all'))
