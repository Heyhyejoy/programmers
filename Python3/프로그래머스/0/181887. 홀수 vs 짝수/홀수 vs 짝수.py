def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    n = 0
    for i in num_list:
        n += 1
        if n % 2 == 0:
            even += i
        else:
            odd += i
    
    if odd > even: 
        answer += odd
    elif odd < even: 
        answer += even
    else:
        answer += even
    return answer