n,k = list(map(int, (input().split())))
if 2*n<=k:
    print(2)
elif (2*n%k>=1):
    print(int(2*n/k)+1)
else:
    print(int(2*n/k))
