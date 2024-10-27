res,sol=[],[]
nums=[0,1,2,3,4,5,6,7,8,9]
def backtrack(nums):
    if len(sol)==10:
        res.append(sol[:])
    else:
        if len(res)>1_000_000:
            return
        n=nums[:]
        for x in n:
            sol.append(x)
            nums.remove(x)
            backtrack(nums)
            sol.pop()
            nums.append(x)
            nums.sort()
backtrack(nums)
print(res[-1])
