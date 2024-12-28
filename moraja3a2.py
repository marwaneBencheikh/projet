t=[7,98,5,23,5,85]
mx=t[0]
mn=t[0]
for i in range(0,6):
    if t[i]>mx:
        mx=t[i]
    if t[i]<mn:
        mn=t[i]
    if t[i]>10:
        print(t[i])
print(mx, mn)

