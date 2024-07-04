class BankAccountManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self._create_file_if_not_exist()

    def _create_file_if_not_exist(self):
        
        try:
            with open(self.file_name, 'x'):
                pass  
        except FileExistsError:
            pass  

    def get_balance(self, account_number):
        
        account_info = self._read_accounts()
        if account_number in account_info:
            return account_info[account_number]
        else:
            print(f"Account {account_number} not found.")
            return None

    def deposit(self, account_number, amount):
        
        account_info = self._read_accounts()
        if account_number in account_info:
            current_balance = account_info[account_number]
            new_balance = current_balance + amount
            account_info[account_number] = new_balance
            self._update_account(account_number, new_balance, f"deposit -> {amount}", f"Total -> {new_balance}")
            print(f"Deposited {amount} into account {account_number}. New balance: {new_balance}")
        else:
            print(f"Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        
        account_info = self._read_accounts()
        if account_number in account_info:
            current_balance = account_info[account_number]
            if current_balance >= amount:
                new_balance = current_balance - amount
                account_info[account_number] = new_balance
                self._update_account(account_number, new_balance, f"withdraw -> {amount}", f"Total -> {new_balance}")
                print(f"Withdrew {amount} from account {account_number}. New balance: {new_balance}")
            else:
                print(f"Insufficient balance in account {account_number}.")
        else:
            print(f"Account {account_number} not found.")

    def update_account(self, account_number, balance):
        
        self._update_account(account_number, balance, "update", f"Total -> {balance}")

    def _read_accounts(self):
        
        account_info = {}
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.strip():  
                        parts = line.strip().split(',')
                        if len(parts) >= 2:
                            account_number = parts[0]
                            balance = float(parts[1])
                            account_info[account_number] = balance
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
        except IOError:
            print(f"Error: Could not read from file '{self.file_name}'.")
        return account_info

    def _update_account(self, account_number, balance, action, total_message):
        
        try:
            with open(self.file_name, 'a') as file:
                file.write(f"{account_number},{balance},{action},{total_message}\n")
        except IOError:
            print(f"Error: Could not write to file '{self.file_name}'.")

file_name = 'accounts.txt'
bank_manager = BankAccountManager(file_name)

print("Balance of account 'A123':", bank_manager.get_balance('A123'))

bank_manager.deposit('A123', 500.0)
print("Updated balance of account 'A123':", bank_manager.get_balance('A123'))

bank_manager.withdraw('A123', 200.0)
print("Updated balance of account 'A123':", bank_manager.get_balance('A123'))

bank_manager.update_account('A123', 1500.0)
print("Updated balance of account 'A123':", bank_manager.get_balance('A123'))
