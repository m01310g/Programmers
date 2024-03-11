def solution(number, limit, power):
    answer = 0
    div = [1]
    for i in range(2, number + 1):
        cnt = 0
        for j in range(1, int(i**(1/2) + 1)):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1
        if cnt > limit:
            cnt = power
            div.append(cnt)
        else:
            div.append(cnt)
    answer = sum(div)
    return answer