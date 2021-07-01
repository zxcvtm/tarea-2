size = int(input())
files = []
for i in range(size):
    file = list(map(int, (input().split())))
    file.reverse()
    files.append(file)

order = []
selectedFile = 0
for i in range(size*size):
    order.append(str(files[selectedFile].pop()))
    selectedFile = selectedFile - 1
    if(selectedFile < 0 or (len(files[selectedFile]) == 0)):
        filesLength = list(map(len, files))
        selectedFile = filesLength.index(max(filesLength))

print(" ".join(order))
    
    
