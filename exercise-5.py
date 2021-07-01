cardsAndMinutes = input().split(" ")
carsArrivedByMinute = input().split(" ")

k, n = [int(element) for element in cardsAndMinutes]
carsByMinute = [int(car) for car in carsArrivedByMinute]
carsInQueue = 0

for i, cars in enumerate(carsByMinute):
    if(i >= n):
        break
    if (carsInQueue + cars - k) > 0:
        carsInQueue = carsInQueue + cars - k
    else:
        carsInQueue = 0
print(carsInQueue)
