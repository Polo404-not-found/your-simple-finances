from Backend.AI_Client import AIClient
from Backend.financial_Info import FinancialData


class main:
    def __init__(self, user):
        self.is_running = True
        self.data = FinancialData()
        self.user = user
        self.ai = AIClient(user = self.user, financial_data = self.data)
    
    def get_menu(self):
        print("Select your option")
        while (self.is_running):
            try: 
                print("1. Add data")
                print("2. Calculate data")
                print("3. Print data")
                print("4. AI")
                print("5. Close")
                i = int(input("Your selection: "))
                print()
                if 1 <= i <= 5:
                    if i == 1:
                        self.data.add_dataframe()
                    elif i == 2:
                        self.data.calculate_data()
                    elif i == 3:
                        self.data.print_data()
                    elif i == 4:
                        self.ai.get_api_key()
                        self.ai.ai_chat()
                    elif i == 5:
                        print("Closing...")
                        self.is_running = False
                else:
                    print("Choose a valid option.")
                    continue
            except ValueError:
                print("Use a valid number")