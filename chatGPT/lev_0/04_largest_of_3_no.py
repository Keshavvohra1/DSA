

num1,num2,num3=int(input("Enter number1: ")),int(input("Enter number2: ")),int(input("Enter number3: "))

# print(max(num1,num2,num3)) OR

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)