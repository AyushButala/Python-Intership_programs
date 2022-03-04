class First():
    def FirstMethod(self):
        message = input("Enter Message : ")
        print(message)

class Second(First):
    def SecondMethod(self,rollNo,name):
        print(f"Roll No = {rollNo} & Student Name = {name}")

class Third(Second):
    def ThirdMethod(self):
        print("Third Method")

class Four(Third):
    def FourthMethod(self):
        super().FirstMethod()
        print("Fourth Method")

# s = Second
# s.SecondMethod()
# s.FirstMethod()

# third = Third
# third.ThirdMethod()

# studentRoll = int(input("Enter Roll No : "))
# studentName = input("Enter Student Name : ")

# third.SecondMethod(studentRoll,studentName)
# third.FirstMethod()

f = Four()
f.FourthMethod()
f.ThirdMethod()

studentRoll = int(input("Enter Roll No : "))
studentName = input("Enter Student Name : ")

f.SecondMethod(studentRoll,studentName)
f.FirstMethod()