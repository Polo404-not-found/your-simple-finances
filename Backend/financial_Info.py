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

    def add_dataframe(self, new_transaction):
        new_row_df = pd.DataFrame([new_transaction], columns=["Type", "Amount", "Description"])
        self.df = pd.concat([self.df, new_row_df], ignore_index=True)

    def calculate_data(self):
            self.income = self.df[self.df['Type'] == 'Income']['Amount'].sum()
            self.outcome = self.df[self.df['Type'] == 'Outcome']['Amount'].sum()
            self.total = self.income - self.outcome
