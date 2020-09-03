import sqlite3


class Customer():

    def __init__(self, email=[]):
        self.email = email

    def clients_home(self):
        print("\n1. Get account statement.")
        print("2. Deposit amount into your account.")
        print("3. Withdraw cash")
        print("4. Send money to another account.")
        print("5. Logout\n")

    def account_registration(self):
        print("\nWelcome to account creation in Maendeleo Bank. \n\nFill in the daetails as instructed")

    
        try:

            name = str(input("\nName: "))
            email = str(input("Email: "))
            min_amount = int(input("Enter minmum amount of 100 henceforth: Sh "))
   

        except:
            print("\nEnter valid inputs\n")

        else:


            if min_amount < 100:
                print("\nEnter a valid amount\n")

            else:
                try:
                    with sqlite3.connect("profiles.sqlite3")  as conn:
                        command = "INSERT INTO PersonInfo VALUES(? , ?, ?)"
                        conn.execute(command, (name, email, min_amount))
                        conn.commit()

                except:
                    print(f"\n{email} already exist with an account. Try another email")

                else:
                    print("")
                    print("You've successfully created an account with us.")


    def sign_in(self):
        print("\nEnter your email to sign in")
        email = str(input("Email: "))

        try:
            with sqlite3.connect("profiles.sqlite3") as conn:
                command = "SELECT * FROM PersonInfo WHERE Email = ?"
                cursor = conn.cursor()

                try:
                    # getting info with the email entered
                    info = tuple(cursor.execute(command, (email,)))
                
                    #used for debugging 
                    # print(info)

                    # Approving the existence of the email in details
                    if email in info[0]:
                        print("\nSuccessful Login to your account")

                # exception expecially when the email doesn't exist
                except:
                    return "Failed"
                else:
                    self.email.append(email)

        except Exception as e:
            print(f"\nDatabase errors {e}")

        else:
            pass
            
    def deposit(self):

        login_email = self.email[0]

        # email signed in with
        # print(login_email)

        try:
            deposit = int(input("\nEnter amount to deposit(minimum 50): Sh "))
            
        except:
            print("\nEnter valid input\n")

        else:
            if deposit < 50:
                print("\nEnter valid amount\n")

            else:
                with sqlite3.connect("profiles.sqlite3") as conn:
                    command = "SELECT Amount FROM PersonInfo WHERE Email = ?"

                    cursor = conn.cursor()
                    amount = tuple(cursor.execute(command, (login_email,)))

                    # for confirming amounts : debugging purpose
                    # print(amount[0][0])

                    new_amount = int(amount[0][0]) + deposit

                    command_update = "UPDATE PersonInfo SET Amount = ? WHERE Email = ?"

                    # amount

                    cursor.execute(command_update, (new_amount, login_email))

                    tot = tuple(cursor.execute(command, (login_email,)))

                    print(f"\nSuccessful deposit of {deposit}\nYour current balnce is: Sh {tot[0][0]}")


    def withdraw_amount(self):
        login_email = self.email[0] 

        with sqlite3.connect("profiles.sqlite3") as conn:
            command = "SELECT Amount FROM PersonInfo WHERE Email = ?"
            cursor = conn.cursor()
             
            original_bal = tuple(cursor.execute(command, (login_email,)))

            # original balance confirmation
            # print(original_bal[0][0])

            try:
                withdrawal_amt = int(input("\nEnter amount to withdraw: Sh "))

            except:
                print("\nEnter valid input\n")

            else:
                if withdrawal_amt > original_bal[0][0]:
                    print("\nThe amount exceeds your balance amount.")

                else:
                    if withdrawal_amt < 1:
                        print("\nInvalid amount\n")

                    else:
                        
                        balance = original_bal[0][0] - withdrawal_amt

                        print(balance)

                        command_update = "UPDATE PersonInfo SET Amount = ? WHERE Email = ?"

                        cursor.execute(command_update, (balance, login_email))

                        current_bal = tuple(cursor.execute(command, (login_email,)))

                        print(f"\n\nSuccessful withdrawal of Sh {withdrawal_amt}.\nCurrent balance is: Sh {current_bal[0][0]}")


    def send_money(self):

        login_email = self.email[0]

        receiver = str(input("\nEnter email of the recepient account: "))

        with sqlite3.connect("profiles.sqlite3") as conn:
            command = "SELECT Email FROM PersonInfo"

            get_amount = "SELECT Amount from PersonInfo WHERE Email = ?"

            cursor = conn.cursor()
            
            mails = list(cursor.execute(command))

            amount_request = tuple(cursor.execute(get_amount, (login_email,)))

            original_bal = amount_request[0][0]

            print(f"\nBalance: Sh {original_bal}")

            emails = []

            for email in mails:

                # print(email[0])
                
                emails.append(email[0])
            
            # for debugging : confirming emails existence
            # print(emails)

            if receiver in emails:
                print(f"\n\nYou're about to send money to: {receiver}\n")

                try:
                    amount_to_send = int(input("Enter the amount to send: Sh "))

                except:
                    print("\nEnter a valid input\n")
                else:
                    if (amount_to_send < 1) or (amount_to_send > original_bal):
                        print("Invalid amount.\n")

                    else:
                        
                        # getting the recepinte's original balance and updating it
                        receiver_orignal_bal = tuple(cursor.execute(get_amount, (receiver,)))
                        receiver_updated_bal = receiver_orignal_bal[0][0] + amount_to_send
                        
                        update_amount = "UPDATE PersonInfo SET Amount = ? WHERE Email = ?" 

                        # updating the recepients's amount side
                        cursor.execute(update_amount, (receiver_updated_bal, receiver)) 

                        # updating the the senders amount side 
                        rem_amount = original_bal - amount_to_send
                        cursor.execute(update_amount, (rem_amount, login_email))

                        # cross checking transaction result
                        current_balance = tuple(cursor.execute(get_amount, (login_email,)))

                        print(f"\n\nYou've successfully sent Sh {amount_to_send} to {receiver}; Current balance: Sh {current_balance[0][0]}")
                     
                      
                    

            else:
                print(f"\nNo account with id : {receiver}\n")

    def account_statement(self):
        login_email = self.email[0]

        with sqlite3.connect("profiles.sqlite3") as conn:
            get_statement = "SELECT * FROM PersonInfo WHERE Email = ?"

            cursor = conn.cursor()
            statement_response = tuple(cursor.execute(get_statement, (login_email,)))

            name, email, account_balance = statement_response[0]

            print("\nYour Account statement is as follows.")
            print(f"\nName : {name}\nEmail: {email}\nAccount Balance: Sh {account_balance}\n")