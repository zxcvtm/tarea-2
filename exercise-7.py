input()
block1 = set(map(int, (input().split())))
input()
block2 = set(map(int, (input().split())))
input()
block3 = set(map(int, (input().split())))

print(len(block1.intersection(block2).intersection(block3)))
