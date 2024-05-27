class Money:
    
    Currency_value = {
        "20's Note" : 20,
        "10's Note" : 10,
        "5's Note/Coin" : 5,
        "2's Note/ Coin" : 2
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Total profit: {self.profit} ")

    def process_money(self):
        print("Please insert Notes/Coins here")
        money_received = 0
        for currency in self.Currency_value:
           money_received += int(input(f"How many {currency}?:"))*self.Currency_value[currency]
        return money_received
    
    def make_payment(self,cost):
        money_received = self.process_money()
        if money_received >= cost:
            change = money_received - cost
            if change !=0:
                print(f"Here is your ₹{change} change")
            self.profit += cost
            return True
        else:
            print("You do not have enough money!! Money refunded")


