array=[3, 7, 2, 9, 4]

big_num=array[0]
small_num=array[0]

for i in range(1,len(array)):
    if array[i]>big_num:
        big_num=array[i]
    if array[i]<small_num:
        small_num=array[i]

print(f"Biggest No: {big_num}\nSmallest No: {small_num}")
