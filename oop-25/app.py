class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, x):
        self.__balance += x

    def withdrawal(self, y):
        self.__balance -= y



class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interest_rate = 0):
        super().__init__(title)
        self.__interest_rate = interest_rate
        self.__balance = balance


    def get_interest_rate(self):
        return self.__interest_rate

    def interest_amount(self):
        return (self.__interest_rate * self.__balance) // 100


wer = SavingsAccount('qwer', 500, 5)
wer.get_interest_rate()
print(wer.interest_amount())