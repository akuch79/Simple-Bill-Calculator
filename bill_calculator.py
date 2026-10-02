
# Simple Bill Calculator

# Ask the user for input
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

# Calculate the total
total = price * quantity

# Display the result using an f-string
print("\n----- BILL SUMMARY -----")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
print("------------------------")
print(f"Your total bill is: {total:.2f}")