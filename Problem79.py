def allIn(num,arr):
    for x in arr:
        chars=[a for a in str(x)]
        if str(num).find(chars[0])==-1:
            return False
        for y in range(1,3):
            if chars[y] not in str(num):
                return False
            else:
                if str(num).find(chars[y])<str(num).find(chars[y-1]):
                    return False
    return True
with open("0079_keylog.txt","r") as file:
    data=file.read()
arr=data.split()
num=1
poss=123456
a=[135,247]
while not allIn(num,arr):
    num+=1
print(num)
