def solution(want, number, discount):
    answer = 0
    
    l = len(discount)
    
    for c in range(10):
        if discount[c] in want:
            number[want.index(discount[c])] -= 1
    
    if [0]*len(number) == number:
        answer += 1
    
    t = 10
    while t < l:
        if discount[t-10] in want:
            number[want.index(discount[t - 10])] += 1
        if discount[t] in want:
            number[want.index(discount[t])] -= 1
        if [0]*len(number) == number:
            answer += 1
        t += 1
    return answer