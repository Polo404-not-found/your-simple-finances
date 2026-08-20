class User:
    def __init__(self):
        self.name = ""
        self.country = ""

    def request_user_data(self):
        print("Please create an Username and enter your residence country.")
        while (True):
            self.name = input("Enter your Username: ").strip()
            self.country = input("Enter your country: ").strip()
            print()
            if not self.name or not self.country:
                print("Please enter valid information")
                print()
            else:
                print(f"Welcome {self.name}")
                print()
                break

    def get_user_data(self) -> str:
        return f"Name: {self.name}, Country: {self.country}"

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}"