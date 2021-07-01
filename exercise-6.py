sections = int(input())
sectionPower = list(map(int, (input().split())))
ind = 0
MAX = sum(sectionPower[:2])
for i in range(sections - 2):
    if  sum(sectionPower[i:i+3]) > MAX:
        MAX = sum(sectionPower[i:i+3])
        ind = sectionPower.index(sectionPower[i]) + 2

print(MAX, ind)
