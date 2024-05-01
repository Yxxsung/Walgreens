import tkinter as tk

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Walgreens POS")

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.root, padx=20, pady=20)
        self.button_frame.pack()

        # Add Item Button
        self.add_button = tk.Button(self.button_frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        # Remove Item Button
        self.remove_button = tk.Button(self.button_frame, text="Remove Item", command=self.remove_item)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        # View Inventory Button
        self.view_button = tk.Button(self.button_frame, text="View Inventory", command=self.view_inventory)
        self.view_button.grid(row=0, column=2, padx=5, pady=5)

        # Exit Button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=root.quit)
        self.exit_button.grid(row=0, column=3, padx=5, pady=5)

    def add_item(self):
        # Function to handle adding an item to the inventory
        # Implement your logic here
        print("Add Item functionality goes here")

    def remove_item(self):
        # Function to handle removing an item from the inventory
        # Implement your logic here
        print("Remove Item functionality goes here")

    def view_inventory(self):
        # Function to handle viewing the inventory
        # Implement your logic here
        print("View Inventory functionality goes here")


def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()