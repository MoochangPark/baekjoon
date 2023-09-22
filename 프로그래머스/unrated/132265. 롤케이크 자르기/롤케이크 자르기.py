from collections import Counter

def solution(topping):
    answer = 0
    
    l = {}
    r = {}
    for t in topping:
        if t not in r:
            r[t] = 1
        else:
            r[t] += 1
    
    for i in range(len(topping)):
        a = topping[i]
        if a not in l:
            l[a] = 1
        else:
            l[a] += 1
        r[a] -=1
        if r[a] == 0:
            del r[a]
        if len(l) == len(r):
            answer += 1
    
    
    
    return answer