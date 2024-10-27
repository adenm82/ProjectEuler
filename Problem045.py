n=2
pents=set()
hexes=set()
tri=0
while tri not in pents or tri not in hexes or tri==40755:
    tri=n*(n+1)//2
    pents.add(n*(3*n-1)//2)
    hexes.add(n*(2*n-1))
    n+=1
print(tri)
