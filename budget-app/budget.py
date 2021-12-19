class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def withdraw(self, amount, description=""):
        if self.balance < amount:
            return False
        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount
        return True

    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(other_cat.name))
            other_cat.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False

    def __str__(self):
        string_repr = [self.name.center(30, "*")]

        for dict in self.ledger:
            desc_line = dict["description"][0:23]
            string_repr.append("{:<23}{:>7.2f}".format(desc_line, dict["amount"]))

        string_repr.append("Total: {}".format(self.balance))

        return "\n".join(string_repr)


def create_spend_chart(categories):
    pass