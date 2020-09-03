import sqlite3

class Manager():
    def __init__(self, emp_id=[]):
        self.emp_id = emp_id

    def admins_home(self):
        print("\nWelcome to the Admins section. Only admins are allowed.\n")
        print("1. Create Bank's Admin account.")
        print("2. Sign in as an Admin.")
        print("3. Exit application.\n")
        
    def admins_actions(self):
        print("\nChooce the admin Action to Perfeorm")
        print("1. Get customers info.")
        print("2. Get admins info.")
        print("3. Delete a customer's account.")
        print("4. Delete an admin's account")
        print("5. Logout application.\n")

    def account_registration(self):
        print("\nRegister as an admin Here")

    
        try:

            name = str(input("\nName: "))
            employee_id = int(input("Enter Employee ID(Should be 8 integersi.e 12345678): "))
  

        except:
            print("\nEnter valid inputs\n")

        else:


            if (employee_id < 0) or (len(str(employee_id)) < 8):
                print("\nEnter a valid employee Id\n")

            else:
                try:
                    with sqlite3.connect("profiles.sqlite3")  as conn:
                        command = "INSERT INTO Admin VALUES(?, ?)"
                        conn.execute(command, (name, employee_id))
                        conn.commit()

                except:
                    print(f"\naccount with id: {employee_id} already exists.Try another employee Id")

                else:
                    print("")
                    print("\nYou've successfully created an account as an admin.\n")


    def sign_in(self):
        print("\nEnter employee id to sign in")

        try:
            # email = str(input("Email: "))
            employee_id = int(input("\nEmployee Id(Should be 8 integers.i.e 12345678): "))


        except:
            return "Failed "

        else:
            try:
                with sqlite3.connect("profiles.sqlite3") as conn:
                    command = "SELECT EmployeeId FROM Admin WHERE EmployeeId = ?"
                    cursor = conn.cursor()

                
                    # getting info with the id entered
                    info = tuple(cursor.execute(command, (employee_id,)))
                    #used for debugging 
                    # print(info[0])

                    # Approving the existence of the employee id in details
                    if employee_id in info[0]:
                        print("\nAdministrative actions ahead: Be keen")
                        self.emp_id.append(employee_id) 
                    
            except:
                return "Failed"

            else:
                pass
                    
                        
    def delete_client_account(self):
        client_account = str(input("\nEnter the clients account's email to delete: "))

        emails = []
        try:
            with sqlite3.connect("profiles.sqlite3") as conn:
                get_info = "SELECT Email from PersonInfo"
                cursor = conn.cursor()
                mails = tuple(cursor.execute(get_info))

                for email in mails:
                    emails.append(email[0])

                if client_account in emails:
                    delete_command = "DELETE FROM PersonInfo WHERE Email = ?"
                    cursor.execute(delete_command,(client_account,))

                    print(f"\n{client_account} has been sucessfully deleted.\n")

                else:
                    print("\nInvalid account email")

        
        except:
            print("\nSome errors...\n")

        else:
            pass
                
    
    def display_admins(self):

        with sqlite3.connect("profiles.sqlite3") as conn:
            get_admins = "SELECT * FROM Admin"

            cursor = conn.cursor()

            admins_response = tuple(cursor.execute(get_admins))

            print("\n\nBelow are the Admins Info.")
            for admin in admins_response:
                name, employee_id = admin
                print(f"\nName: {name}\t\tEmployee Id: {employee_id}")


    def display_customers(self):

        with sqlite3.connect("profiles.sqlite3") as conn:
            get_customers = "SELECT * FROM PersonInfo"

            cursor = conn.cursor()

            customers_response = tuple(cursor.execute(get_customers))

            print("\n\nBelow are the Customers Info.")
            for customer in customers_response:
                name, email, account_bal = customer
                print(f"\nName: {name}\t\tEmail:{email}\t\tAcount Balance: Sh {account_bal}")

    
    def delete_admin(self):
        admin_id_to_delete = int(input("\nEnter the admin account id to delete: "))

        emp_ids = []
        try:
            with sqlite3.connect("profiles.sqlite3") as conn:
                get_info = "SELECT EmployeeId from Admin"
                cursor = conn.cursor()
                admins_info_response = tuple(cursor.execute(get_info))

                # checking response for debugging
                # print(admins_info_response)
                for admin in admins_info_response:
                    emp_ids.append(admin[0])

                # checking emp_ids for debugging
                # print(emp_ids)
                if admin_id_to_delete in emp_ids:
                    delete_command = "DELETE FROM Admin WHERE EmployeeId = ?"
                    cursor.execute(delete_command,(admin_id_to_delete,))

                    print(f"\n{admin_id_to_delete} has been sucessfully deleted.")

                else:
                    print("\nInvalid admin's id\n")

        
        except:
            print("\nSome errors...\n")

        else:
            pass