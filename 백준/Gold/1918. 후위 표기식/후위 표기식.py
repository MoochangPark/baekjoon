l = list(input())
st = []
alpha = ''
for ll in l:
    if ll.isalpha():
        alpha += ll
    else:
        if ll == '(':
            st.append(ll)
        elif ll == '*' or ll == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                alpha += st.pop()
            st.append(ll)
        elif ll == '+' or ll == '-':
            while st and st[-1] != '(':
                alpha += st.pop()
            st.append(ll)
        elif ll == ')':
            while st and st[-1] != '(':
                alpha += st.pop()
            st.pop()
while st:
    alpha += st.pop()
print(alpha)