import math
def solution(fees, records):
    answer = []
    
    max_time = 23 * 60 + 59
    
    d = {}
    aw = {}
    for r in records:
        t = r.split(" ")

        if t[2] == "OUT":
            tmp = d[t[1]]
            tmp = int(tmp[0:2]) * 60 + int(tmp[3:])
            now = int(t[0][0:2]) * 60 + int(t[0][3:])
            dex = now - tmp
            if t[1] not in aw:
                aw[t[1]] = 0
            aw[t[1]] += dex
            del d[t[1]]
        else:
            d[t[1]] = t[0]
    for i,j in d.items():
        tmp = int(j[0:2]) * 60 + int(j[3:])
        if i not in aw:
            aw[i] = 0
        aw[i] += max_time - tmp
    lis = []
    for i,j in aw.items():
        if j < fees[0]:
            lis.append([i,fees[1]])
        else:
            lis.append([i,fees[1] + math.ceil((j-fees[0])/fees[2]) * fees[3]])
    lis.sort(key=lambda x : x[0])
    answer = [i[1] for i in lis]
    
    return answer