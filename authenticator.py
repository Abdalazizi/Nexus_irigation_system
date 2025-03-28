class Authentication:
    users = []

    def __init__(self):
        self.username = None
        self.password = None
        self.logedin = False

    def login(self, uname, pwd):
        for user in self.users:
            if user['name'] == uname and user['pwd'] == str(pwd):
                print(f"Welcome {uname}")
                self.logedin = True
                return 
        print("Wrong username or password")

    def register(self, uname, pwd):
        # Check if user already exists
        for user in self.users:
            if user['name'] == uname:
                print("User already exists")
                return
        # Add new user
        self.users.append({
            "name": uname,
            "pwd": str(pwd)
        })
        print("User created successfully!")
class IrigationControl:
    # all irigation logic must be here 
    pass
class WeatherInformation:
    # all weather info goes herre
    pass
class CropsControl:
    # crops control goes here
    pass
class Dashboard(Authentication):
    def __init__(self):
        super().__init__()
        
# Testing
