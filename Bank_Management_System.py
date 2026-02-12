import random
from abc import ABC, abstractmethod

#Abstract Class
class Account(ABC):
    bank_name = 'Repubic National Bank'

    def __init__(self, acc_num, holder_name, bal=0):
        self.__acc_num = acc_num
        self.__holder_name = holder_name
        self.__bal = bal
        self.transactions = [] 

    # Encapsulation
    def get_acc_num(self):
        return self.__acc_num

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self, name):
        self.__holder_name = name

    def get_bal(self):
        return self.__bal

    def _update_bal(self, amount):
        self.__bal += amount

    # Abstraction
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def account_type(self):
        pass

    def add_transaction(self, message):
        self.transactions.append(
            f'{message}'
        )

    def show_transactions(self):
        if not self.transactions:
            print('No transactions yet.')
        else:
            print(f'\nTransaction History for {self.__holder_name}:')
            for trn in self.transactions:
                print(' - ', trn)

    def display_info(self):
        print('\n====== Account Info ======')
        print(f'Bank Name      : {Account.bank_name}')
        print(f'Account Number : {self.__acc_num}')
        print(f'Holder Name    : {self.__holder_name}')
        print(f'Balance        : ₹{self.__bal}')
        print(f'Account Type   : {self.account_type()}')
        print("===========================\n")

# ================================
# Inheritance and Polymorphism
# ================================

class SavingsAccount(Account):

    def __init__(self, acc_num, holder_name, bal=0, interest_rate=0.04):
        super().__init__(acc_num, holder_name, bal)
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._update_bal(amount)
            self.add_transaction(f'Deposited ₹{amount}')
            print(f'₹{amount} deposited successfully!')
        else:
            print('Invalid deposit amount!')

    def withdraw(self, amount):
        if 0 < amount <= self.get_bal():
            self._update_bal(-amount)
            self.add_transaction(f'Withdrawn ₹{amount}')
            print(f'₹{amount} withdrawn successfully!')
        else:
            print('Insufficient balance or invalid amount!')

    def add_interest(self):
        interest = self.get_bal() * self.__interest_rate
        self._update_bal(interest)
        self.add_transaction(f'Interest added ₹{interest:.2f}')
        print(f'Interest ₹{interest:.2f} added to your account!')

    def account_type(self):
        return 'Savings Account'


class CurrentAccount(Account):

    def __init__(self, acc_num, holder_name, bal=0, overdraft_limit=5000):
        super().__init__(acc_num, holder_name, bal)
        self.__overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self._update_bal(amount)
            self.add_transaction(f'Deposited ₹{amount}')
            print(f'₹{amount} deposited successfully!')
        else:
            print('Invalid deposit amount!')

    def withdraw(self, amount):
        if 0 < amount <= (self.get_bal() + self.__overdraft_limit):
            self._update_bal(-amount)
            self.add_transaction(f'Withdrawn ₹{amount}')
            print(f'₹{amount} withdrawn successfully!')
        else:
            print('Overdraft limit exceeded!')

    def account_type(self):
        return 'Current Account'

# ================================
# Bank Account Creation and Perform Operations
# ================================

class Bank:
    def __init__(self):
        self.__accounts = {}

    def __generate_unique_account_number(self):
        while True:
            acc_num = str(random.randint(1000000000, 9999999999))
            if acc_num not in self.__accounts:
                return acc_num

    def create_account(self):
        holder_name = input('Enter Holder Name: ')
        acc_type = input('Enter Account Type (Savings/Current): ')
        initial_deposit = float(input('Enter Initial Deposit: '))

        acc_num = self.__generate_unique_account_number()

        if acc_type == 'Savings':
            account = SavingsAccount(acc_num, holder_name, initial_deposit)
        elif acc_type == 'Current':
            account = CurrentAccount(acc_num, holder_name, initial_deposit)
        else:
            print('Invalid account type!')
            return

        self.__accounts[acc_num] = account
        print(f'\n Account created successfully! Your Account Number is: {acc_num}\n')

    def find_account(self, acc_num):
        return self.__accounts.get(acc_num, None)

    def perform_deposit(self):
        acc_num = input('Enter Account Number: ')
        amount = float(input('Enter Deposit Amount: '))
        acc = self.find_account(acc_num)
        if acc:
            acc.deposit(amount)
        else:
            print('Account not found!')

    def perform_withdrawal(self):
        acc_num = input('Enter Account Number: ')
        amount = float(input('Enter Withdrawal Amount: '))
        acc = self.find_account(acc_num)
        if acc:
            acc.withdraw(amount)
        else:
            print('Account not found!')

    def show_balance(self):
        acc_num = input('Enter Account Number: ')
        acc = self.find_account(acc_num)
        if acc:
            acc.display_info()
        else:
            print('Account not found!')

    def add_interest(self):
        acc_num = input('Enter Account Number: ')
        acc = self.find_account(acc_num)
        if isinstance(acc, SavingsAccount):
            acc.add_interest()
        else:
            print('Interest applicable only for savings accounts!')

    def show_all_accounts(self):
        if not self.__accounts:
            print('No accounts found!')
        else:
            for acc in self.__accounts.values():
                acc.display_info()

    @staticmethod
    def bank_info():
        print(f'\n Welcome to {Account.bank_name}')
        print('We provide Savings and Current accounts with auto-generated numbers!\n')


def main():
    Bank.bank_info()
    bank = Bank()

    while True:
        print('====== BANK MANAGEMENT MENU ======')
        print('1. Create Account')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Check Balance')
        print('5. Add Interest (Savings Only)')
        print('6. Show All Accounts')
        print('7. Exit')
        print("==================================")

        choice = input('Enter choice (1-7): ')

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.perform_deposit()
        elif choice == '3':
            bank.perform_withdrawal()
        elif choice == '4':
            bank.show_balance()
        elif choice == '5':
            bank.add_interest()
        elif choice == '6':
            bank.show_all_accounts()
        elif choice == '7':
            print('Thank you for banking with us! Goodbye!')
            break
        else:
            print('Invalid choice, please try again!')


if __name__ == '__main__':
    main()
