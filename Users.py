from Bank import Bank
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        

    def create_account(self,bank):
        if self.name not in bank.accounts:
            bank.accounts[self.name] = {
                'email': self.email,
                'balance': 0,
                'loan': 0,
                'transaction': []
            }
            print(f"Bank Account created for {self.name}.")
        else:
            print("Account Name already exists.")

    def checkBalance(self,bank):
        if self.name in bank.accounts:
            return bank.accounts[self.name]['balance']
        else:
            print("Account Not available")


    def deposit(self, amount, bank):
        if self.name in bank.accounts:
            bank.accounts[self.name]['balance'] += amount
            bank.banks_fund += amount
            bank.accounts[self.name]['transaction'].append(f"Deposited: {amount}")
            print(f"Deposit {amount} successful. {self.name} balance: {bank.accounts[self.name]['balance']}")
        else:
            print("Account not found.")

    def withdraw(self,amount,bank):
        if self.name in bank.accounts and bank.accounts[self.name]['balance'] >= amount:
            bank.accounts[self.name]['balance'] -= amount
            bank.accounts[self.name]['transaction'].append(f"Debited: {amount}")
        elif bank.banks_fund == 0 :
            print('The bank is bankrupt')
        else:
            print("Insufficient balance")

    def check_transection(self,bank):
        if self.name in bank.accounts:
            return bank.accounts[self.name]['transaction']
        else:
            print("ACCOUNT NOT AVAILABLE")

    def amount_transfer(self,reciver,amount,bank):
        if self.name and reciver in bank.accounts:
            if bank.accounts[self.name]['balance'] >= amount:
                bank.accounts[reciver]['balance'] += amount
                bank.accounts[reciver]['transaction'].append(f"Deposited: {amount}")
                bank.accounts[self.name]['balance'] -= amount
                bank.accounts[self.name]['transaction'].append(f"Debited: {amount}")
                print(f'Trafer {amount} successfully to {reciver}')
            else:
                print('Insufficient amount')
        else:
            print('Invalid Account')

    def apply_loan(self,amount,bank):
        if bank.loan_available:
            if self.name in bank.accounts:
                if bank.banks_fund <= amount:
                    print('The Bank has  insufficient fund for providing Loan')
                elif amount <= bank.accounts[self.name]['balance'] * 2:
                    bank.accounts[self.name]['balance'] += amount
                    bank.accounts[self.name]['loan'] += amount
                    bank.banks_fund -= amount
                    bank.total_loan += amount
                    bank.accounts[self.name]['transaction'].append(f"loan: {amount}")
                    print(f'your loan application for amount {amount} is successfull')
                else:
                    print(f"Amount is not valid You can take loan upto {bank.accounts[self.name]['balance'] * 2}")

            else:   
                print('Invalid Account')
        else:
            print('Loan feature is currently off')

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email):
        if name not in self.bank.accounts:
            self.bank.accounts[name] = {
                'email': email                
            }
            print(f"Admin Account created for {name}.")
        else:
            print("Account Name already exists.")

    def check_total_balance(self):
        return self.bank.banks_fund

    def check_total_loan(self):
        return self.bank.total_loan

    def loan_feature(self):
        self.bank.loan_available = not self.bank.loan_available
        print(f"Loan feature is now {'enabled' if self.bank.loan_available else 'disabled'}")


