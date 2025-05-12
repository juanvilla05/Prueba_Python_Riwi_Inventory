# 🛍️ Store Inventory Management System 🚀

Welcome to your store's inventory management system! 📦 This Python program allows you to keep detailed track of your products, from adding them to calculating the total value of your stock. Let's get started!

## ⚙️ Execution Instructions

To run this system, follow these simple steps:

1.  **💾 Save the code:** Make sure you have saved the Python code in a file. You can name it, for example, `inventory.py`.
2.  **🐍 Open your terminal or command prompt:** Navigate to the directory where you saved the `inventory.py` file.
3.  **🚀 Run the program:** Type the following command and press Enter:

    ```bash
    python inventory.py
    ```

    You will see the main menu appear! 🎉

## 📝 Example of Input and Output Data

Here's a glimpse of how the program interacts:

**Adding a new product:**

--- [ Add a New Product to Inventory ]---
Enter the product name: New Product
Enter the product price: 25.99
Enter the available quantity: 50
The product 'New Product' has been added to the inventory.


**Querying a product:**

--- [ Query Product ] ---
Enter the name of the product you want to search for: tenis
name: tenis
Price: $20.50
Available quantity: 10


**Updating the price of a product:**

--- [ Update Product Price ] ---
Enter the name of the product whose price you want to update: Camisetas
Enter the new price of the product: 19.99
The price of 'Camisetas' has been updated to $19.99.


**Deleting a product:**

--- [ Delete product from Inventory ] ---
Enter the name of the product you want to delete: Billeteras
Are you sure you want to delete 'Billeteras'? (yes/no): yes
The product 'Billeteras' has been deleted from the inventory.


**Calculating the total value of the inventory:**

--- [ Store Inventory Management ] ---
Select an option:
5. Calculate the total value of the inventory

The total value of the inventory is: $1735.70


**Exiting the program:**

--- [ Store Inventory Management ] ---
Select an option:
6. Exit
Thank you for visiting, come back soon!


## ✨ Main Features

This inventory management system offers the following essential functionalities:

1.  **➕ Add Product:** Allows adding new items to the inventory, requesting their name, price, and available quantity. Keep your catalog always up-to-date! 🆕
2.  **🔍 Query Product:** Searches for a product by its name and displays its details: name, price, and quantity in stock. Find information instantly! 🔎
3.  **💰 Update Price:** Modifies the price of an existing product in the inventory. Keep your prices current! 🏷️
4.  **🗑️ Delete Product:** Removes a product from the inventory. When an item is no longer available! 💨
5.  **📊 Calculate Total Value:** Calculates the total economic value of all products in the inventory. A clear view of your capital! 📈
6.  **🚪 Exit:** Closes the program safely. Until the next management session! 👋

## 🧱 Program Structure

The program is organized as follows:

* **`inventory` (list):** A list that acts as the database for our products. Each product is stored as a dictionary. 📒
* **Product Dictionaries:** Each product in the `inventory` list is a dictionary with the following keys:
    * `"name"` (str): The name of the product.
    * `"price"` (float): The unit price of the product.
    * `"quantity"` (int): The quantity available in stock.
* **Functions:** The program is divided into functions to modularize the different actions:
    * `add_product()`: Adds a new product to the inventory.
    * `query_product()`: Searches for and displays the information of a product.
    * `update_price()`: Modifies the price of a product.
    * `delete_product()`: Removes a product from the inventory.
    * `calculate_total_value()`: Calculates the total value of the inventory.
    * `main()`: The main function that contains the user interaction menu and calls the other functions.

## 🧠 Logic and Functioning

The program's logic focuses on manipulating the `inventory` list.

* **Add:** A new dictionary is created with the information provided by the user and added to the `inventory` list using `.append()`.
* **Query:** The `inventory` list is iterated over. For each product, the name entered by the user is compared (case-insensitive) with the product's name. If they match, the information is displayed.
* **Update:** Similar to querying, the product is searched for by name. Once found, the new price is requested, and the value is updated in the product's dictionary.
* **Delete:** The product is searched for by name, and its index in the list is stored. The user is asked for confirmation before removing the element from the list using `.pop()` with the stored index.
* **Calculate Total Value:** The `inventory` list is traversed. For each product, its price is multiplied by its quantity, and the result is added to an accumulator. Finally, the total is displayed.
* **Main Menu:** The `main()` function presents a `while` loop that displays the options to the user and executes the corresponding function based on their choice. The loop breaks when the user chooses the exit option.

I hope this README guides you and is very useful to understand the functions and structure of the store! 😊
