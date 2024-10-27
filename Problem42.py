with open("0042_words.txt","r") as file:
    data=file.read()
arr=data.split(",")
arr=[x[1:-1] for x in arr]
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tris=set()
for n in range(1,20):
    tris.add(n*(n+1)//2)
words=0
for x in arr:
    score=0
    for y in x:
        score+=letters.index(y)+1
    if score in tris:
        words+=1
print(words)
