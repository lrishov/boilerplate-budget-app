class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount' : amount, 'description' : description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount' : - (amount), 'description' : description})
            return True
        return False
    
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
    
    
    def transfer(self, amount, receiver):
        if self.check_funds(amount):
            self.ledger.append({'amount' : - (amount), 'description' : 'Transfer to ' + receiver.name})
            receiver.ledger.append({'amount' : amount, 'description' : 'Transfer from ' + self.name})
            return True
        return False
        
    def check_funds(self, amount):
        return self.get_balance() >= amount
     
    def __str__(self):
        check = self.name.center(30,"*")
        for item in self.ledger:
            check = check + '\n' + f"{item['description'][0:23]:<23}{item['amount']:>7.2f}"
        check = check + '\n' + 'Total: ' + str(self.get_balance())
        return check


def create_spend_chart(categories):
    chart = {}
    for item in categories:
        chart[item.name] = abs(sum([x['amount'] for x in item.ledger if x['amount'] < 0]))
    result = {key: int(round(value / sum(chart.values()), 2)*100) for key, value in chart.items()}
    x = "Percentage spent by category"
    for percent in range(100, -10,-10):
        x = x + "\n" + f"{percent:>3}"+ "|"
        for key, value in result.items():
            if value >= percent:
                x = x + " o "
            else:
                x = x + "   "
        x = x + " " 
    x = x + "\n    " + (len(result) * 3 + 1) * "-"
    chart = list(result.keys())
    for i in range(0,len(max(chart, key=len))):
        x = x + "\n    "
        for item in chart:
            try: 
                if item[i]: 
                    x = x + " " + item[i] + " "
            except:
                x = x + "   "
        x = x + " "

    return x
