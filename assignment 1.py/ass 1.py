N = int(input("enter number:"))
print(N)
print("the reversed numbers are:", end="")
for num in range(N, -1, -1):
    print(num, end="   ")
