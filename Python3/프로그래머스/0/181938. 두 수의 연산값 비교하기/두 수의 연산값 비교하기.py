def solution(a, b):
    answer_1 = str(a) + str(b)
    answer_2 = ((2 * a)  * b)
    answer_1a = int(answer_1)

    if answer_1a > answer_2:
        return int(answer_1a)
    else:
        return int(answer_2)
        