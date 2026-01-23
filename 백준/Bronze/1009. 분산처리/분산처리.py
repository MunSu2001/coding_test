n = int(input())
T = []

for _ in range(n):
    a, b = map(int, input().split())

    last = pow(a, b, 10)   
    if last == 0:
        last = 10          
    T.append(last)
print(*T, sep='\n')