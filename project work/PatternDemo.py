print("Pattern 1 : \n")

value = int(input("Enter No. Of Star : "))

for i in range(value):
    for j in range(i+1):
        print("*",end="")
    print("\r")

print("\nPattern 2 :\n")

for i in range(value):
    for j in range(value-i):
        print("*",end="")
    print("\r")

print("\nPattern 3 :\n")

for i in range(value):
    for space in range(value-(i+1)):
        print(" ",end="")

    for j in range(i+1):
        print("*",end="")
    print("\r")

print("\nPattern 4 :\n")

for i in range(value):
    for space in range(i):
        print(" ",end="")

    for j in range(value-i):
        print("*",end="")
    print("\r")

print("\nPattern 5 :\n")

for i in range(value):
    for space in range(value-(i+1)):
        print(" ",end="")

    for j in range((2*i)+1):
        print("*",end="")
    print("\r")

print("\nPattern 6 :\n")

for i in range(value):
    for space in range(i):
        print(" ",end="")

    for j in range((2*(value-i))-1):
        print("*",end="")
    print("\r")