print("\nCAMPUS CAFÉ ORDER SYSTEM")
print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo - $8.00")
print("5. Exit")

choice = input("Enter choice (1-5): ")

price = 0
item = ""

# ----- MENU -----
if choice == "1":
    size = input("Size (small/medium/large): ").lower()
    if size == "medium":
        price = 4.50
        item = "Coffee Medium"
    elif size == "large":
        price = 5.50
        item = "Coffee Large"
    else:
        print("Invalid size → Small used")
        price = 3.50
        item = "Coffee Small"

elif choice == "2":
    price = 6.00
    item = "Sandwich"
    if input("Add cheese? (yes/no): ").lower() == "yes":
        price += 0.75
        item += " + Cheese"

elif choice == "3":
    price = 5.50
    dress = input(
        "Dressing (ranch/italian/vinaigrette/none): "
    ).lower()
    if dress not in ["ranch","italian","vinaigrette","none"]:
        print("Invalid → none used")
        dress = "none"
    item = f"Salad ({dress})"

elif choice == "4":
    price = 8.00
    item = "Combo"

    size = input("Coffee size: ").lower()
    if size == "medium":
        price += 1
    elif size == "large":
        price += 2

    if input("Add cheese? ").lower() == "yes":
        price += 0.75
        item += " + Cheese"

else:
    print("Goodbye")
    exit()

# ----- NAME -----
name = input("Enter name: ").strip()
while name == "":
    name = input("Name cannot be empty: ")

# ----- QUANTITY -----
while True:
    try:
        qty = int(input("How many? "))
        if qty > 0:
            break
    except:
        pass
    print("Enter a valid number")

# ----- TOTAL -----
subtotal = price * qty
tax = subtotal * 0.07
total = subtotal + tax

print("\n===== ORDER RECEIPT =====")
print("Customer:", name)
print("Item:", item)
print("Quantity:", qty)
print(f"Unit Price: ${price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("=========================")