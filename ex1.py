m=[[1,2,3],[4,5,6,],[7,8,9]]
rm=[[None,None,None],[None,None,None],[None,None,None]]

for i in range(0,3):
    for j in range(0,3):
        rm[i][j]=m[j][i]
print(rm)

    


