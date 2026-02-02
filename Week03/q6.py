# Question 6: Inventory System
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8),
}

print("=== Current Inventory ===")
for product, details in inventory.items():
    print(f"{product} - Price: ${details[0]}, Quantity: {details[1]}")

# Sets for categories
electronics = {"Laptop","Monitor"}
accessories = {"Mouse","Keyboard"}
all_products = electronics | accessories  # Union of both sets
print(f"\nAll Products Categories: {all_products}") 

# Extracting prices into a list
price_list = [details[0] for details in inventory.values()]
price_list.sort()
print(f"\nSorted prices: {price_list}")
print(f"Lowest pirce: ${price_list[0]}")
print(f"Highest price: ${price_list[-1]}")

# Modifications
inventory["Headphones"] = (49.99, 20)  # Adding new product
inventory["Mouse"] = (29.99, 12) # Updating quantity
del inventory["Monitor"]  # Deleting monitor

print("\n=== Final Inventory ===")
for product, details in inventory.items():
    print(f"{product} - Price: ${details[0]}, Quantity: {details[1]}")  