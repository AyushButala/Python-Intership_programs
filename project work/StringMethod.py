message = "#hello_everyone good afternoon#"

print(message.capitalize())
print(message.title())
upperChar = message.upper()
print(upperChar)
print(upperChar.lower())

value = input("Enter Message : ")

if value.isnumeric():
    print("Number Value")
else:
    #print("Character")
    if value.upper()=="YES":
        print("Yes")
    else:
        print("No")

#print(message.split('_'))
splitValue = message.split('_')
for i in splitValue:
    print(i)

print(splitValue[1].split())

print(message.strip('#'))

print(message.rstrip('#'))
print(message.lstrip('#'))

print(message.replace('afternoon','night'))