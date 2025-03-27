
class Authentication:
    users = [
        {
            "name":"twariq",
            "pwd":"123"
        }
    ]
    def __init__(self):
        self.username = None
        self.password = None
        self.logedin = False
    
    def login(self, uname,pwd):
        for user in self.users:
            if user['name'] == uname:
                print(f"Welcome {uname}")
                self.logedin = True
            else:
                print("Wrong username or password")
    def register(self, uname,pwd):
        for user in self.users:
            if user['name'] == uname:
                print(f"user already exist")
                self.logedin = True
            else:
                self.users.append(
                {
                    "name":uname,
                    "pwd":pwd
                }
                )
                print("User created")
    
            # print(user['name'])
test = Authentication()
test.register("twariq123",43)
print(test.users)
