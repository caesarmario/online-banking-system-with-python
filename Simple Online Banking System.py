# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

##1. Admin related functions ##
#Admin login function
def admin_login():
    print("\n+++ Admin Login Menu +++")
    admin_ID = str(input("> Enter your Admin ID: "))
    admin_pass = str(input("> Enter your Password: "))
    admin_file = open("admin_db.txt","r")
    for line in admin_file:
        login_admin = line.strip().split(",")
        if (admin_ID == login_admin[0] and admin_pass == login_admin[2]):
            print("\n\n=== WELCOME, ",login_admin[1]," ===")
            admin_menu()
            return True
    print("!!! You enter wrong ID or Password !!!")
    print("--- Return to Admin Login ---\n\n")
    admin_login()
    return False

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Admin menu after login function
def admin_menu():
    print("\n>> Admin MENU:")
    print("1. Create NEW Profile\n2. Search Customer Data\n3. Search Customer Transaction\n4. Log Out")
    opt_admin_menu=int(input("> Please select your option (1/2/3/4): "))
    while(opt_admin_menu !='4'):
        if (opt_admin_menu==1):
            admin_new_profile()
        elif(opt_admin_menu==2):
            admin_search_customer_data()
        elif(opt_admin_menu==3):
            admin_search_customer_transaction()
        elif(opt_admin_menu==4):
            print("=== GOOD BYE, SEE YOU AGAIN! ===\n\n")
            main_menu()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
        opt_admin_menu=int(input("Please select your option (1/2/3/4): "))

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Admin new customer profile
def admin_new_profile():
    print("\nYou choose '1. Create NEW Profile'")
    print("----------------------------------")
    customer_file = open("customer_db.txt","a")
    transaction_file = open("transaction_db.txt","a")
    new_customer_id = str(input("> Enter new customer ID: "))
    new_customer_name = str(input("> Enter new customer NAME: "))
    new_customer_address = str(input("> Enter new customer ADDRESS: "))
    new_customer_phone = str(input("> Enter new customer PHONE: "))
    new_customer_pass = str(input("> Enter new customer PASSWORD: "))
    new_customer_balance = str(input("> Enter BALANCE for new customer: "))
    customer_file.write(new_customer_id+","+new_customer_name+","+new_customer_address+","
                        +new_customer_phone+","+new_customer_pass+","+new_customer_balance+"\n")
    customer_file.close()
    transaction_file.write(new_customer_id+","+new_customer_balance+",Deposit\n")
    transaction_file.close()
    print("*** NEW ACCOUNT CREATED! ***")
    print("--- RETURN TO ADMIN MENU ---\n")
    admin_menu()
    
# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Admin search customer data
def admin_search_customer_data():
    print("\nYou choose '2. Search Customer Data'")
    print("----------------------------------")

    customer_id = str(input("> Enter customer ID: "))
    customer_file = open("customer_db.txt","r")
    for line in customer_file:
        search_customer = line.strip().split(",")
        if (customer_id == search_customer[0]):
            print("===== DATA FOUND =====")
            print("ID\t:"+search_customer[0]+"\nName\t:"+search_customer[1]+
                  "\nAddress\t:"+search_customer[2]+"\nPhone Number\t:"+search_customer[3])
            print("--- RETURN TO ADMIN MENU ---\n")
            admin_menu()
            return True
    print("!!! DATA NOT FOUND ! !!!")
    print("--- RETURN TO ADMIN MENU ---\n")
    admin_menu()
    return False

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Admin search customer transaction
def admin_search_customer_transaction():
    print("\nYou choose '3. Search Customer Transaction'")
    print("----------------------------------")
    current_balance=0
    admin_view_id = str(input("> Enter customer ID: "))
    transaction_file = open("transaction_db.txt","r")
    print("\n=== Transaction History ===\n")
    for line in transaction_file:
        view_transaction_file = line.strip().split(",")
        if (admin_view_id == view_transaction_file[0]):
            current_balance=int(view_transaction_file[1])+current_balance
            print(view_transaction_file[2]+"\t\t"+view_transaction_file[1])
    print(">> Current Balance: ",current_balance)
    print("--- Return to Admin Menu ---\n\n")
    admin_menu()

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

