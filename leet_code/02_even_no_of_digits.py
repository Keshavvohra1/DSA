nums = [555,901,482,1771]

count=0
for num in nums:
        string=str(num)
        if len(string)%2==0:
                count+=1

print(count)