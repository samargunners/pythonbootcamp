class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, dep_amt):
        self.balance += dep_amt
    
    def withdrawal(self,wid_amt):
        if self.balance >= wid_amt:
            self.balance -= wid_amt
            print(f'{wid_amt} Withdrawn from account')
        else:
            print('Insufficient funds')

acct1 = Account('Joese',100)

print(acct1.owner)

print(acct1.balance)

acct1.withdrawal(50)

acct1.withdrawal(75)