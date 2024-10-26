letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("0022_names.txt","r") as file:
    data=file.read()
arr=data.split(",")
arr=[x[1:-1] for x in arr]
arr.sort()
sum=0
for i,x in enumerate(arr):
    score=0
    for y in x:
        score+=letters.index(y)+1
    score*=(i+1)
    sum+=score
print(sum)
