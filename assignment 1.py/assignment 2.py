information = input("Enter the input ")

try:
    int(information)
    it_is = True
except ValueError:
    it_is = False

if it_is == True:
    print("information is integer")
elif it_is == False:
    print("information is string")
