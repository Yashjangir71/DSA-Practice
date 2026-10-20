s1="abc"
s2="cba"
match=True
if len(s1)!=len(s2):
    match=False
else:
    i=0
    j=len(s2)-1
    while i<len(s1):
        if s1[i]!=s2[j]:
            match=False
            break
        i+=1
        j-=1
print(match)