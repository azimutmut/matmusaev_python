arr = list(map(int, input("enter the numbers").split()))
a = [x for x in arr if x % 3 == 0]
if a:
    print(a)
else:
    print("There are no multiples of 3 in the array")
