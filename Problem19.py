day=1
month=0
days=[31,28,31,30,31,30,31,31,30,31,30,31]
year=1900
dotw=0
suns=0
while year<=2000:
    print(year)
    if day==1 and dotw==0 and year>1900:
        suns+=1
        print(year,month+1,day)
    if year%4==0 and month==1 and day==28:
        day=29
        dotw=(dotw+1)%7
    elif day>=days[month]:
        day=1
        month+=1
        dotw=(dotw+1)%7
        if month==12:
            month=0
            year+=1
    else:
        day+=1
        dotw=(dotw+1)%7
print(suns)
