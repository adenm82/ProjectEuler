grid=[]
row=[]
for x in range(21):
    row=[]
    for y in range(21):
        row.append(0)
    grid.append(row)
grid[0][0]=1
for x in range(1,21):
    grid[0][x]=1
for x in range(1,21):
    for y in range(21):
        if y==0:
            grid[x][y]+=grid[x-1][y]
        else:
            grid[x][y]+=grid[x-1][y]+grid[x][y-1]
print(grid[-1][-1])
