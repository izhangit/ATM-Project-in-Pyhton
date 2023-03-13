# ATM Machine in Python 

print("....Welcome to HDFC Account!!....")
print("")

pin = 9150
chances = 3
balances = 50000

while chances != 0:
    user_pin = int(input("Enter your pin : "))
    if user_pin != pin:
        chances -=1
        print("Worng pin! Please Enter the Right Pin! ")
        print(f"You have {chances} chances left!")
    else:
        break
while True:
        print("Enter Your Choice")
        user_choices = input("B : Balances , D : Deposit , W : Withdraw  : ")
        
        # Balances 
        if user_choices == 'b':
            print(f'Your balance is Rs.{balances}')

        # Deposit      
        if user_choices == 'd':
            deposit_user = int(input("Enter the Amount would you like to Deposit : "))
            balances = deposit_user + balances
            print(f"You've Deposited Amount Rs.{deposit_user}")
            print(f"Your Total Balance is Rs.{balances}")
            # Nested if 
            # Withdraw
        if user_choices == 'w':
            withdraw_user = int(input("Enter the amount would you like to withdraw : "))
            if withdraw_user > balances:
                print("Insufficient Balance")
            else:
                balances -= withdraw_user  
                print(f"You have Withdrawn Rs.{withdraw_user}")
                print(f"Your Total Balance is Rs.{balances}")
        
                print("")
    # User exit
        user_exit = input("Would you like exit? yes/no : ")
        if user_exit == "yes":
            print("")
            print("Thanks for Using HDFC Bank!☺")
            break
        else:
            continue


