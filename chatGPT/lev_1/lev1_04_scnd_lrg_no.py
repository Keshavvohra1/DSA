arr=[2,6,5,4,7]
big=second_big=float("-inf")

for i in arr:
    if big<i:
        second_big=big
        big=i
    elif big>i and second_big<i:
        second_big=i
print(f"2nd Biggest:{second_big} \nBiggest:{big}")