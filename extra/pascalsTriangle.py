def solution(n):
    
    i = 0
    while len(n) > 2:
        n[i] = (n[i] + n[i + 1]) % 10
        i += 1

        if i == len(n) - 1:
            n.pop()
            i = 0

    return "".join(n)

solution([4,5,6,7])