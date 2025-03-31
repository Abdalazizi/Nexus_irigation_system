class CropsControl:
    def __init__(self):
        self.crops = []
    

    def register_crop(self):
        crop_name = input("Enter the crop name: ").strip()
        if crop_name:
            self.crops.append(crop_name)
            print(f"Crop '{crop_name}' registered successfully!")
        else:
            print("Crop name can't be empty.")
    

    def view_crops(self):
        if self.crops:
            print("\nRegistered Crops:")
            for index, crop in enumerate(self.crops, start=1):
                print(f"{index}. {crop}")
        else:
            print("No crops have been registered yet.")


if __name__ == "__main__":
    crops_control = CropsControl()
    while True:
        action = input("\nDo you want to register a crop or view crops? (register/view/exit): ").strip().lower()
        if action == "register":
            crops_control.register_crop()
        elif action == "view":
            crops_control.view_crops()
        elif action == "exit":
            print("Exiting Crops Management System.")
            break
        else:
            print("Invalid input. Please enter 'Register', 'View', or 'Exit'")
