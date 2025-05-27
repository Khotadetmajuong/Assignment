#methodoverloading to handle deposit methods
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, *args):
        if len(args) == 1:
            amount = args[0]
            print(f"Depositing ${amount} in cash.")
        elif len(args) == 2:
            amount, cheque_no = args
            print(f"Depositing ${amount} via cheque #{cheque_no}.")
        elif len(args) == 3:
            amount, bank_name, txn_id = args
            print(f"Depositing ${amount} via online transfer from {bank_name}, txn ID: {txn_id}.")
        else:
            print("Invalid deposit method.")
            return

        self.balance += amount
        print(f"New balance: ${self.balance}\n")
       

# Usage
acc = BankAccount("Alice")

acc.deposit(1000)                              # Cash deposit
acc.deposit(2000, "CHQ123456")                 # Cheque deposit
acc.deposit(3000, "Chase Bank", "TXN789456")   # Online transfer

print('...........................................................................')
print('...........................................................................')





#Method Overloading Example 2:  E-commerce Shipping Cost Calculator
class ShippingCalculator:
    def calculate_cost(self, *args):
        if len(args) == 1:
            weight = args[0]
            cost = weight * 5
            print(f"Standard shipping cost for {weight}kg: ${cost}")
        elif len(args) == 2:
            weight, distance = args
            cost = weight * 5 + distance * 0.1
            print(f"Regional shipping cost for {weight}kg over {distance}km: ${cost}")
        elif len(args) == 3:
            weight, distance, express = args
            cost = weight * 5 + distance * 0.1 + (20 if express else 0)
            shipping_type = "Express" if express else "Regular"
            print(f"{shipping_type} shipping cost for {weight}kg over {distance}km: ${cost}")
        else:
            print("Invalid input for shipping cost calculation.")

# Usage
calc = ShippingCalculator()
calc.calculate_cost(10)                        # Standard
calc.calculate_cost(10, 100)                   # Regional
calc.calculate_cost(10, 100, True)             # Express
