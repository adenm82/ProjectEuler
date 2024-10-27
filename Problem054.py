def high(x):
    nums="123456789TJQKA"
    high=0
    for y in x:
        high=max(high,nums.find(y))
    return high
def pair(x):
    arr=[]
    nums="23456789TJQKA"
    for y in range(len(x)):
        if y%3==0:
            if x[y] in arr:
                return nums.find(x[y])
            arr.append(x[y])
    return -1
def twopair(x):
    arr=[]
    pair=-1
    nums="23456789TJQKA"
    for y in range(len(x)):
        if y%3==0:
            if x[y] in arr:
                if pair>-1:
                    return max(pair,nums.find(x[y]))
                else:
                    pair=nums.find(x[y])
            arr.append(x[y])
    return -1
def three(x):
    dict={}
    nums="23456789TJQKA"
    for y in range(len(x)):
        if y%3==0:
            if x[y] in dict:
                dict[x[y]]+=1
                if dict[x[y]]==3:
                    return nums.find(x[y])
            else:
                dict[x[y]]=1
    return -1
def four(x):
    dict={}
    for y in range(len(x)):
        if y%3==0:
            if x[y] in dict:
                dict[x[y]]+=1
                if dict[x[y]]==4:
                    return int(x[y])
            else:
                dict[x[y]]=1
    return -1
def flush(x):
    arr=[]
    for y in range(len(x)):
        if y%3==1:
            arr.append(x[y])
    if len(set(arr))==1:
        return high(x)
    return -1
def straight(x):
    arr=[]
    nums="23456789TJQKA"
    for y in range(len(x)):
        if y%3==0:
            arr.append(nums.find(x[y]))
    arr.sort()
    if len(set(arr))==5 and arr[-1]-arr[0]==4:
        return high(x)
    return -1
def fullhouse(x):
    dict={}
    for y in range(len(x)):
        if y%3==0:
            if x[y] in dict:
                dict[x[y]]+=1
            else:
                dict[x[y]]=1
    if 3 in dict.values() and 2 in dict.values():
        return three(x)
    return -1
def straightflush(x):
    if straight(x)>-1 and flush(x)>-1:
        return high(x)
    return -1
def royalflush(x):
    if straightflush(x)>-1 and "T" in x and "A" in x:
        return high(x)
    return -1
def highthree(x):
    dict={}
    arr=[]
    nums="23456789TJQKA"
    for y in range(len(x)):
        if y%3==0:
            arr.append(nums.find(x[y]))
            if x[y] in dict:
                dict[x[y]]+=1
            else:
                dict[x[y]]=1
    most=0
    for x in arr:
        if dict[x]<3:
            most=max(most,x)
    return most
def hightwo(x):
    dict={}
    arr=[]
    nums="23456789TJQKA"
    for y in range(len(x)):
        if y%3==0:
            arr.append(int(nums.find(x[y])))
            if x[y] in dict:
                dict[int(nums.find(x[y]))]+=1
            else:
                dict[int(nums.find(x[y]))]=1
    most=0
    for z in arr:
        if dict[z]<2:
            most=max(most,z)
    return most
def winner(x,y):
    print()
    print(x)
    print(y)
    if royalflush(x)>-1:
        p1val=9
        print("Royal Flush")
    elif straightflush(x)>-1:
        p1val=8
        print("Straight Flush")
    elif four(x)>-1:
        p1val=7
        print("Four of a Kind")
    elif fullhouse(x)>-1:
        p1val=6
        print("Full House")
    elif flush(x)>-1:
        p1val=5
        print("Flush")
    elif straight(x)>-1:
        p1val=4
        print("Straight")
    elif three(x)>-1:
        p1val=3
        print("Three of a Kind")
    elif twopair(x)>-1:
        p1val=2
        print("Two Pair")
    elif pair(x)>-1:
        p1val=1
        print("Pair")
    else:
        p1val=0
        print("High Card")
    if royalflush(y)>-1:
        p2val=9
        print("Royal Flush")
    elif straightflush(y)>-1:
        p2val=8
        print("Straight Flush")
    elif four(y)>-1:
        p2val=7
        print("Four of a Kind")
    elif fullhouse(y)>-1:
        p2val=6
        print("Full House")
    elif flush(y)>-1:
        p2val=5
        print("Flush")
    elif straight(y)>-1:
        p2val=4
        print("Straight")
    elif three(y)>-1:
        p2val=3
        print("Three of a Kind")
    elif twopair(y)>-1:
        p2val=2
        print("Two Pair")
    elif pair(y)>-1:
        p2val=1
        print("Pair")
    else:
        p2val=0
        print("High Card")
    if p1val>p2val:
        print("Player 1")
        return 1
    elif p2val>p1val:
        print("Player 2")
        return 2
    else:
        if p1val==6:
            if fullhouse(x)>fullhouse(y):
                return 1
            elif fullhouse(y)>fullhouse(x):
                return 2
            else:
                if high(x)>high(y):
                    return 1
                else:
                    return 2
        elif p1val==3:
            if three(x)>three(y):
                return 1
            elif three(x)<three(y):
                return 2
            else:
                if highthree(x)>highthree(y):
                    return 1
                else:
                    return 2
        elif p1val==2:
            if twopair(x)>twopair(y):
                return 1
            elif twopair(x)<twopair(y):
                return 2
            else:
                if hightwo(x)>hightwo(y):
                    return 1
                else:
                    return 2
        elif p1val==1:
            if pair(x)>pair(y):
                return 1
            elif pair(x)<pair(y):
                return 2
            else:
                if hightwo(x)>hightwo(y):
                    return 1
                else:
                    return 2
        else:
            if high(x)>high(y):
                return 1
            else:
                return 2
file=open("0054_poker.txt","r")
data=list(file)
data[0]=data[0][:-1]
p1=[]
p2=[]
p1best=0
p2best=0
for x in data:
    p1.append(x[:14])
    p2.append(x[15:-1])
count=0
count2=0
for x in range(len(data)):
    if winner(p1[x],p2[x])==1:
        count+=1
    else:
        count2+=1
print(count)
print(count2)
