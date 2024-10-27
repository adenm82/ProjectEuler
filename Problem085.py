def rects(x,y):
    count=0
    for a in range(1,x+1):
        for b in range(1,y+1):
            count+=(x-a+1)*(y-b+1)
    return count
diff=0
least=float('inf')
for x in range(1,100):
    for y in range(1,100):
        diff=abs(2000000-rects(x,y))
        if diff<least:
            least=diff
            print(x,y,rects(x,y),x*y)
