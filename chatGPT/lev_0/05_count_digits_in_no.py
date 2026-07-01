# print("Number of digits in the number:", len(str(num)))

num=int(input("Enter a number: "))
i=0
while num>0:
    num=num//10
    i+=1
print(i)