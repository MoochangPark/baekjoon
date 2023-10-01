d = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
answer = 0
a = d.index(input()) * 10
b = d.index(input())
answer = a+b
c = d.index(input())
for _ in range(c):
    answer *= 10

print(answer)