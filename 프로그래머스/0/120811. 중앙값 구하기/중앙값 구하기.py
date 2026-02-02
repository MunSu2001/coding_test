def solution(array):
    answer = 0
    a = sorted(array)
    n = len(a) // 2
    answer = a[n]
    return answer