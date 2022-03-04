class ATM():

    def Balance(self):
        self.amount = 2500
        return self.amount

    def Deposite(self):
        depositeAmount = int(input("Enter Deposite Amount : "))
        self.amount = self.amount+depositeAmount
        return self.amount

    def Withdraw(self):
        withdrawAmount = int(input("Enter Withdraw Amount : "))
        if self.amount>withdrawAmount:
            self.amount = self.amount-withdrawAmount
            return self.amount
        else:
            return "Insufficient Balance"

atm = ATM()

operation = input("Enter Operation (Balance/Deposite/Withdraw) : ")

if operation == "Balance":
    print(atm.Balance())
elif operation == "Deposite":
    atm.Balance()
    print(atm.Deposite())
elif operation == "Withdraw":
    atm.Balance()
    print(atm.Withdraw())
else:
    print("Invalid Operation")