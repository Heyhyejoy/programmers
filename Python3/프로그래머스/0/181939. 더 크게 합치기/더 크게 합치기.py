def solution(a, b):
    answer_1 = str(a)+str(b)
    answer_2 = str(b)+str(a)
    
    if answer_1 > answer_2:
        return int(answer_1)
    else:
        return int(answer_2)