# Nexus irrigation system

## Overview
This project is a **Nexus irrigation system** that helps farmers manage their crops, irrigation system, and get weather updates. The system includes features like user registration, crop management, irrigation control, and weather information.

## Features

1. **User Registration and Login**: 
   - Farmers can register as new users or log in to an existing account to access the dashboard.
   
2. **Crop Management**:
   - Farmers can register new crops by entering the crop name, type, and area.
   - They can also view all crops they've registered.
   
3. **Irrigation Control**:
   - Farmers can turn the irrigation system on or off.
   - They can also set the irrigation duration and decide whether it should turn off automatically after a certain period.

4. **Weather Information**:
   - The system generates a random weather report showing the weather condition, temperature, and humidity.

## Getting Started

### Requirements
To use this system, you need Python installed on your machine.

### How to Run the Code

1. **Clone or Download the Code**:
   - Download or clone the project files to your local machine.

2. **Run the Program**:
   - Open your terminal (or command prompt).
   - Navigate to the directory where the project is stored.
   - Run the program by typing: `python <filename>.py`.

3. **Follow the Menu Options**:
   - Once the program is running, you’ll see a menu with different options. Simply follow the instructions on the screen.

### Example of Features:
- **Registering a User**:
   - Choose option 1 and enter a username and password.
   
- **Logging In**:
   - Choose option 2 and enter your username and password to log in.
   
- **Managing Crops**:
   - Once logged in, choose option 3 to register a new crop, or choose option 4 to view your registered crops.

- **Controlling Irrigation**:
   - Choose option 5 to start irrigation. You can set the duration and decide if it should turn off automatically after the specified time.
   - Option 6 allows you to monitor irrigation status.

- **Getting Weather Information**:
   - Choose option 7 to get a weather report.

## Structure of the Code

The system consists of the following classes:

1. **Authentication**:
   - Handles user registration and login.

2. **IrrigationControl**:
   - Manages the irrigation system (turning on/off, setting duration, etc.).

3. **WeatherInformation**:
   - Generates random weather reports.

4. **Crop**:
   - Represents a crop with a name, type, and area.

5. **CropsControl**:
   - Manages the registration and viewing of crops.

6. **Dashboard**:
   - The main dashboard where users interact with the system.

## Notes

- This project is designed to simulate a farming dashboard and is intended for educational or demonstration purposes.
- The weather information and other actions like irrigation control are simulated for the purpose of this system.
  
## License
This project is open-source. Feel free to use or modify it!
