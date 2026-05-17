expenses = []

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((item, amount))

        print("Expense Added!")

    elif choice == "2":

        total = 0

        print("\nExpenses List")

        for item, amount in expenses:
            print(item, "-", amount)
            total += amount

        print("Total Expense:", total)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")