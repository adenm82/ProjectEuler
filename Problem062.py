#4 minutes, very slow
import time
from collections import Counter
def isPerm(n1,n2):
    return Counter(str(n1))==Counter(str(n2))
start=time.time()
cubes=set()
for x in range(1,10000):
    cubes.add(x**3)
cubs=list(cubes)
cubs.sort()
for i,x in enumerate(cubs):
    print(i)
    numCubes=0
    for y in cubs:
        if isPerm(x,y):
            numCubes+=1
    if numCubes==5:
        print(x)
        break
print("Done")
print(time.time()-start,"seconds")
