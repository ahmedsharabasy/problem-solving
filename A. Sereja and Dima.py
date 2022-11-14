
x=int(input())

nums= list(map(int,input().split()))

sereja=0
dima=0

for i in nums:
    if len(nums)==1:
        sereja+=nums[0]    
    if nums[0]>nums[-1]:
        sereja+=nums[0]
        nums.remove(nums[0])
    else:
        sereja+=nums[-1]
        nums.remove(nums[-1])       
    if nums[0]>nums[-1]:
        dima+=nums[0]
        nums.remove(nums[0])
    else:
        dima+=nums[-1]
        nums.remove(nums[-1])

print(sereja , dima)            


