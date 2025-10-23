# Task 1:
# Create a function calculate_final_price(price, tax_rate=0.07, discount=0.10) that:
#  - Returns the final price after both operations (tax first, then discount)

# Output:
# calculate_final_price(100) == 96.3
# calculate_final_price(200, 0.08) == 192.6


def calculate_final_price(price, tax_rate=0.07, discount=0.10):
    price_tax = price + (price * tax_rate)
    final_price = price_tax - (price_tax * discount)

    return round(final_price, 2)

print(calculate_final_price(59.99))






# Task 2:
# Create a function create_email(name, domain="example.com") that:
# - Defines an inner function sanitize_name() that:
#     - Converts the name to lowercase
#     - Replaces spaces with dots
#   Returns the final email.

# Example:
# print(create_email("Jon Doe"))         # "jon.doe@example.com"

def create_email(name, domain="gmail.com"):
    def sanitize_name():
        return name.lower().replace(' ', '.')

    return (f"{sanitize_name()}@{domain}")

print(create_email("Meder Emilev"))


