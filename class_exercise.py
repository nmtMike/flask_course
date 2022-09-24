class BankAccount():
    def __init__(self, owner:str = 'user', balance:int = 0):
        self.owner = owner
        self.balance = balance
        print('thank you for your belief in our survice')

    def __repr__(self):
        return f'''Bank account information:
        owner: {self.owner}
        current balance {self.balance} '''
    
    def deposit(self, amount:int):
        self.balance += amount
        print(f'your ${amount} have been deposited successfully!!!')
        print(f'current balance {self.balance} ')
    
    def withdraw(self, amount:int):
        if self.balance >= amount:
            self.balance -= amount
            print(f'your ${amount} have been withdrawed successfully!!!')
        else: print(f'sorry, your current blance is ${self.balance}!!!')


acct1 = BankAccount(owner='Jose', balance=100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(20)
acct1.withdraw(10000)
