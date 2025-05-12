# Let's start by creating a list to store our products' information.
# Each product will be a "dictionary", where we store information with labels (keys) and their value (name, price, quantity).
inventory = []

# Now, let's create 5 initial products in the inventory, as indicated in the exercise.
# We will use the same dictionary structure with the keys 'name', 'price', and 'quantity'.
product_1 = {"name": "tenis", "price": 20.50, "quantity": 10}
product_2 = {"name": "Camisetas", "price": 18.50, "quantity": 5}
product_3 = {"name": "Billeteras", "price": 35.50, "quantity": 3}
product_4 = {"name": "Gorras", "price": 20.20, "quantity": 8}
product_5 = {"name": "Jeans", "price": 55.20, "quantity": 12}

# With .append we add these initial products to our inventory list.
inventory.append(product_1)
inventory.append(product_2)
inventory.append(product_3)
inventory.append(product_4)
inventory.append(product_5)

# --------------------------------------------------------------------------
# 1. Function to add a new product to the inventory.
# --------------------------------------------------------------------------
def add_product() -> None:
    """
    This function allows adding a new product to the inventory.
    It asks the user for the name (str), price (float), and quantity (int) of the product.
    """
    print("\n--- [ Add a New Product to Inventory ]---")
    # We ask the user to enter the name of the new product.
    new_product_name: str = input("Enter the product name: ")
    # We are going to make sure that the price is a positive number.
    while True:
        try:
            new_price_str: str = input("Enter the product price: ")
            new_price: float = float(new_price_str)
            if new_price > 0:
                break
            else:
                print("The price must be a positive number.")
        except ValueError:
            print("Please enter a valid number for the price.")

    # We also make sure that the quantity is a positive integer or zero.
    while True:
        try:
            new_quantity_str: str = input("Enter the available quantity: ")
            new_quantity: int = int(new_quantity_str)
            if new_quantity >= 0:
                break
            else:
                print("The quantity must be a positive number or zero.")
        except ValueError:
            print("Please enter a valid integer for the quantity.")

    # We create a new dictionary {} with the product information.
    new_product = {"name": new_product_name, "price": new_price, "quantity": new_quantity}
    # We add this new dictionary to our inventory list.
    inventory.append(new_product)
    print(f"The product '{new_product_name}' has been added to the inventory.")

# --------------------------------------------------------------------------
# 2. Function to query a product in the inventory by its name.
# --------------------------------------------------------------------------
def query_product() -> None:
    """
    This function allows querying the details of a product in the inventory by its name (str).
    It iterates through the 'inventory' list and displays the name (str),
    price (float), and quantity (int) of the product if found.
    """
    print("\n--- [ Query Product ] ---")
    search_name: str = input("Enter the name of the product you want to search for: ")
    found: bool = False
    # We iterate through each product in our inventory list.
    for product in inventory:
        # We compare the name (str) entered by the user with the name (str) of the current product.
        if product["name"].lower() == search_name.lower():
            # If the names match (ignoring case), we display the product information.
            print(f"name: {product['name']}")
            print(f"Price: ${product['price']:.2f}") # The :.2f is to display the price with two decimal places.
            print(f"Available quantity: {product['quantity']}")
            found = True
            break # If we find the product, we don't need to continue searching.
    # If after checking all the products we don't find the name, we display a message.
    if not found:
        print(f"The product '{search_name}' is not found in the inventory.")

# --------------------------------------------------------------------------
# 3. Function to update the price of a product
# --------------------------------------------------------------------------
def update_price() -> None:
    """
    This function allows updating the price (float) of a product in the inventory.
    It asks the user for the name (str) of the product and the new price (float),
    validates the new price, and updates the price in the corresponding dictionary
    within the 'inventory' list.
    """
    print("\n--- [ Update Product Price ] ---")
    product_to_update: str = input("Enter the name of the product whose price you want to update: ")
    found: bool = False
    # We search for the product by its name (str).
    for product in inventory:
        if product["name"].lower() == product_to_update.lower():
            found = True
            # If we find the product, we ask for the new price (float).
            while True:
                try:
                    new_price_str: str = input("Enter the new price of the product: ")
                    new_price: float = float(new_price_str)
                    if new_price > 0:
                        # We update the price (float) of the product in the dictionary.
                        product["price"] = new_price
                        print(f"The price of '{product['name']}' has been updated to ${new_price:.2f}.")
                        break # We exit the price validation loop.
                    else:
                        print("The price must be a positive number.")
                except ValueError:
                    print("Please enter a valid number for the price.")
            break # We exit the product search loop.
    # If we don't find the product, we display a message.
    if not found:
        print(f"The product '{product_to_update}' is not found in the inventory.")

# --------------------------------------------------------------------------
# 4. Function to delete a product from the inventory
# --------------------------------------------------------------------------
def delete_product() -> None:
    """
    This function allows deleting a product from the inventory.
    It asks the user for the name (str) of the product to delete, searches for the product in the 'inventory' list,
    and, after confirmation (str), deletes it.
    """
    print("\n--- [ Delete product from Inventory ] ---")
    product_to_delete: str = input("Enter the name of the product you want to delete: ")
    found_index: int = -1 # We will use this to remember the position of the product if we find it.

    for index, product in enumerate(inventory):
        if product["name"].lower() == product_to_delete.lower():
            found_index = index
            break # We found the product, we don't need to continue searching.

    # If we find the product, we ask for confirmation (str) before deleting it.
    if found_index != -1:
        confirmation: str = input(f"Are you sure you want to delete '{inventory[found_index]['name']}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            # We delete the product from the list using the index (int) we saved.
            deleted_product: str = inventory.pop(found_index)
            print(f"The product '{deleted_product['name']}' has been deleted from the inventory.")
        else:
            print("The product has not been deleted.")
    else:
        print(f"The product '{product_to_delete}' is not found in the inventory.")

# --------------------------------------------------------------------------
# 5. Function to calculate the total value of the inventory
# --------------------------------------------------------------------------
def calculate_total_value() -> None:
    """
    This function calculates the total value of the inventory.
    It iterates through each product in the 'inventory' list,
    multiplies its price (float) by its quantity (int), and adds it to the total value (float).
    Finally, it displays the total value.
    """
    total_value: float = 0

    for product in inventory:
        # We multiply the price (float) of the product by its quantity (int) and add it to the total value (float).
        total_value += product["price"] * product["quantity"]
    # We display the total value (float) with two decimal places.
    print(f"\nThe total value of the inventory is: ${total_value:.2f}")

def main() -> None:
    """
    Main function that executes the store inventory management menu.
    It displays the options to the user and calls the corresponding functions based on their choice.
    The main loop continues until the user chooses the exit option ('6').
    """
    while True:
        print("\n--- [ Store Inventory Management ] ---")
        print("Select an option:")
        print("1. Add product to inventory")
        print("2. Query product in inventory")
        print("3. Update product price")
        print("4. Delete product from inventory")
        print("5. Calculate the total value of the inventory")
        print("6. Exit")

        option: str = input("Enter the number of the desired option: ")

        if option == '1':
            add_product()
        elif option == '2':
            query_product()
        elif option == '3':
            update_price()
        elif option == '4':
            delete_product()
        elif option == '5':
            calculate_total_value()
        elif option == '6':
            print("Thank you for visiting, come back soon!")
            break # We exit the main loop and the program ends.
        else:
            print("Invalid option. Please try again.")

# This condition ensures that the main() function is executed only when the script is run directly.
if __name__ == "__main__":
    main()
