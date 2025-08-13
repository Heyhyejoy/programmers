def solution(num_list):
    add = 0
    mul = 1
    
    for i in num_list:
        
        add += i
        mul = mul * i 
        
    add = add ** 2
    print(add)
    print(mul)
    
    if mul > (add):
        return 0
    else:
        return 1