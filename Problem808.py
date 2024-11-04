def isRPS(x, s):
    return (not isPal(x)) and int(str(x)[::-1]) in s
def isPal(x):
    return str(x) == str(x)[::-1]
def sieve(num):
    prime = [True for i in range(num + 1)]
    dict = {}
    p = 2
    while p * p <= num:
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
                dict[i] = 0
        p += 1
    return dict
num = 40_000_000
dict = sieve(num)
squares = [x**2 for x in range(2, num) if x not in dict]
s = set(squares)
rps=[x for x in squares if isRPS(x,s)]
print(sum(rps[:50]))
