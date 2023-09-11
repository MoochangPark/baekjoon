def solution(elements):
    answer = 0
    count = set()
    for i in range(1,len(elements)):
        for j in range(len(elements)):
            a = elements[j:j+i]
            b = a + elements[:i - len(a)]
            
            count.add(sum(b))
    count.add(sum(elements))
    answer = len(count)
    return answer