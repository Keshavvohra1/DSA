arr=[1,2,3,4,5,6,7]
even=0
odd=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1

print(f"Even={even} \nOdd={odd}")