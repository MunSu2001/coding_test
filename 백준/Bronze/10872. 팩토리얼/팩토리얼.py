a = int(input())
f = 1
if a > 0:
    for x in range(a):
        f *= x+1
    print(f)
else:
    print('1')