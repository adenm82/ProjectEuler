#Took an hour, can't be bothered to find a better solution
def arrSum(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum
def split(x):
    l = len(str(x))
    string = str(x)
    res, sol = [], []
    s = ""
    def backtrack(s):
        if len(s) == l:
            if len(sol) > 1 and arrSum([int(y) for y in sol])==int(x**0.5):
                res.append(sol[:])
                return True
        else:
            ll = len(s)
            s += string[ll]
            sol.append(string[ll])
            backtrack(s)
            sol.pop()

            if sol:
                sol[-1] += string[ll]
                backtrack(s)
                sol[-1] = sol[-1][:-1]

    backtrack("")
    return len(res)>0
num = 10**12
sum = 0
squares = [x**2 for x in range(1, int(num**0.5) + 1)]
for x in squares:
    if split(x):
        sum += x
print(sum)
