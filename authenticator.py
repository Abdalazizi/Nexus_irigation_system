import time
import random
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
        for user in self.users:
            if user['name'] == uname:
                print("User already exists")
                return
        self.users.append({"name": uname, "pwd": str(pwd)})
        print("User created successfully!")

class IrrigationControl:
    def __init__(self):
        self.irrigation_status = False
        self.irrigation_duration = 0

    def turn_on_irrigation(self):
        self.irrigation_status = True
        print("Irrigation turned ON.")

    def turn_off_irrigation(self):
        self.irrigation_status = False
        print("Irrigation turned OFF.")

    def set_irrigation_duration(self):
        try:
            duration = int(input("Enter the irrigation duration (in minutes): "))
            if duration <= 0:
                print("Invalid input. Duration should be greater than 0 minutes.")
            else:
                self.irrigation_duration = duration
                print(f"Irrigation duration set to {self.irrigation_duration} minutes.")
        except ValueError:
            print("Invalid input. Please enter an integer value for duration.")

    def start_irrigation(self):
        user_choice = input("Do you want to turn ON the irrigation? (yes/no): ").strip().lower()
        if user_choice == 'yes':
            self.turn_on_irrigation()
            self.set_irrigation_duration()
            auto_off = input(f"Do you want to automatically turn off irrigation after {self.irrigation_duration} minutes? (yes/no): ").strip().lower()
            if auto_off == 'yes':
                print(f"Watering for {self.irrigation_duration} minutes...")
                time.sleep(self.irrigation_duration * 60)
                self.turn_off_irrigation()
                print("Irrigation has finished.")
            else:
                print("Irrigation is ON. You need to manually turn it off when you are done.")
        elif user_choice == 'no':
            print("Irrigation remains OFF.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    def stop_irrigation(self):
        if self.irrigation_status:
            self.turn_off_irrigation()
        else:
            print("Irrigation is already OFF.")

    def monitor_irrigation_status(self):
        status = "ON" if self.irrigation_status else "OFF"
        print(f"Irrigation status: {status}")

class WeatherInformation:
    def __init__(self):
        self.conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy"]

    def generate_weather_report(self):
        return {
            "Condition": random.choice(self.conditions),
            "Temperature": f"{random.randint(15, 35)}°C",
            "Humidity": f"{random.randint(40, 90)}%"
        }

    def display_weather(self):
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

    
class Crop:
    def __init__(self,name,crop_type,area):
        self.name= name
        self.crop_type= crop_type
        self.area= area

class CropsControl:
    # crops control goes here
    pass
class Dashboard(Authentication):
    def __init__(self):
        super().__init__()
        self.irrigation_system = IrrigationControl()
        self.weather_info = WeatherInformation()
        self.crop_monitor = CropsControl()

    def main_menu(self):
        print("\n===== Smart Farming Dashboard =====")
        while True:
            print("\n1. Register User")
            print("2. Login")
            print("3. Register Crops")
            print("4. View Registered Crops")
            print("5. Start Irrigation")
            print("6. Monitor Irrigation Status")
            print("7. Check Weather Information")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                uname = input("Enter username: ")
                pwd = input("Enter password: ")
                self.register(uname, pwd)
            elif choice == "2":
                uname = input("Enter username: ")
                pwd = input("Enter password: ")
                self.login(uname, pwd)
            elif choice == "3":
                if self.logedin:
                    self.crop_monitor.register_crops_from_input(self.username)
                else:
                    print("You need to log in first!")
            elif choice == "4":
                if self.logedin:
                    self.crop_monitor.view_registered_crops(self.username)
                else:
                    print("You need to log in first!")
            elif choice == "5":
                self.irrigation_system.start_irrigation()
            elif choice == "6":
                self.irrigation_system.monitor_irrigation_status()
            elif choice == "7":
                self.weather_info.display_weather()
            elif choice == "8":
                print("Exiting Smart Farming Dashboard. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 8.")

# Running the dashboard
if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.main_menu()
