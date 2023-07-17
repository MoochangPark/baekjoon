now_channel = 100
want_channel = int(input())
broken_button = int(input())
button_list = []
if broken_button:
    button_list = list(input().split())

mins = abs(now_channel - want_channel)

for i in range(1000001):
    ok = True
    for j in str(i):
        if j in button_list:
            ok = False
            break
    if ok:
        mins = min(mins, len(str(i)) + abs(i - want_channel))
        
print(mins)