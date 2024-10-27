from collections import Counter
def permuted(x):
    s=str(x)
    c=Counter(s)
    for y in range(2,7):
        if Counter(str(x*y))!=c:
            return False
    return True
x=1
while not permuted(x):
    x+=1
print(x)
