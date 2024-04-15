class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                if self.inventory[item] == 0:
                    del self.inventory[item]
            else:
                print("Error: Not enough quantity of", item, "in inventory")
        else:
            print("Error: Item", item, "not found in inventory")

    def view_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(item + ":", quantity)


def main():
    pharmacy_inventory = Inventory()

    while True:
        print("\nPharmacy Inventory Management System")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. View current inventory")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            pharmacy_inventory.add_item(item, quantity)
        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            pharmacy_inventory.remove_item(item, quantity)
        elif choice == '3':
            pharmacy_inventory.view_inventory()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()