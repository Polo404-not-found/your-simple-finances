from Backend.main import main
from Backend.user_Info import User


def app():
    print("---Your Simple Finance---")
    information = User()
    run = main(user = information)
    information.request_user_data()
    run.get_menu()
    
    
if __name__ == "__main__":
    app()