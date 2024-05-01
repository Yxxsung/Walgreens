#imports added by Sophia 04/30/2024
import inventory
import POS 
import UIWalgreens



class Inventory:
    def __init__(self):
        # Initialize an empty dictionary to store inventory items and their quantities
        self.inventory = {}

    def add_item(self, item, quantity):
        # Add a specified quantity of an item to the inventory
        if item in self.inventory:
            # If the item already exists in the inventory, increase its quantity
            self.inventory[item] += quantity
        else:
            # If the item is not already in the inventory, add it with the specified quantity
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        # Remove a specified quantity of an item from the inventory
        if item in self.inventory:
            # If the item exists in the inventory
            if self.inventory[item] >= quantity:
                # If the quantity to remove is less than or equal to the current quantity of the item
                self.inventory[item] -= quantity
                if self.inventory[item] == 0:
                    # If the quantity becomes zero after removal, delete the item from the inventory
                    del self.inventory[item]
            else:
                # If the specified quantity to remove exceeds the current quantity of the item
                print("Error: Not enough quantity of", item, "in inventory")
        else:
            # If the item is not found in the inventory
            print("Error: Item", item, "not found in inventory")

    def view_inventory(self):
        # Display the current inventory items and their quantities
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(item + ":", quantity)


def main():
    # Create an instance of the Inventory class
    pharmacy_inventory = Inventory()

    while True:
        # Display the main menu for the inventory management system
        print("\nPharmacy Inventory Management System")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. View current inventory")
        print("4. Exit")

        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # If the user chooses to add an item to the inventory
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            pharmacy_inventory.add_item(item, quantity)
        elif choice == '2':
            # If the user chooses to remove an item from the inventory
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            pharmacy_inventory.remove_item(item, quantity)
        elif choice == '3':
            # If the user chooses to view the current inventory
            pharmacy_inventory.view_inventory()
        elif choice == '4':
            # If the user chooses to exit the program
            print("Exiting program...")
            break
        else:
            # If the user enters an invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Call the main function when the script is executed
    main()