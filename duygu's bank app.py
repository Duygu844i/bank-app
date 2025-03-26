

# Initialize variables
account_holder = input("Enter your name: ")
balance = 0.0

# Function to display the menu
def display_menu():
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

# Main loop
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${balance:.2f}.")
        else:
            print("Please enter a positive amount.")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${balance:.2f}.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Please enter a positive amount.")

    elif choice == '3':
        print(f"Current balance: ${balance:.2f}.")

    elif choice == '4':
        print("Thank you for using the Bank Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")