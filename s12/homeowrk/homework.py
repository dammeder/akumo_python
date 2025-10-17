product_data = {
    "store": "TechNova",
    "location": {
        "city": "San Francisco",
        "country": "USA"
    },
    "products": [
        {
            "id": "P1001",
            "name": "Wireless Mouse",
            "brand": "LogiTech",
            "price": 29.99,
            "currency": "USD",
            "stock": 134,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "battery_life": "12 months"
            },
            "ratings": {
                "average": 4.5,
                "count": 240
            }
        },
        {
            "id": "P1002",
            "name": "Mechanical Keyboard",
            "brand": "KeyChron",
            "price": 79.99,
            "currency": "USD",
            "stock": 57,
            "specs": {
                "color": "White",
                "switch_type": "Gateron Brown",
                "backlight": "RGB"
            },
            "ratings": {
                "average": 4.7,
                "count": 145
            }
        },
        {
            "id": "P1003",
            "name": "Sony Wireless Noise-Canceling Headphones",
            "brand": "Sony",
            "price": 199.99,
            "currency": "USD",
            "stock": 0,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "noise_cancellation": "Active",
                "battery_life": "30 hours"
            },
            "ratings": {
                "average": 4.8,
                "count": 529
            }
        }
    ]
}

# Task 1: Print this following message by getting values from the dictionary
# Message: Company TechNova is located in San Francisco, USA.

print(f"Company {product_data['store']} is located in {product_data['location']['city']}, {product_data['location']['country']}.")





# Task 2: Print All Out-of-Stock Products
# Use the product_data dictionary and print the names of products that are out of stock (i.e., stock is 0).
# Example Output:
#  Out of stock: Bluetooth Speaker
#  Out of stock: Wireless Charger


for product in product_data.get('products', []):
    if product.get('stock') == 0:
        print(f"Out of stock: {product.get('name')}")




# Task 3: List Products Over $50 with High Rating
# Print the name, price, and average rating of products where the price is greater than $50 and the average rating is above 4.5.
# Example Output:
#  Mechanical Keyboard - $79.99 - Rating: 4.7
#  Noise-Canceling Headphones - $199.99 - Rating: 4.8

for product in product_data.get('products', []):
    avg = product.get('ratings', {}).get('average')

    if product.get('price') > 50 and avg > 4.5:

        print(f"{product.get('name')} - ${product.get('price')} - Rating: {avg} ")
