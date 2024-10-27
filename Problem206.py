def concealed(x):
    s=str(x)
    if len(s)!=19:
        return False
    nums=['1','2','3','4','5','6','7','8','9','0']
    for x in range(0,len(s),2):
        if s[x]!=nums[x//2]:
            return False
    return True
x=10
while not concealed(x**2):
    x+=10
print(x)
