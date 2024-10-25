arr=[0]*1001
sols=[]
for x in range(1,1000):
    for y in range(1,1000):
        z=(x**2+y**2)**0.5
        if z==int(z):
            if [y,x] not in sols and x+y+z<=1000:
                sols.append([x,y])
                arr[x+y+int(z)]+=1
                if x+y+z==120:
                    print(x,y,z)
most=0
m=0
for x in range(len(arr)):
    if arr[x]>most:
        most=arr[x]
        m=x
print(most)
print(m)
