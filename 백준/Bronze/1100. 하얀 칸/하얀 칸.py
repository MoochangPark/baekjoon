l = [list(input()) for _ in range(8)]
answer = 0
for i in range(len(l)):
  for j in range(len(l[i])):
    if i % 2 == 0:
      if j % 2 == 0:
        if l[i][j] == 'F':
          answer += 1
    else:
      if j % 2 != 0:
        if l[i][j] == 'F':
          answer += 1
print(answer)