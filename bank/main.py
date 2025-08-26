from colorama import init, Fore, Style
import pyfiglet
import getpass

init(autoreset=True)

accounts = {}

def display_heading():
    print(Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("My Bank", font="slant"))

def display_menu():
    print(Fore.YELLOW + Style.BRIGHT + "\n=== MENU OPTIONS ===")
    print(Fore.GREEN + Style.BRIGHT + "1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")
    print(Fore.YELLOW + "=" * 22)

def create_account():
    acc_no = input(Fore.CYAN + "Enter account number: ")
    if acc_no in accounts:
        print(Fore.RED + "Account already exists.")
        return
    name = input(Fore.CYAN + "Enter account holder's name: ")
    password = getpass.getpass(Fore.CYAN + "Set a password for the account: ")
    try:
        balance = float(input(Fore.CYAN + "Enter initial deposit amount: "))
    except ValueError:
        print(Fore.RED + "Invalid amount.")
        return
    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "password": password
    }
    print(Fore.GREEN + "✅ Account created successfully.")

def verify_password(acc_no):
    password = getpass.getpass(Fore.MAGENTA + "Enter your password: ")
    if accounts[acc_no]["password"] == password:
        return True
    else:
        print(Fore.RED + "Incorrect password.")
        return False

def deposit():
    acc_no = input(Fore.CYAN + "Enter account number: ")
    if acc_no not in accounts:
        print(Fore.RED + "Account not found.")
        return
    if not verify_password(acc_no):
        return
    try:
        amount = float(input(Fore.CYAN + "Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print(Fore.GREEN + "💰 Deposit successful.")
    except ValueError:
        print(Fore.RED + "Invalid amount.")

def withdraw():
    acc_no = input(Fore.CYAN + "Enter account number: ")
    if acc_no not in accounts:
        print(Fore.RED + "Account not found.")
        return
    if not verify_password(acc_no):
        return
    try:
        amount = float(input(Fore.CYAN + "Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print(Fore.GREEN + "💸 Withdrawal successful.")
        else:
            print(Fore.RED + "Insufficient balance.")
    except ValueError:
        print(Fore.RED + "Invalid amount.")

def check_balance():
    acc_no = input(Fore.CYAN + "Enter account number: ")
    if acc_no in accounts:
        if verify_password(acc_no):
            data = accounts[acc_no]
            print(Fore.BLUE + f"👤 Account Holder: {data['name']}, 💰 Balance: {data['balance']}")
    else:
        print(Fore.RED + "Account not found.")

def view_all_accounts():
    if not accounts:
        print(Fore.YELLOW + "No accounts to show.")
        return
    print(Fore.BLUE + "\n--- All Accounts ---")
    for acc_no, info in accounts.items():
        print(Fore.LIGHTWHITE_EX + f"Acc No: {acc_no}, Name: {info['name']}, Balance: {info['balance']}")

def main():
    while True:
        display_heading()
        display_menu()
        choice = input(Fore.LIGHTMAGENTA_EX + "Enter your choice (1-6): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_all_accounts()
        elif choice == "6":
            print(Fore.GREEN + "\nThank you for using our banking system! Goodbye.\n")
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")

if __name__ == "__main__":
    main()
