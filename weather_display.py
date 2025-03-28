#!/usr/bin/env python3

import random

def display_weather():
    """
    Function: Displays simulated weather information for farming decisions.
    """
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy"]
    temperature = random.randint(15, 35)  # Simulating temperature in Celsius
    humidity = random.randint(40, 90)  # Simulating humidity percentage

    print("\n--- Weather Information ---")
    print(f"Condition: {random.choice(weather_conditions)}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print("----------------------------")

def main():
    """
    Main function to display weather information when called.
    """
    print("Welcome to the Farmer's Weather Information System")
    
    while True:
        choice = input("\nDo you want to check the weather? (yes/no): ").strip().lower()
        if choice == "yes":
            display_weather()
        elif choice == "no":
            print("Exiting the system. Have a great day!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()

