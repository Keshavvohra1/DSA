#find max no of consecutive 1s in an array
nums=[1,1,0,1,1,1,1,0]

count=0
max_count=0
for i in range(len(nums)):
    if nums[i]==0:
        count=0
    elif nums[i]==1:
        count+=1
        max_count=max(max_count,count)
        
    
print(max_count)