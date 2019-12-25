n=int(input())
k=bin(n)
k=k[2:]
print(k.count('1'),k.count('0'))
