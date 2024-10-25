grid=[]
row=[]
for x in range(1001):
    row=[]
    for y in range(11001):
        row.append(0)
    grid.append(row)
row=500
col=500
grid[row][col]=1
num=2
dir=0
count=1
times=0
counts=0
while num<=1001*1001:
    if dir==0:
        col+=1
        grid[row][col]=num
    elif dir==1:
        row+=1
        grid[row][col]=num
    elif dir==2:
        col-=1
        grid[row][col]=num
    else:
        row-=1
        grid[row][col]=num
    times+=1
    if times==count:
        dir=(dir+1)%4
        counts+=1
        if counts==2:
            counts=0
            count+=1
        times=0
    num+=1
sum=0
for x in range(1001):
    sum+=grid[x][x]
    sum+=grid[x][1001-x-1]
sum-=grid[500][500]
print(sum)
