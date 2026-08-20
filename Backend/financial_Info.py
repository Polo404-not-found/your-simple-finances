import pandas as pd


class FinancialData:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Type", "Amount", "Description"])
        self.type = ""
        self.amount = 0.0
        self.description = ""
        self.income = 0.0
        self.outcome = 0.0
        self.total = 0.0    
        self.processed_data = 0

    def get_data(self): 
        print("---Initializing---")
        while(True):
            try:
                print("Select one option:")
                print("1. Income\n2. Outcome\n3. Cancel")
                selection = int(input("Choose your option: "))
                if selection == 3:
                    print("Operation cancelled.")
                    print()
                    return None
                if selection not in [1,2]:
                    print("Not valid selection")
                    print()
                    continue 
            except ValueError:
                print("Please use only the numbers provided")
                print()
                continue 
            self.type = "Income" if selection == 1 else "Outcome"
            while (True):
                try:
                    raw_amount = input(f"Enter your {self.type} amount: ").strip()
                    raw_amount = raw_amount.replace(',','.')
                    self.amount = float(raw_amount)
                    if self.amount < 0.0:
                        print("The amount can't be negative")
                        print()
                        continue
                    break
                except ValueError:
                    print("Error, Amount must be a number")
                    print()
            while (True):
                self.description = input("Enter your description: ").strip()
                if not self.description:
                    print("Description can't be empty")
                    print()
                    continue
                else:
                    print("Data added.")
                    print()
                    break
            return {
                "Type": self.type,
                "Amount": self.amount,
                "Description": self.description
                }

    def add_dataframe(self):
        new_data = self.get_data()
        if new_data is None:
            return 
        new_row_df = pd.DataFrame([new_data])
        self.df = pd.concat([self.df, new_row_df], ignore_index = True)

    def calculate_data(self):
        if self.df.empty:
            print("There's no information to print")
            print()
            return 
        else:
            print("\n--Calculating---")
            self.income = self.df[self.df['Type'] == 'Income']['Amount'].sum()
            self.outcome = self.df[self.df['Type'] == 'Outcome']['Amount'].sum()
            print(f"Your total income is: {self.income}")
            print(f"Your total outcome is: {self.outcome}")
            self.total = self.income - self.outcome
            print(f"Your balance is: {self.total}")
            print()

    def print_data(self):
        if self.df.empty:
            print("No data to print..")
            print()
            return 
        else:
            print("Loading data...")
            print("Your data: ")
            print(self.df.to_string(index = False))
            print()