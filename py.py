class Atm:
    def __init__(self,atmCardNum,pin):
        self.atmCardNum = atmCardNum
        self.pin = pin

    def cashWithdrawal(self,amount):
        newAmount = 50000-amount
        print("you have withdrawn"+str(amount))
        print("your remaining balance is"+str(newAmount))

    def checkBal(self):
        print("Your balance is 50000")

def main():
        atmCardNum = input("Enter your card number")
        pin = input("Enter your pin")



        new_user = Atm(atmCardNum,pin)

        print("chose your activity")
        print("1. cash withdrawal, 2. check balance")
        activity = int(input("enter the activity number"))
        if activity == 1:
            new_user.checkBal()
        elif activity == 2:
            amount = int(input("Enter the amount"))
            new_user.cashWithdrawal(amount)
        else:
            print("please enter a valid option")

if __name__=="__main__":
        main()


