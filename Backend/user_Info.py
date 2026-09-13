class User:
    def __init__(self):
        self.name = ""
        self.country = ""

    def __str__(self):
        return f"User: {self.name}, Country: {self.country}"