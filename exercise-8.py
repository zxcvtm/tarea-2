guestsResponse = int(input())
total = 2
for i in range(guestsResponse):
    total = total + len(input().split("+"))
if(total == 13):
    total = total + 1
print(total*100)
