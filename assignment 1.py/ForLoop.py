#values = [1,3,4,6,7,8,9,0]

# for i in range(10):
#     print(i+1)

# for i in range(1,11):
#     print(i)

# for i in range(1,11,3):
#     print(i)

startValue = int(input("Enter Start Value : "))
endValue = int(input("Enter End Value : "))
jumpValue = int(input("Enter Jump Value : "))
# for i in range(endValue):
#     print(i)

# for i in range(startValue,endValue):
#     print(i)

for i in range(startValue,endValue,jumpValue):
    print(i)