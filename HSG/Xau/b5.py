s = input()

k = s.split()
ans = ''
mxn = 0
for i in k:
    if(mxn < len(i)):
        mxn = len(i)
        ans = i
print(ans)
