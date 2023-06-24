s = list(input())
t = [0] * 26

for i in s:
  t[ord(i) - ord('A')] += 1

holcnt = 0
hol = ''
jjak = ''
for i in range(26):
  if t[i] != 0:
    if t[i] % 2 == 1:
      holcnt += 1
      hol += chr(i+65)
    jjak += chr(i+65) * (t[i] // 2)
  
if holcnt > 1:
  print("I'm Sorry Hansoo")
else:
  print(jjak + hol + jjak[::-1])