num=20
while True:
    count=0
    for x in range(1,21):
        if num%x==0:
            count+=1
        else:
            break
    if count==20:
        print(num)
        break
    num+=20
