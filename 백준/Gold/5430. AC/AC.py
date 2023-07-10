t = int(input())

for _ in range(t):
  cmd = input()
  
  n = int(input())
  
  l = input().strip('[]').split(',')
  
  c = 1
  r = False
  for i in cmd:
    if i == 'R':
      if r:
        r = False
      else:
        r = True
    else:
      if n:
        if r:
          l.pop(-1)
        else:
          l.pop(0)
        n -= 1
      else:
        c = 0
        print('error')
        break
  if c:
    if r:
      print('[' + ','.join(l[::-1]) + ']')
    else:
      print('[' + ','.join(l) + ']')