import time

# Sample database for users
data = {
    # Account no. : ["First name", "Last name", "Password", Balance]
    1: ["Aryan", "Raj", "pass0321", 82627],
    2: ["Aniruddh", "", "word1230", 7282]
}

# Function to create a new user account
def createUser():
    while True:
        print("Creating new user")
        print("Enter your details")
        print()
        time.sleep(0.5)
        
        # Input for user details
        fname = input("Enter your first name : ").title()
        time.sleep(0.3)
        lname = input("Enter your last name : ").title()
        print()
        time.sleep(0.3)
        
        fname = " ".join(fname.split())  # Remove extra spaces
        lname = " ".join(lname.split())
        
        if fname == "":
            print("First name is empty")
            print()
            continue
        else:
            print(f"Your first name is : {fname}")
            time.sleep(0.3)
            print(f"Your last name is : {lname}")
            print()
            time.sleep(0.5)
            
            print("Enter [C] to continue")
            print("Enter [R] to resubmit")
            print("Enter [X] to exit")
            print()
            time.sleep(0.5)
            
            command = input("Enter [KEY] : ").lower()
            print()
            time.sleep(0.5)
        
        if command == "c":
            # Create a password and add user to database
            password = createPass()
            acc = len(data) + 1
            data[acc] = [fname, lname, password, 0]
            print("User created successfully")
            print()
            time.sleep(0.3)
            print("Your details")
            print(f"Account no. : {acc}")
            print(f"Name : {fname} {lname}")
            print(f"Password : {password}")
            print()
            time.sleep(0.5)
        elif command == "r":
            createUser()
        elif command == "x":
            return
        else:
            print(f"You entered wrong key [{command}]")
            print()
            time.sleep(0.5)
        break

# Function to create a password
def createPass():
    while True:
        print("Create your password for banking")
        print("Password should be at least 8 characters")
        print()
        time.sleep(0.5)
        
        password = input("Create a password : ")
        time.sleep(0.3)
        cpassword = input("Confirm your password : ")
        print()
        time.sleep(0.5)
        
        if len(password) < 8:
            print("Password is less than 8 characters")
            print()
            time.sleep(0.5)
            continue
        elif cpassword != password:
            print("Confirm password didn't match")
            print()
            time.sleep(0.5)
            continue
        else:
            return password

# Function for user login
def login():
    print("Login to your account")
    print()
    time.sleep(0.5)
    
    acc = int(input("Enter your account number : "))
    time.sleep(0.3)
    fname = input("Enter your first name : ").capitalize()
    time.sleep(0.3)
    password = input("Enter your banking password : ")
    print()
    time.sleep(0.5)
    
    if acc in data:
        if fname in data[acc]:
            if password in data[acc]:
                showUser(acc)
            else:
                print("Password is incorrect")
                print()
                time.sleep(0.5)
        else:
            print("First name is incorrect")
            print()
            time.sleep(0.5)
    else:
        print("Account not found")
        print()
        time.sleep(0.5)

# Function to show user dashboard
def showUser(acc):
    while True:
        print(f"Account No. : {acc}")
        print(f"Name : {data[acc][0]} {data[acc][1]}")
        print(f"Balance : {data[acc][3]}")
        print()
        time.sleep(0.5)
        
        print("Enter [D] to deposit")
        print("Enter [W] to withdraw")
        print("Enter [T] to transfer")
        print("Enter [N] to change name")
        print("Enter [P] to change password")
        print("Enter [L] to logout")
        print()
        time.sleep(0.5)
        
        command = input("Enter [KEY] : ").lower()
        print()
        time.sleep(0.5)
        
        if command == "d":
            deposit(acc)
        elif command == "w":
            withdraw(acc)
        elif command == "t":
            transfer(acc)
        elif command == "n":
            changeName(acc)
        elif command == "p":
            changePass(acc)
        elif command == "l":
            print("Thanks")
            print("Logout successfully")
            print()
            time.sleep(0.5)
            break
        else:
            print(f"You entered wrong key [{command}]")
            print()
            time.sleep(0.5)

