arr=[1,2,4,5]
n=len(arr)+1
sum_s=(n*(n+1))/2
summ=0
for i in range(len(arr)):
    summ+=arr[i]

print(sum_s-summ)