a=[1,2,3,4]
def runningsum(nums):
    x=[]
    for i in range(0,len(nums)):
        total=0
        for j in range(0,i+1):
            total=total+nums[j]
        x.append(total)
    return x
print(runningsum(a))