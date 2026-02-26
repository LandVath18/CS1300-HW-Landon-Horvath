15
age_input = input("Enter your age: ")

try:
    age = int(age_input)
    if age < 0:
        print("Error: Age cannot be negative.")
    else:
        matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()
        is_matinee = True if matinee_input == "yes" else False
    
        if age < 13:
            age_group = "Child"
            price = 6.00 if is_matinee else 8.00
        elif age <= 17:
            age_group = "Teen"
            price = 7.00 if is_matinee else 10.00
        elif age <= 64:
            age_group = "Adult"
            price = 8.00 if is_matinee else 13.00
        else:
            age_group = "Senior"
            price = 6.00 if is_matinee else 7.00

        print(f"Age group: {age_group}")
        print(f"Ticket price: ${price:.2f}")

except ValueError:
    print("Error: Age must be a valid integer.")
