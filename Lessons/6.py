# venv - это виртуальное окружение
# модули 3: встроенные, собственные и внешние

from Les2 import Book

# if __name__ == __main__
































class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)

    def moneyx(self):
        amount = int(input("Сумма для пополнения: "))
        self.balance + amount
        print(f'Счет пополнен. Баланс: {self.balance+amount}')

    def _kill(self):
        self.balance = 0
        print('Остаток на счету: 0')

    def _jackpot(self):
        self.balance * 10
        print('Баланс умножен на 10')

    def _bigball(self, another):
        self.balance + another.balance
        print('Балансы обьединены')

class Calculator:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return self.num1 + other.num1

    def __sub__(self, other):
        return self.num1 - other.num1

    def __mul__(self, other):
        return self.num1 * other.num1

    def __truediv__(self, other):
        return self.num1 / other.num1


bank1 = Bank('Kani', '20000')
bank2 = Bank('Bani', '40000')
bank3 = Bank('Sani', '8000')

bank1.moneyx()
bank2._kill()
bank3._jackpot()
bank1._bigball(bank2)


