def solution(n, k):
    answer = 0
    t = ''
    while n >= k:
        t += str(n % k)
        n //= k
    t += str(n)
    t = t[::-1]
    t = t.split('0')
    
    for tt in t:
        if len(tt) == 0 or tt == '1' or tt == '0':
            continue
        s = True
        
        for i in range(2,int(int(tt)**0.5)+1):  
            if int(tt) % i == 0:
                s = False
                break
        if s:
            answer += 1
            
    return answer