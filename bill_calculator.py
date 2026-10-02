# Simple Bill Calculator

try:
    price = float(input("Enter the price of one item: "))
    quantity = int(input("Enter the quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    total = price * quantity

    print("\n----- BILL SUMMARY -----")
    print(f"{quantity} items at {price:.2f} each = {total:.2f}")
    print("------------------------")
    print(f"Your total bill is: {total:.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")