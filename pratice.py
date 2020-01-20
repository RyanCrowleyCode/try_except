# Basic Exception Handling
# Because Python is a dynamically typed language, you need to carefully consider how to get the type of a variable and make no assumptions in your code.

# Let's look at some basic code and see what harmful side-effects can happen.

class BankAccount():
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        """Add money to a bank account

        Arguments:
            amount - a numberical value by which the bank account's balance will increase
        """
        try:
            self.balance += amount
            print(f'${amount} was added to your account.')
        except TypeError:
            print("Error: The add_money method requires a numeric value.")

        self.get_balance()

    def withdraw_money(self, amount):
        """Withdraw money from a bank account

        Arguments:
            amount - A numerical value by which the bank account's balance will decrease
        """
        try:
            if self.balance - amount < 0:
                raise ValueError("Error: Insufficient funds.")
            else:
                self.balance -= amount
                print(f'${amount} was withdrawn from your account.')
        except ValueError as error:
            print(error)
        except TypeError:
            print("Error: The withdraw_money method requires a numeric value.")
            
        self.get_balance()
    
    def get_balance(self):
        print(f'Your current balance is ${self.balance}.')

        

my_account = BankAccount()
# my_account.add_money('Gazillion dollars')
my_account.add_money(50)

print()
my_account.withdraw_money(10)
        