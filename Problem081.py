file=open("0081_matrix.txt","r")
data=file.read()
arr=[]
data=data.split(",")
data=data[:-1]
for x in range(len(data)):
    if "\n" in data[x]:
        dub=data[x].split("\n")
        arr.append(int(dub[0]))
        arr.append(int(dub[1]))
    else:
        arr.append(int(data[x]))
grid=[]
temp=[]
count=1
arr.append(7981)
for x in arr:
    temp.append(x)
    if count==80:
        count=0
        grid.append(temp)
        temp=[]
    count+=1
for x in range(1,80):
    grid[0][x]+=grid[0][x-1]
for x in range(len(grid)):
    if x>0:
        for y in range(len(grid[x])):
            if y==0:
                grid[x][y]+=grid[x-1][y]
            else:
                grid[x][y]+=min(grid[x][y-1],grid[x-1][y])
print(grid[-1][-1])
