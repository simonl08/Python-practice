#ATM machine
def card_pin(pin):
    print("Please enter your pin number: ")
    pin=int(input()) 
    if pin == 6531:
        print("You have logged in successfully")
        withdraw()
    else: 
        print("You have failed to login, please try again")

def withdraw():
        print("Welcome to the atm")
        i=0
        while i <=3:
            print("How can we help you today?")
            print("1. Check balance \n2. Withdraw Cash \n3. exit")
            options = int(input())
            if options == 1:
                balance = 1000
                print(f"Your current balance is £{balance}")
            elif options == 2:
                print("Please enter the amount of cash you would like to withdraw?: ")
                cash =int(input())
                if balance > cash:
                    balance -= cash
                    print("You have withdrawn £{} from your bank, your new balance is £{}".format(cash, balance))
                else:
                    print("Your transaction has failed please refer to your current balance before withdrawing")
            elif options == 3:
                print("Thank you for using our atm")
                break

card_pin(1)
