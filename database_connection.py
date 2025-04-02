import mysql.connector
import json
class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            # Load database configuration from config.json
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
            self.conn = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )
            self.cursor = self.conn.cursor()
            print("Database connection established.")
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            self.conn = None
            self.cursor = None

    def reconnect_if_needed(self):
        if not self.conn or not self.conn.is_connected():
            print("Reconnecting to database...")
            self.connect()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
