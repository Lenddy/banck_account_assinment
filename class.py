class BankAccount:
    # if you waht to change the interes rate just chane the int_rate number 
    def __init__(self,balance = 0,int_rate = 0.01):
        self.int_rate = int_rate
        self.balance = balance


        
    def deposit(self, amount):
        current_balance = self.balance
        new_balance= current_balance + amount
        self.balance = new_balance


    def withdraw(self, amount2):
        current_balance2 = self.balance
        new_balance2 = current_balance2 - amount2
        self.balance = new_balance2


    def display_account_info(self):
        print("your balance is", self.balance)
        print("your interest rate is",self.int_rate)


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate 

# if you want to change the amount on your account just change the number on account = BankAccount()
account = BankAccount(100.00)
account.display_account_info()
# if you want to deposit a differnt amount just change the value inside account.deposit()
account.deposit(100.00)
account.display_account_info()
# if you want to withdraw a differnt amount just change the value inside account.withdraw()
account.withdraw(50.00)
account.display_account_info()
account.yield_interest()
account.display_account_info()


