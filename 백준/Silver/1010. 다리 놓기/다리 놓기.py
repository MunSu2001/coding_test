import sys
input = sys.stdin.readline

T = int(input().strip())

MAX = 30
C = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for n in range(MAX + 1):
    C[n][0] = 1
    C[n][n] = 1
    for k in range(1, n):
        C[n][k] = C[n-1][k-1] + C[n-1][k]

for _ in range(T):
    N, M = map(int, input().split())
    print(C[M][N])
