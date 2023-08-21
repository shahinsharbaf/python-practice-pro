class BankAccount:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        try:
            amount = float(amount)
            self.balance += amount
            print("$%0.2f increased" % amount)
            self.show_balance()
        except:
            print("not valid")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                print("the amount is high than balance")
            else:
                self.balance -= amount
                print("$%0.2f decreased" % amount)
                self.show_balance()
        except:
            print("not valid")

    def show_balance(self):
        print("you balance is %0.2f" % self.balance)
