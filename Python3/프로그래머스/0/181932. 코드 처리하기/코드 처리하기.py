def solution(code):
    ret = ''
    one = 1
    zero = 0
    mode = 0
    idx = -1
    
    for i in code:
        idx += 1
        if i != '1' and mode == zero and idx % 2 == 0:
            ret += i
        elif i != '1' and mode == one and idx % 2 == 1:
            ret += i   
        elif i == '1' and mode == zero:
            mode += 1
        elif i == '1' and mode == one:
            mode -= 1
        else:
            pass
            
    if not ret:
        return 'EMPTY'
    return ret