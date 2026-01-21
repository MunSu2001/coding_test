def solution(num_list):
    a = []
    b = []
    answer = 0
    for n in num_list:
        if n % 2 == 0:
            a.append(n)
        else:
            b.append(n)
    a = "".join(map(str, a))
    b = "".join(map(str, b))
    answer = int(a) + int(b)
    return answer