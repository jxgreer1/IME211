# ----------------------------------------------------
# Final Exam: Grocery Store Inventory
# ----------------------------------------------------

# Inventory list
inventory = [
    {"item": "Apple", "quantity": 50, "price_per_unit": 0.5},
    {"item": "Banana", "quantity": 100, "price_per_unit": 0.2},
    {"item": "Orange", "quantity": 75, "price_per_unit": 0.3},
    {"item": "Milk", "quantity": 30, "price_per_unit": 1.5},
    {"item": "Eggs", "quantity": 200, "price_per_unit": 0.1},
    {"item": "Bread", "quantity": 40, "price_per_unit": 2.0},
]

# TODO 1: Calculate the total value of stock in inventory and save as total_value
for stock in inventory:
    quantity = stock["quantity"]
    ppu = stock["price_per_unit"]
    stockvalues= (quantity * ppu)
    #print(stockvalues)

# TODO 2: Update the quantity of an item in the inventory by collecting the item name and amount by which to
#  change the existing quantity

item_name = input("Enter the item name to update: ")
change = int(input("Enter the amount to add or subtract from the quantity (use negative for subtraction): "))

for item in inventory:
    if item["item"] == item_name:
        item ["quantity"] += change

# TODO 3: Add a new item to the inventory by collecting the item name, quantity, and price from the user
ItemName = input("Please input the Item you wish to add:")
ItemQuantity = input("Please input the quantity you wish to add:")
ItemPrice = input("Please input the Price you wish to add:")

print(f"{ItemName} has been added to your list")

# TODO 4: Display a printout in the following format:
#  Current Inventory:
#  Apple - 50
#  Banana - 100
print("Current Inventory:")
for item in inventory:
    print(f"{item['item']} - {item['quantity']}")
print(f"{ItemName} - {ItemQuantity}")