##2. Customer related functions ##
#Customer login menu
def customer_login():
    print("\n\n*** WELCOME Customer! Please enter your login! ***")
    customer_id = str(input("> Enter your Customer ID: "))
    customer_pass = str(input("> Enter your Password: "))
    customer_file = open("customer_db.txt","r")
    for line in customer_file:
        login_customer = line.strip().split(",")
        if (customer_id == login_customer[0] and customer_pass == login_customer[4]):
            print("\n\n=== WELCOME, ",login_customer[1]," ===")
            customer_menu()
            return True
    print("!!! You enter wrong ID or Password !!!")
    print("--- Return to Customer Login ---")
    customer_login()
    return False

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Customer menu after login function
def customer_menu():
    print(">> Customer MENU:\n")
    print("1. Deposit\n2. Withdrawal\n3. View Transaction\n4. Logout")
    opt_customer_menu=int(input("> Please select your option (1/2/3/4): "))
    while(opt_customer_menu !='4'):
        if (opt_customer_menu==1):
            customer_deposit()
        elif(opt_customer_menu==2):
            customer_withdraw()
        elif(opt_customer_menu==3):
            customer_view()
        elif(opt_customer_menu==4):
            print("*** Good bye! Have a nice day! ***\n\n")
            main_menu()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
        opt_customer_menu=int(input("> Please select your option (1/2/3/4): "))
        

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Customer deposit transaction
def customer_deposit():
    print("\nYou choose '1. Deposit'")
    print("----------------------------------")
    deposit_id = str(input("> Enter your Customer ID: "))
    deposit_balance = str(input("> Enter the BALANCE to be deposit: "))
    deposit_pass = str(input("> Enter your Password: "))
    customer_file = open("customer_db.txt","r")
    transaction_file = open("transaction_db.txt","a")
    for line in customer_file:
        cust_deposit = line.strip().split(",")
        if (deposit_id == cust_deposit[0] and deposit_pass == cust_deposit[4]):
            transaction_file.write(deposit_id+","+deposit_balance+",Deposit\n")
            transaction_file.close()
            print("*** BALANCE SUCSSESFULLY DEPOSIT! ***")
            print("--- Return to Customer Menu ---\n")
            customer_menu()
            return True
    print("!!! You enter wrong ID or Password !!!")
    print("--- Return to Customer Menu ---\n\n")
    customer_menu()
    return False
    
# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Customer withdraw transaction
def customer_withdraw():
    print("\nYou choose '2. Withdrawal'")
    print("----------------------------------")
    withdrawal_id = str(input("> Enter your Customer ID: "))
    withdrawal_balance = str(input("> Enter the BALANCE to be withdraw: "))
    withdrawal_pass = str(input("> Enter your Password: "))
    customer_file = open("customer_db.txt","r")
    transaction_file = open("transaction_db.txt","a")
    for line in customer_file:
        cust_withdrawal = line.strip().split(",")
        if (withdrawal_id == cust_withdrawal[0] and withdrawal_pass == cust_withdrawal[4]):
            transaction_file.write(withdrawal_id+",-"+withdrawal_balance+",Withdrawal\n")
            transaction_file.close()
            print("*** WITHDRAWAL SUCCESS! ***")
            print("--- Return to Customer Menu ---\n")
            customer_menu()
            return True
    print("!!! You enter wrong ID or Password !!!")
    print("--- Return to Customer Menu ---\n\n")
    customer_menu()
    return False
    
# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Customer view transaction 
def customer_view():
    current_balance=0
    print("\nYou choose '3. View Transaction'")
    print("----------------------------------")
    view_id = str(input("> Enter customer ID: "))
    transaction_file = open("transaction_db.txt","r")
    print("\n=== Transaction History ===\n")
    for line in transaction_file:
        view_transaction_file = line.strip().split(",")
        if (view_id == view_transaction_file[0]):
            current_balance=int(view_transaction_file[1])+current_balance
            print(view_transaction_file[2]+"\t\t"+view_transaction_file[1])
    print(">> Current Balance: ",current_balance)
    print("--- Return to Customer Menu ---\n\n")
    customer_menu()
    
# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#Main menu
def main_menu ():
    print("**** WELCOME TO APU's ONLINE BANKING SYSTEM ****\n")
    print(">> MAIN MENU")
    print("1. Admin\n2. Customer\n3. Exit")
    opt_main_menu=int(input("> Please select your login as (1/2/3): "))
    while(opt_main_menu !='4'):
        if (opt_main_menu==1):
            admin_login()
        elif(opt_main_menu==2):
            customer_login()
        elif(opt_main_menu==3):
            quit()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
        opt_main_menu=int(input("> Please select your login as (1/2/3): "))


# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_

#To run main menu functions at first time
main_menu()

# Simple Online Banking System by caesarmario
# More about myself: https://linktr.ee/caesarmario_