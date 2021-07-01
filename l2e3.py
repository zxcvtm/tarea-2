
def getKeyFromArrayValueDict(array):
    keyFromArrayValueDict = {}
    for index, value in enumerate(array):
        keyFromArrayValueDict[value] = index
    return keyFromArrayValueDict
    
