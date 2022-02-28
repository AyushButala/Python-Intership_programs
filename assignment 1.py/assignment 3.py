startvalue = int(input("enter start value:"))
endvalue = int(input("enter end value:"))


if startvalue > endvalue:
    startvalue, endvalue = endvalue, startvalue

    for i in range(startvalue, endvalue):

        print(i)
else:

    for i in range(startvalue, endvalue):

        print(i)
