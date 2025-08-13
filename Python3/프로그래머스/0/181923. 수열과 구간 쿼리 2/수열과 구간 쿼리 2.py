def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        list = []
        for i in arr[s:e+1]:
            if i > k:
                list.append(i)
        answer.append(-1 if not list else min(list))
    return answer
                
                
