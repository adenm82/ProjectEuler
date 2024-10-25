peter=[]
psol=[]
colin=[]
csol=[]
def Pbacktrack(sum):
    if len(psol)==9:
        peter.append(sum)
        return
    else:
        for x in range(1,5):
            psol.append(x)
            sum+=x
            Pbacktrack(sum)
            psol.pop()
            sum-=x
Pbacktrack(0)
def Cbacktrack(sum):
    if len(csol)==6:
        colin.append(sum)
        return
    else:
        for x in range(1,7):
            csol.append(x)
            sum+=x
            Cbacktrack(sum)
            csol.pop()
            sum-=x
Cbacktrack(0)
dict={}
for x in peter:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
s=set(peter)
totalRolls=0
peterWins=0
for x in list(s):
    for y in colin:
        if x>y:
            peterWins+=dict[x]
        totalRolls+=dict[x]
print(peterWins/totalRolls)
