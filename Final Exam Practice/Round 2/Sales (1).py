# ----------------------------------------------------
# Final Exam Variant 3: E-commerce Sales Tracker (Solution)
# ----------------------------------------------------

# Product catalog and sales data
product_catalog = {
    "P001": {"name": "Laptop", "price": 1200.00},
    "P002": {"name": "Smartphone", "price": 800.00},
    "P003": {"name": "Headphones", "price": 150.00},
    "P004": {"name": "Monitor", "price": 300.00},
    "P005": {"name": "Keyboard", "price": 50.00},
    "P006": {"name": "Mouse", "price": 25.00},
    "P007": {"name": "Printer", "price": 200.00},
}

sales_data = [
    {"product_id": "P001", "quantity": 3},
    {"product_id": "P002", "quantity": 5},
    {"product_id": "P003", "quantity": 10},
    {"product_id": "P004", "quantity": 2},
    {"product_id": "P005", "quantity": 8},
    {"product_id": "P006", "quantity": 15},
    {"product_id": "P007", "quantity": 1},
]

# TODO 1: Calculate and print the total amount of money made from sales


# TODO 2: Prompt user for a product ID and reprompt them for a product ID if the ID
#  they provide is not in the product catalog. Store as product_ID


# TODO 3: Increase the quantity of the previously provided product_ID by 1 in the sales_data


# TODO 4: Produce a printout in the following format:
#  Total Value Sold per Product:
#  Laptop: $3600
