def solution(numbers):
    answer = [0] * len(numbers)
    l = []
    for i in range(len(numbers)):
        if len(l) == 0:
            l.append([i,numbers[i]])
        else:
            while len(l) and l[-1][1] < numbers[i]:
                t = l.pop()
                answer[t[0]] = numbers[i]
            
            l.append([i,numbers[i]])
            
    for t in l:
        answer[t[0]] = -1
    
    return answer