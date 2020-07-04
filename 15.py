print("Welcome to my banking app")
class Account:
    def __init__(self, accountno, fullname, balance):
        self.balance= balance
        self.accountno = accountno
        self.fullname = fullname
    def deposit(self):
        amount = input("Enter amount to be Deposited: ")
        self.balance= self.balance+amount
        print("Balance after being deposited", self.balance)
        print(" Amount Deposited:", amount)
        

    def withdraw(self):
        amount = input("Enter amount to be Withdrawn: ")
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance")
        print("\n New Balance=", self.balance)
bankcustomer = Account('3748393473', 'Ella', '40000')

bankcustomer.deposit()
bankcustomer.withdraw()
