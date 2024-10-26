with open("0013_numbers.txt","r") as file:
    data=file.read()
arr=data.split("\n")
arr=[int(x) for x in arr]
sum=0
for x in arr:
    sum+=x
print(str(sum)[:10])
