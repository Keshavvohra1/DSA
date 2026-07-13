arr=[1,2,3,4,5]

last=arr[-1] #5
arr2=[]
arr2.append(last)
for i in range(0,len(arr)-1):
    arr2.append(arr[i])

print(arr2)