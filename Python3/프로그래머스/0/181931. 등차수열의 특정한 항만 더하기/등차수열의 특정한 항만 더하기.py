def solution(a, d, included):
    answer = 0
    n = 0
    one = 1
    
    for i in included:
        print(i)
        if i == one:
            answer += a + (d * n) 
            print(answer)
            n += 1
        else:
            n += 1

    return answer