arr=[4, 5, 1, 2, 3]

for i in range(1,len(arr)):
    if(arr[i-1]>arr[i]):
       print(False)
       break
else:
     print(True)