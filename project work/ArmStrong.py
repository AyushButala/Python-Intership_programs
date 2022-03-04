armNumber = input("Enter Number : ")

sum = 0
for i in armNumber:
    num = int(i)**3
    sum = sum+num

#print(sum)
if int(armNumber)==sum:
    print("Armstrong Number")
else:
    print("Invalid")