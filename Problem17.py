def letters(x,dict):
    hundreds=x//100
    tens=x%100//10*10
    ones=x%100%10
    if x==1000:
        return len(dict[1000])
    elif x%100==0:
        return len(dict[hundreds])+len("Hundred")
    elif x<20:
        return len(dict[x])
    elif x<100:
        if x%10==0:
            return len(dict[tens])
        else:
            return len(dict[tens])+len(dict[ones])
    else:
        if x%100>20:
            return len(dict[hundreds])+len("hundredand")+len(dict[tens])+len(dict[ones])
        else:
            return len(dict[hundreds])+len("hundredand")+len(dict[x%100])
dict={}
dict[1000]="OneThousand"
dict[0]=""
dict[1]="One"
dict[2]="Two"
dict[3]="Three"
dict[4]="Four"
dict[5]="Five"
dict[6]="Six"
dict[7]="Seven"
dict[8]="Eight"
dict[9]="Nine"
dict[10]="Ten"
dict[11]="Eleven"
dict[12]="Twelve"
dict[13]="Thirteen"
dict[14]="Fourteen"
dict[15]="Fifteen"
dict[16]="Sixteen"
dict[17]="Seventeen"
dict[18]="Eighteen"
dict[19]="Nineteen"
dict[20]="Twenty"
dict[30]="Thirty"
dict[40]="Forty"
dict[50]="Fifty"
dict[60]="Sixty"
dict[70]="Seventy"
dict[80]="Eighty"
dict[90]="Ninety"
count=0
for x in range(1,1001):
    count+=letters(x,dict)
    print(x, letters(x,dict))
print(count)
