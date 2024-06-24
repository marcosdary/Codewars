class BankAccount:
    def __init__(self, deposit, fees, inflation) -> None:
        self.deposit = deposit
        self.fees = fees
        self.inflation = inflation
    
    def lifeplan(self, value, time):
        if self.deposit >= 0 and time > 0:
            return True
        
        if self.deposit < 0:
            return False
        cal = self.deposit + ((self.fees/100)*self.deposit) - value
        self.deposit = round(cal, 0)
        value = round(value + (value * (self.inflation/100)), 1)
        
        time -= 1

        return self.lifeplan(value, time)
    
def fortune(f0, p, c0, n, i):
    account = BankAccount(f0, p, i)
    return account.lifeplan(c0, n)

print(fortune(4383861, 4, 293380, 14, 7))