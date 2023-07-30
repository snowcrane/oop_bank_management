from Bank import Bank
from Users import User,Admin

def main():

    bank = Bank()
    admin = Admin(bank)

# Admin's  account
    admin.create_account('Green', 'green@gmail.com')
    admin.create_account('Grus', 'jane@gmail.com')

# User's account
    user1 = User('Snow', 'snow@gmail.com')
    user2 = User('Crane', 'crane@gmail.com')

    user1.create_account(bank)
    user2.create_account(bank)

    # check deposit
    user1.deposit(5000,bank);
    user2.deposit(500,bank)

    #check user balance
    print(user1.checkBalance(bank))
    print(user2.checkBalance(bank))

    #check withdraw
    user1.withdraw(1000,bank)
    print(user1.checkBalance(bank))

    #check transection history
    print(user1.check_transection(bank))

    # check transfer
    user1.amount_transfer('Crane',300,bank)
    print(user1.check_transection(bank))
    print(user2.check_transection(bank))

#   check loan feature
    user1.apply_loan(1000,bank)
    print(user1.check_transection(bank))
    user1.withdraw(4700,bank)
    print(user1.checkBalance(bank))
    user2.apply_loan(400,bank)

    # Admin checks total bank balance and total loan amount
    print("Total bank's fund:", admin.check_total_balance())

    # disable Admin loan feature
    admin.loan_feature()
    user1.apply_loan(1000,bank)
    print(user1.check_transection(bank))

#   check Admin Total bank's loan
    print("Total loan amount:", admin.check_total_loan())

if __name__ =='__main__':
    main()