import time
import random
import mysql.connector

# Database Configuration
db_config = {
    "host": "c925344929a7.e8a77726.alu-cod.online",
    "user": "Twariq",
    "password": "1234",
    "database": "school",
    "port": 36483,
    "use_pure": True
}

class Database:
    def __init__(self):
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(**db_config)
            self.cursor = self.conn.cursor(dictionary=True)
            print("Database connection successful!")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            self.conn = None

    def execute(self, query, values=None, fetch=False):
        try:
            self.cursor.execute(query, values)
            if fetch:
                return self.cursor.fetchall()
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Query execution error: {err}")

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

class Authentication(Database):
    def __init__(self):
        super().__init__()
        self.username = None
        self.logged_in = False

    def login(self, uname, pwd):
        query = "SELECT * FROM users WHERE name=%s AND pwd=%s"
        user = self.execute(query, (uname, pwd), fetch=True)
        if user:
            print(f"Welcome {uname}")
            self.username = uname
            self.logged_in = True
        else:
            print("Wrong username or password")

    def register(self, uname, pwd):
        query = "SELECT * FROM users WHERE name=%s"
        if self.execute(query, (uname,), fetch=True):
            print("User already exists")
        else:
            self.execute("INSERT INTO users (name, pwd) VALUES (%s, %s)", (uname, pwd))
            print("User created successfully!")

class IrrigationControl(Database):
    def __init__(self):
        super().__init__()
        self.irrigation_status = False
        self.irrigation_duration = 0

    def turn_on_irrigation(self, uname, duration):
        self.irrigation_status = True
        self.irrigation_duration = duration
        self.execute("INSERT INTO irrigation_status (status, duration, name) VALUES (1, %s, %s)", (duration, uname))
        print("Irrigation turned ON for", duration, "minutes.")
        time.sleep(duration * 60)
        self.turn_off_irrigation()

    def turn_off_irrigation(self):
        self.irrigation_status = False
        self.execute("UPDATE irrigation_status SET status=0 WHERE status=1")
        print("Irrigation turned OFF.")

    def monitor_irrigation_status(self):
        status = "ON" if self.irrigation_status else "OFF"
        print(f"Irrigation status: {status}")

class CropsControl(Database):
    def __init__(self):
        super().__init__()

    def register_crop(self, uname, name, crop_type, area):
        self.execute("INSERT INTO crops (user_name, name, crop_type, area) VALUES (%s, %s, %s, %s)", (uname, name, crop_type, area))
        print(f"Crop '{name}' registered successfully.")

    def view_registered_crops(self, uname):
        crops = self.execute("SELECT * FROM crops WHERE user_name=%s", (uname,), fetch=True)
        if not crops:
            print("No crops registered yet.")
        else:
            print("Registered Crops:")
            for crop in crops:
                print(f"Name: {crop['name']}, Type: {crop['crop_type']}, Area: {crop['area']} sq.m")

class Dashboard(Authentication):
    def __init__(self):
        super().__init__()
        self.irrigation_system = IrrigationControl()
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
            print("7. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                uname = input("Enter username: ")
                pwd = input("Enter password: ")
                self.register(uname, pwd)
            elif choice == "2":
                uname = input("Enter username: ")
                pwd = input("Enter password: ")
                self.login(uname, pwd)
            elif choice == "3" and self.logged_in:
                name = input("Enter the crop name: ")
                crop_type = input("Enter the crop type: ")
                area = float(input("Enter the crop area (in sq.m): "))
                self.crop_monitor.register_crop(self.username, name, crop_type, area)
            elif choice == "4" and self.logged_in:
                self.crop_monitor.view_registered_crops(self.username)
            elif choice == "5" and self.logged_in:
                duration = int(input("Enter irrigation duration (minutes): "))
                self.irrigation_system.turn_on_irrigation(self.username, duration)
            elif choice == "6":
                self.irrigation_system.monitor_irrigation_status()
            elif choice == "7":
                print("Exiting Smart Farming Dashboard. Goodbye!")
                break
            else:
                print("Invalid choice or login required!")

# Running the dashboard
if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.main_menu()
