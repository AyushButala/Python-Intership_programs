import re

emailId = input("Enter Email Id : ")

emailPatter = '[a-z|0-9]*@'

data = re.match(emailPatter,emailId)

if data:
    print("Match")
else:
    print("Not Match")

value = input("Enter Value : ")
searchPattern = '^P....n$'
dataSearch = re.search(searchPattern,value)
print(dataSearch)

dataFind = re.findall(searchPattern,value)
print(dataFind)