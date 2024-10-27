def reduce(n,d):
    notReduced=True
    while notReduced:
        notReduced=False
        for x in range(2,n+1):
            if n%x==0 and d%x==0:
                notReduced=True
                n//=x
                d//=x
    return d
def cancel(n,d):
    frac=n/d
    if n%10==0 or d%10==0:
        return False
    ns=str(n)
    ds=str(d)
    if ns[0] in ds:
        if ds[0]==ns[0]:
            return frac==(int(ns[1]))/(int(ds[1]))
        else:
            return frac==(int(ns[1]))/(int(ds[0]))
    if ns[1] in ds:
        if ds[1]==ns[1]:
            return frac==(int(ns[0]))/(int(ds[0]))
        else:
            return frac==(int(ns[0]))/(int(ds[1]))
    return False
nprod=1
dprod=1    
for n in range(10,100):
    for d in range(n+1,100):
        if cancel(n,d):
            nprod*=n
            dprod*=d
print(reduce(nprod,dprod))
