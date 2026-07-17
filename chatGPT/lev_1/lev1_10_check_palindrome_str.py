string_by_user=input("Enter string: ")
rev_str=string_by_user[::-1]

if string_by_user==rev_str:
    print("Palindrome")
else:
    print("Not palindrome")