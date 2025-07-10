class Account:
    def __init__(self, account_number, account_balance):
        self.accno = account_number
        self.accbalance = account_balance

    def debit(self, amt):
        self.accbalance -= amt
        print(f"Rs.{amt} Debited..")
        self.getbalance()
        
    def credit(self, amt):
        self.accbalance += amt
        print(f"Rs.{amt} Credited..")
        self.getbalance()
            
    def getbalance(self):
        print(f"Current Balance: {self.accbalance}")

acc1 = Account(123456789, 0)
acc1.getbalance()
acc1.credit(40000)
acc1.debit(500)