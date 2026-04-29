#Create a class bankaccount with attributes owner and balance and lastly implement methods of deposit,withdraw and show balance
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited UGX {amount}.") 
    
    def withdraw(self, amount):
        if amount>self.balance:
            print(f"You cannot withdraw an amount greater than current balance")   
        else:
            self.balance-=amount
            print(f"You have withdrawn UGX{amount}.")
    def show_balance(self):
        print(f"Your balance is {self.balance}")
           
    
b1= BankAccount("Lyn",2000)
b1.deposit(20000)
b1.show_balance() 
b1.withdraw(200000)
b1.show_balance()  