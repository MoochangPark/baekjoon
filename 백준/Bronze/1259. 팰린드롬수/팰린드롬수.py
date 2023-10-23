while True:
  a = input()
  
  if a == '0':
    break
    
  left = 0
  right = len(a)-1
  check = True
  
  while left <= right:
    if a[left] != a[right]:
      check = False
      break
    left += 1
    right -= 1
    
  if check:
    print('yes')
  else:
    print('no')