class BankAccount:
    def __init__(self, account_number: int, balance: float):
        # Initialize private attributes using double underscores
        self.__account_number = account_number
        self.__balance = 0.0
        
        # Use the setter to apply validation during initialization
        self.set_balance(balance)

    # --- Public Setter Methods ---
    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def set_balance(self, balance: float):
        # Validation: check if the balance is negative
        if balance < 0:
            print("Warning: Balance cannot be negative. Operation ignored.")
        else:
            self.__balance = float(balance)

    # --- Public Getter Methods using @property decorator ---
    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def balance(self) -> float:
        return self.__balance

# --- Instantiating and utilizing the object ---
# Creating the object using sample values
a1 = BankAccount(12345, 1000)

# Displaying the output in the requested format
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")  # Formatted to 2 decimal places
