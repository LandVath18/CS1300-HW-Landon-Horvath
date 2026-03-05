# campus_cafe.py
# Menu-driven campus café ordering system

TAX_RATE = 0.07

print("==============================")
print("CAMPUS CAFÉ ORDER SYSTEM")
print("==============================")
print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo - $8.00")
print("5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ")

item_name = ""
unit_price = 0

# ----- Coffee -----
if choice == "1":
    size = input("Choose size (small/medium/large): ").lower()

    if size == "medium":
        unit_price = 4.50
        item_name = "Coffee (Medium)"
    elif size == "large":
        unit_price = 5.50
        item_name = "Coffee (Large)"
    else:
        print("Invalid size. Defaulting to Small.")
        unit_price = 3.50
        item_name = "Coffee (Small)"

# ----- Sandwich -----
elif choice == "2":
    unit_price = 6.00
    cheese = input("Add cheese? (yes/no): ").lower()

    if cheese == "yes":
        unit_price += 0.75
        item_name = "Sandwich + Cheese"
    else:
        item_name = "Sandwich"

# ----- Salad -----
elif choice == "3":
    unit_price = 5.50
    dressing = input(
        "Choose dressing (ranch/italian/vinaigrette/none): "
    ).lower()

    valid = ["ranch", "italian", "vinaigrette", "none"]

    if dressing not in valid:
        print("Invalid dressing. Defaulting to none.")
        dressing = "none"

    item_name = f"Salad ({dressing})"

# ----- Combo -----
elif choice == "4":
    unit_price = 8.00

    size = input("Coffee size (small/medium/large): ").lower()
    if size == "medium":
        unit_price += 1.00
    elif size == "large":
        unit_price += 2.00

    cheese = input("Add cheese? (yes/no): ").lower()
    if cheese == "yes":
        unit_price += 0.75
        item_name = "Combo + Cheese"
    else:
        item_name = "Combo"

elif choice == "5":
    print("Goodbye!")
    exit()

else:
    print("Invalid menu choice.")
    exit()

# ----- Customer Name -----
name = input("Enter your name: ").strip()
if name == "":
    print("Name cannot be empty.")
    exit()

# ----- Quantity Validation -----
try:
    quantity = int(input("How many? "))
    if quantity <= 0:
        print("Quantity must be positive.")
        exit()
except:
    print("Invalid quantity.")
    exit()

# ----- Calculations -----
subtotal = unit_price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# ----- Receipt -----
print("==============================")
print("ORDER RECEIPT")
print("==============================")
print(f"Customer: {name}")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("==============================")
print("Thank you for your order!")
