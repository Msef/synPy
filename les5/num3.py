x = int(input())
a = int(input())
b = int(input())

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
else:
    print(0 if a + b < x else 1)
