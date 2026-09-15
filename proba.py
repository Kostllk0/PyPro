class BankAccount:
    '''Банковский счет'''
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'''Владелец аккаунта: {self.owner}
Баланс: {self.balance}'''
    def deposit(self, amount):
        self.balance += amount
        print(f'Счет пополнен на {amount}, баланс: {self.balance}')
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Недостаточно средств на балансе')
        else:
            self.balance -= amount
            print(f'Вы сняли {amount}')
    def get_balance(self):
        return f'У вас на счету: {self.balance}'