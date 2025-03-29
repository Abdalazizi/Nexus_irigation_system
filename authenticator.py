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
     """Handles weather data generation and display."""
 def __init__(self):
        self.conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy"]
        self.temperature = 0
        self.humidity = 0

    def generate_weather_report(self):
        """Generate random weather data."""
        self.temperature = random.randint(15, 35)  # Simulating temperature in Celsius
        self.humidity = random.randint(40, 90)  # Simulating humidity percentage
        condition = random.choice(self.conditions)

        return {
            "Condition": condition,
            "Temperature": f"{self.temperature}°C",
            "Humidity": f"{self.humidity}%"
        }

    def display_weather(self):
        """Continuously prompt the user to display weather information."""
        print("Welcome to the Farmer's Weather Information System")
        
        while True:
            choice = input("\nDo you want to check the weather? (yes/no): ").strip().lower()
            if choice == "yes":
                weather_report = self.generate_weather_report()
                print("\n--- Weather Information ---")
                for key, value in weather_report.items():
                    print(f"{key}: {value}")
                print("----------------------------")
            elif choice == "no":
                print("Exiting the system. Have a great day!")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    pass
class CropsControl:
    # crops control goes here
    pass
class Dashboard(Authentication):
    def __init__(self):
        super().__init__()
        
# Testing
if __name__ == "__main__":
    weather_info = WeatherInformation()
    weather_info.display_weather()
