#Pretty slow
count=0
dict={}
for d in range(2,12001):
    for n in range(int((1/3)*d),d//2+1):
        if n not in dict or d not in dict[n]:
            if n/d<0.5 and n/d>1/3:
                count+=1
            x=2
            while d*x<=12000:
                if n*x not in dict:
                    dict[n*x]=[d*x]
                else:
                    dict[n*x].append(d*x)
                x+=1
print(count)
