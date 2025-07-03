#programme for  shopping cart

foods  =[]
prices =[]
total = 0.0
print("Welcome to the shopping cart program!")
while True:
 
    food  = input ("Enter the food item you want to add (or type 'q' to exit): ")
    if food.lower() == 'q':
        break
    price = input("Enter the price of the food item: ")
    try:
        price = float(price)
        foods.append(food)
        prices.append(price)
        print(f"{food} has been added to the cart at ${price:.2f}.")
    except ValueError:
        print("Invalid price. Please enter a valid number.")


print("\nYour shopping cart contains:")
for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")  

total = sum(prices)    
print(f"\nTotal cost of items in the cart: ${total:.2f}")  


