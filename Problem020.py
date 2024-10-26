def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
num=factorial(100)
sum=0
for x in str(num):
    sum+=int(x)
print(sum)
