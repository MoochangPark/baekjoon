def solution(k, dungeons):
    answer = 0
    
    def dfs(count, l, now):
        nonlocal answer
        
        for d in dungeons:
            if d not in l and now >= d[0]:
                dfs(count + 1, l + [d], now - d[1])
        
        answer = max(answer, count)
            
    for d in dungeons:
        if k >= d[0]:
            dfs(1,[d], k - d[1])
    
    return answer