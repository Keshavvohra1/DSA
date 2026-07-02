num=int(input("Enter a number: "))
# 1234
rev_num=""
while num>0:
    a=num%10
    rev_num+=str(a)
    num=num//10

print(rev_num)

