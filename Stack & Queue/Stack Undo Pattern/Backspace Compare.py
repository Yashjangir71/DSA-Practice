s1="ab#c"
s2="ad#c"
stack1=[]
stack2=[]
for i in s1:
    if i=="#":
        stack1.pop()
    else:
        stack1.append(i)

for i in s2:
    if i=="#":
        stack2.pop()
    else:
        stack2.append(i)

print(stack1 == stack2)