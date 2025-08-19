def solution(my_string, index_list):
    answer = []
    word = ''
    for i in index_list:
        letter = my_string[i]
        word += letter
        answer = "".join(word)
    
    return answer