# Function to change user's name
def changeName(acc):
    while True:
        print("Change your name")
        print()
        time.sleep(0.5)
        
        fname = input("Enter your new first name : ").title()
        time.sleep(0.3)
        lname = input("Enter your new last name : ").title()
        print()
        time.sleep(0.3)
        
        fname = " ".join(fname.split())
        lname = " ".join(lname.split())
        
        if fname == "":
            print("First name is empty")
            print()
            continue
        else:
            print(f"Your first name is : {fname}")
            time.sleep(0.3)
            print(f"Your last name is : {lname}")
            print()
            time.sleep(0.5)
            
            while True:
                print("Enter [S] to save")
                print("Enter [R] to resubmit")
                print("Enter [C] to cancel")
                print()
                time.sleep(0.5)
                
                command = input("Enter [KEY] : ").lower()
                print()
                time.sleep(0.5)
                
                if command == "s":
                    data[acc][0] = fname
                    data[acc][1] = lname
                    print("Name changed successfully")
                    print()
                    time.sleep(0.5)
                    return
                elif command == "r":
                    changeName(acc)
                    return
                elif command == "c":
                    print("Change name cancelled")
                    print()
                    time.sleep(0.5)
                    return
                else:
                    print(f"You entered wrong key [{command}]")
                    print()
                    time.sleep(0.5)

# Function to change user's password
def changePass(acc):
    while True:
        print("Change your password")
        print("Enter the details below")
        print()
        time.sleep(0.5)
        
        oldPassword = input("Enter current password : ")
        time.sleep(0.3)
        newPassword = input("Enter new password : ")
        time.sleep(0.3)
        cNewPassword = input("Confirm new password : ")
        print()
        time.sleep(0.5)
        
        if oldPassword != data[acc][2]:
            print("Current password is incorrect")
            print()
            time.sleep(0.5)
        elif len(newPassword) < 8:
            print("New password is less than 8 characters")
            print()
            time.sleep(0.5)
        elif newPassword != cNewPassword:
            print("Confirm password didn't match")
            print()
            time.sleep(0.5)
        else:
            data[acc][2] = newPassword
            print("Password changed successfully")
            print()
            time.sleep(0.5)
            break

# Function to deposit money
def deposit(acc):
    amount = int(input("Enter amount to deposit : "))
    print()
    time.sleep(0.5)
    
    if amount > 0:
        data[acc][3] += amount
        print(f"{amount} is credited to your account")
        print()
        time.sleep(0.5)
    else:
        print("Invalid amount")
        print()
        time.sleep(0.5)

# Function to withdraw money
def withdraw(acc):
    amount = int(input("Enter amount to withdraw : "))
    print()
    time.sleep(0.5)
    
    if amount > 0 and data[acc][3] >= amount:
        data[acc][3] -= amount
        print(f"{amount} is debited from your account")
        print()
        time.sleep(0.5)
    elif data[acc][3] < amount:
        print("Insufficient balance")
        print()
        time.sleep(0.5)
    else:
        print("Invalid amount")
        print()
        time.sleep(0.5)

# Function to transfer money to another account
def transfer(acc):
    while True:
        print("Transfer Money")
        print()
        time.sleep(0.5)

        # Get recipient account number and transfer amount
        targetAcc = int(input("Enter recipient account number : "))
        time.sleep(0.3)
        amount = int(input("Enter amount to transfer : "))
        print()
        time.sleep(0.5)

        # Check if recipient account exists
        if targetAcc not in data:
            print("Recipient account not found")
            print()
            time.sleep(0.5)
        # Validate the transfer amount
        elif amount <= 0:
            print("Invalid amount")
            print()
            time.sleep(0.5)
        # Check if the user has sufficient balance
        elif data[acc][3] < amount:
            print("Insufficient balance")
            print()
            time.sleep(0.5)
        # Process the transfer
        else:
            data[acc][3] -= amount
            data[targetAcc][3] += amount
            print(f"{amount} transferred to account {targetAcc}")
            print()
            time.sleep(0.5)
            break

# Main program loop
run = True
while run:
    # Display welcome message and options
    print("Welcome to PyBank")
    print()
    time.sleep(0.5)

    print("Enter [C] to create user")
    print("Enter [L] to login")
    print("Enter [X] to exit")
    print()
    time.sleep(0.5)

    # Get user input
    command = input("Enter [KEY] : ").lower()
    print()
    time.sleep(0.5)

    # Navigate based on user input
    if command == "c":
        createUser()  # Create a new user
        time.sleep(0.5)
    elif command == "l":
        login()  # Login to an existing account
        time.sleep(0.5)
    elif command == "x":
        run = False  # Exit the program
    else:
        print(f"You entered a wrong key [{command}]")
        print()
        time.sleep(0.5)