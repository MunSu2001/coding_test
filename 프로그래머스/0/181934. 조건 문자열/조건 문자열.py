def solution(ineq, eq, n, m):
    answer = 0
    a = ineq + eq
    if a == ">=":
        return 1 if n >= m else 0
    elif a == "<=":
        return 1 if n <= m else 0
    elif a == "<!":
        return 1 if n < m else 0
    else:
        return 1 if n > m else 0
        
    return answer