from customer import Customer
from manager import Manager
from bank_utilites import home_page, logout


customer = Customer()
manager = Manager()

reloop = True

while reloop == True:
    # homepage
    home_page() 

    try :
        choice = int(input("Action: "))

    except ValueError:
        print("\ninvalid input\n")

    else:
        if choice == 1:
            customer.account_registration()

        elif choice == 2:

            if customer.sign_in() != "Failed":
                print("\nSelect action to perform with your account\n")

                reloop = False
                reloop1 = True

                while reloop1 == True:
                    try:
                        # clients action page
                        customer.clients_home()
                        choice = int(input("Action: "))

                    except ValueError:
                        print("\nInvalid choice\n")
                        
                    else:
                        if choice == 1:
                            customer.account_statement()

                        elif choice == 2:
                            customer.deposit()

                        elif choice == 3:
                            customer.withdraw_amount()

                        elif choice == 4:
                            customer.send_money()

                        elif choice ==5:
                            logout()

                        else:
                            pass

            else:
                print("\nYou don't have an account with us. Register to have acess.\n")

        elif choice == 3:
            reloop = False
            reloop1 = True

            while reloop1 == True:
                # admins home
                manager.admins_home()

                try:
                    choice = int(input("Choice: "))

                except:
                    print("\nInvalid choice chosen.\n")

                else:

                    if choice == 1:
                        manager.account_registration()
                        
                    elif choice == 2:

                        if manager.sign_in() != "Failed":
                            reloop1 = False
                            reloop2 = True

                            while reloop2 == True:
                                try:
                                    manager.admins_actions()
                                    choice = int(input("Choice: "))

                                except:
                                    print("\nInvalid input\n")

                                else:

                                    if choice == 1:
                                        manager.display_customers()

                                    elif choice == 2:
                                        manager.display_admins()

                                    elif choice == 3:
                                        manager.delete_client_account()

                                    elif choice == 4:
                                        manager.delete_admin()

                                    elif choice ==5:
                                        logout()

                                    else:
                                        print("\nInvalid chooice... try again\n")

                        else:
                            print("\nThe admin account doesn't exist... Register\n")
            

                    elif choice ==3:
                        logout()

                    else:
                        print("\nInvalid choice...\n")

        elif choice ==4:
            logout()

        else:
            print("\nInvalide choice... Try again.\n")




        