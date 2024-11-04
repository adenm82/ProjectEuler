from operator import itemgetter
def distance(x1, y1, x2, y2):
    xdist = abs(x2 - x1)
    ydist = abs(y2 - y1)
    return (xdist**2 + ydist**2) ** 0.5
s = [290797]
for x in range(4_000_000):
    s.append((s[-1] ** 2) % 50515093)
coords = [[s[2 * x], s[2 * x + 1]] for x in range(2_000_000)]
coords = sorted(coords, key=itemgetter(0))
minDist = float("inf")
for x in range(2_000_000):
    y=x+1
    while y<2_000_000 and abs(coords[y][0]-coords[x][0])<minDist and abs(coords[y][1]-coords[x][1])<minDist:
        x1 = coords[x][0]
        y1 = coords[x][1]
        x2 = coords[y][0]
        y2 = coords[y][1]
        if abs(x1 - x2) < minDist and abs(y1 - y2) < minDist:
            dist = distance(x1, y1, x2, y2)
            minDist = min(minDist, dist)
        y+=1
print(minDist)
