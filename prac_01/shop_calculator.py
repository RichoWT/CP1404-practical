total_price = 0
DISCOUNT = 0.9
DISCOUNT_THRESHOLD = 100
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item
if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price * DISCOUNT
print(f"Total price for {number_of_items} items is ${total_price:.2f}")