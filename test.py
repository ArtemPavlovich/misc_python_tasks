n = int(input())
a = input().split()
b = sorted(a)
res = 0

for i in range(1, n):
    if b[i] == b[i-1]:
        res = res + 1

print (res)
