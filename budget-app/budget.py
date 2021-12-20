class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def withdraw(self, amount, description=""):
        if self.balance < amount:
            return False
        self.balance -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(other_cat.name))
            other_cat.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False

    def __str__(self):
        string_repr = [self.name.center(30, "*")]

        for ledger in self.ledger:
            desc_line = ledger["description"][0:23]
            string_repr.append("{:<23}{:>7.2f}".format(desc_line, ledger["amount"]))

        string_repr.append("Total: {}".format(self.balance))

        return "\n".join(string_repr)


def create_spend_chart(categories):
    category_names = []
    spending_list = []
    spending_percentage = []
    # create spending percentage from category in categories
    for category in categories:
        category_names.append(category.name)

        for item in category.ledger:
            if item["amount"] < 0:
                spending_list.append(item["amount"])

    total = round(sum(spending_list), 2)

    print(
        f"Spending: {spending_list} with categories as follows: {category_names} and categories total: {total}")

    for spending in spending_list:
        percentage = spending/total * 100
        spending_percentage.append(round(percentage))
    print(f"Spending percentage is {spending_percentage} with total {sum(spending_percentage)}")

    # create the chart from spending percentage
    graph = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        graph += str(i).rjust(3) + "| "
        for spending in spending_percentage:
            if spending < i:
                graph += "   "
            elif spending >= i:
                graph += "o  "
        graph += "\n"
    graph += "    -" + ("---" * (len(category_names)))


    # create the title of budget name


    return graph
