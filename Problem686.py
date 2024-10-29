#1 minute, kinda slow
def p(l,n):
    j=6
    count=0
    length=len(str(l))
    power=64
    while count<n:
        power*=2
        j+=1
        power=int(str(power)[:length+30])
        seg=int(str(power)[:length])
        if seg==l:
            count+=1
            print(count)
    return j
print(p(123,678910))
