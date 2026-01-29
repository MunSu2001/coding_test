N = int(input())
A = map(int, input().split())
v = int(input())
a = 0
for x in A:
    if x == v:
        a+= 1
print(a)