print("welcome to pizza delivery system")
print("\n menu")
print("1. margarite $5")
print("2. veggie $7")
print("3. pepporoni $8")
price=0
pizza_choice =int(input("Enter the no.of pizza choice"))
quantity=int(input("Enter the quantity"))
if pizza_choice==1:
    price=5
elif pizza_choice==2:
    price=7
elif pizza_choice==3:
    price=8
else:
    print("Enter valid choice")
if price!=0:
    total_price=price*quantity
print(f"total_price is {total_price}")


