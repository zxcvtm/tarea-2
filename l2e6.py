import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
dataFrame = pd.read_csv('MAPF_Algorithms.csv', sep='\t', decimal=',')

def getTimeVSResolvedInstances(frame, statusField, timeField):
    newFrame = frame.copy().loc[(frame[statusField] == 0)]
    newFrame = newFrame.sort_values(timeField)
    newFrame = newFrame.groupby([timeField]).size().reset_index(name='counts')
    newFrame['counts'] = newFrame['counts'].cumsum()
    return newFrame

MtMS = getTimeVSResolvedInstances(dataFrame.iloc[:, [0,1,2,3]], "Status MtMS", "Time SOC MtMS")
ASP_E = getTimeVSResolvedInstances(dataFrame.iloc[:, [0, 4, 5, 6]], "Status ASP Base E", "Time SOC ASP Base E")
ASP_F = getTimeVSResolvedInstances(dataFrame.iloc[:, [0, 7, 8, 9]], "Status Base F", "Time SOC Base F")
CBS = getTimeVSResolvedInstances(dataFrame.iloc[:, [0, 10, 11, 12]], "Status CBS", "Time SOC CBS")
BCP = getTimeVSResolvedInstances(dataFrame.iloc[:, [0, 13, 14, 15]], "Status BCP", "Time SOC BCP")

plt.plot(MtMS["Time SOC MtMS"], MtMS["counts"], label='MtMS')
plt.plot(ASP_E["Time SOC ASP Base E"], ASP_E["counts"], label='ASP Base E')
plt.plot(ASP_F["Time SOC Base F"], ASP_F["counts"], label='Base F')
plt.plot(CBS["Time SOC CBS"], CBS["counts"], label='CBS')
plt.plot(BCP["Time SOC BCP"], BCP["counts"], label='BCP')

#add step size of 50
plt.xticks(np.arange(0, 650, 50))

plt.legend()
plt.title("Rendimiento de testeo algoritmico")
plt.xlabel('Tiempo')
plt.ylabel('Instancias Resueltas')
plt.grid()
plt.show()
