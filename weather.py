import random

def adjust_weather():
    """Allows the farmer to set weather conditions."""
    print("\n--- Weather Control Panel ---")
    temperature = float(input("Set Temperature (°C): "))
    rainfall = float(input("Set Rainfall (mm): "))
    wind_speed = float(input("Set Wind Speed (km/h): "))
    
    return {
        "temperature": temperature,
        "rainfall": rainfall,
        "wind_speed": wind_speed
    }

def generate_weather_report(weather):
    """Generates a weather report with farming advice."""
    print("\n--- Weather Report ---")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Rainfall: {weather['rainfall']} mm")
    print(f"Wind Speed: {weather['wind_speed']} km/h")
    
    print("\n--- Farming Advice ---")
    if weather['rainfall'] < 20:
        print("Advice: Consider irrigating your crops.")
    else:
        print("Advice: Sufficient rainfall detected, no irrigation needed.")
    
    if weather['temperature'] > 35:
        print("Warning: High temperature detected, ensure proper shading for crops.")
    elif weather['temperature'] < 10:
        print("Warning: Low temperature detected, consider using protective coverings.")
    
    if weather['wind_speed'] > 50:
        print("Warning: High wind speed detected, secure lightweight plants and equipment.")
    else:
        print("Wind conditions are normal.")

def main():
    print("Welcome to the Smart Weather Control System for Farmers!")
    while True:
        weather = adjust_weather()
        generate_weather_report(weather)
        
        cont = input("Do you want to adjust the weather again? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Exiting Weather Control System. Stay safe!")
            break

if __name__ == "__main__":
    main()
