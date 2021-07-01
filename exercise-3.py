firstCombinationIsOdd = int(input())%2 == 1
secondCombinationIsOdd = int(input())%2 == 1

if(firstCombinationIsOdd and not secondCombinationIsOdd):
    print("no")
else:
    print("yes")
