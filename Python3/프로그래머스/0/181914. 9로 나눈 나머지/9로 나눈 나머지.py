def solution(number):
    answer = 0
    for str in number :
        answer += int(str)
    return answer%9