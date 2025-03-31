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
    def __init__(self):
        self.crops = {}

    def register_crop(self, uname, crop):
        """Registers a new crop for the user."""
        if uname not in self.crops:
            self.crops[uname] = []
        self.crops[uname].append(crop)
        print(f"Crop '{crop.name}' registered successfully.")

    def register_crops_from_input(self, uname):
        """Handles user input to register multiple crops."""
        while True:
            name = input("Enter the crop name (or 'exit' to finish): ")
            if name.lower() == 'exit':
                break
            crop_type = input("Enter the crop type: ")
            area = float(input("Enter the crop area (in square meters): "))
            new_crop = Crop(name, crop_type, area)
            self.register_crop(uname,new_crop)
    def get_crops(self, uname):
           return self.crops.get(uname, [])
    def view_registered_crops(self, uname):
        """Displays all crops registered by a user."""
        crops = self.get_crops(uname)
        if not crops:
            print("No crops registered yet.")
        else:
            print("Registered Crops:")
            for crop in crops:
                print(f"Name: {crop.name}, Type: {crop.crop_type}, Area: {crop.area} sq.m")

    
class Dashboard(Authentication):
    def __init__(self):
        super().__init__()
        
# Testing
if __name__ == "__main__":
    # Example usage:
    #irrigation_system = IrigationControl()

# Simulate user input for starting irrigation, setting duration, and automatic turn off
    #irrigation_system.start_irrigation()

# Monitor status of irrigation
    #irrigation_system.monitor_irrigation_status()
    # weather_info = WeatherInformation()
    # weather_info.display_weather()
# crop monitor
     crop_monitor= CropsControl()
     crop_monitor.register_crops_from_input("Cassie")
     crop_monitor.view_registered_crops("Cassie")

