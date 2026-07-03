temperary=int(input("Enter a number: "))
number=str(temperary)

reverse=""

while temperary>0:
    rem=temperary%10
    reverse+=str(rem)
    temperary=temperary//10

if reverse==number:
    print("Palindrome")
else:
    print("Not Palindrome")
