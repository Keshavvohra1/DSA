arr=[2,6,5,4,7,3,2]
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)