from customer import Customer
from manager import Manager
from bank_utilites import home_page

customer = Customer()
manager = Manager()

# homepage
home_page() 

try :
    choice = int(input("Action: "))

except ValueError:
    print("invalid input")

else:
    if choice == 1:
        customer.account_registration()

    elif choice == 2:

        if customer.sign_in() != "Failed":
            print("\nSelect action to perform with your account")

            try:
                # clients action page
                customer.clients_home()

                choice = int(input("Action: "))


            except ValueError:
                print("Invalid choice")

            else:
                if choice == 1:
                    customer.account_statement()

                elif choice == 2:
                    customer.deposit()

                elif choice == 3:
                    customer.withdraw_amount()

                elif choice == 4:
                    customer.send_money()

                else:
                    pass

        else:
            print("\nYou don't have an account with us. Register to have acess.\n")


    elif choice == 3:
        # admins home
        manager.admins_home()

        try:
            choice = int(input("Choice: "))

        except:
            print("Invalid choice chosen.")

        else:
            if choice == 1:
                manager.account_registration()
            
            elif choice == 2:

                if manager.sign_in() != "Failed":

                    try:
                        manager.admins_actions()
                        choice = int(input("Choice: "))

                    except:
                        print("Invalid input")
                    else:
                        if choice == 1:
                            manager.display_customers()

                        elif choice == 2:
                            manager.display_admins()

                        elif choice == 3:
                            manager.delete_client_account()

                        elif choice == 4:
                            manager.delete_admin()

                        else:
                            print("Invalid chooice... try again")

                else:
                    print("The admin account doesn't exist... Register")

            else:
                print("Invalid choice...")


    else:
        print("Invalide choice... Try again.")




        