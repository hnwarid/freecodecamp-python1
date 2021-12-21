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
    spendings = []
    percentages = []

    # create spending percentage from category in categories
    for category in categories:
        spending_total = 0
        category_names.append(category.name)
        for item in category.ledger:
            if item["amount"] < 0:
                spending_total += item["amount"]
        spendings.append(spending_total)
    for spending in spendings:
        percentage = round(spending/sum(spendings) * 100)
        percentages.append(percentage)

    # create the chart from spending percentage
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage < i:
                chart += "   "
            elif percentage >= i:
                chart += "o  "
        chart += "\n"
    chart += "    -" + ("---" * (len(category_names))) + "\n"

    # create the title of budget name
    chart_length = 0
    for name in category_names:
        if len(name) > chart_length:
            chart_length = len(name)

    for i in range(chart_length):
        chart += "     "
        for name in category_names:
            if i > len(name[:i]):
                chart += "   "
            elif len(name) > i:
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < chart_length-1:
            chart += "\n"

    return chart
