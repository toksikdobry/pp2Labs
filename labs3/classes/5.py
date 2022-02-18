class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        def __init__(self, money):
            self.money = money
        self.balance += money

    def withdraw(self, money):
        def __init__(self, money):
            self.money = money
        if(self.balance >= money): self.balance -= money
        else: self.balance -= (money - (money - self.balance))

    def res(self):
        return self.owner, self.balance

account = Bank("Yelaman", 1000)
account.deposit(100)
print(account.res())