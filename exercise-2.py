number = int(input())
limits = [1,5,10,20,50,100,250,500,1000]
words = ["few","several","pack","lots","horde","throng","swarm", "zounds", "legion"]
traduction = "few"
for index, limit in enumerate(limits):
    if(number >= limit):
        traduction = words[index]
print(traduction)
