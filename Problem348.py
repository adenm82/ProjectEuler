def isPal(x):
    return str(x)==str(x)[::-1]
squares=[]
cubes=[]
for x in range(2,50_000):
    squares.append(x**2)
    if x<1000:
        cubes.append(x**3)
dict={}
arr=[]
for x in squares:
    for y in cubes:
        if isPal(x+y):
            if x+y in dict:
                dict[x+y]+=1
            else:
                dict[x+y]=1
            if dict[x+y]==4:
                arr.append(x+y)
                print(x+y)
arr=arr[:5]
print(arr[0]+arr[1]+arr[2]+arr[3]+arr[4])
