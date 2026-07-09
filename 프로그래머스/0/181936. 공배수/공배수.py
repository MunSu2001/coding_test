def solution(number, n, m):
    answer = 0
    if number % n == 0:
        if number % m == 0:
            answer = 1
        else:
            anwer = 0
    else:
        answer = 0
    return answer