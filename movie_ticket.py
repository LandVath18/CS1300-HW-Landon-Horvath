# movie_ticket.py
# This program calculates movie ticket price based on age and matinee status

# Get user age
age = int(input("Enter your age: "))

# Validate age
if age < 0:
    print("Error: Age cannot be negative.")
else:
    # Ask if matinee and convert to Boolean using ternary operator
    matinee_input = input("Is this a matinee showing? (yes/no): ").lower()
    is_matinee = True if matinee_input == "yes" else False

    # Determine age group and pricing using nested if statements
    if age < 13:
        age_group = "Child"
        if is_matinee:
            price = 6.00
        else:
            price = 8.00

    elif age <= 17:
        age_group = "Teen"
        if is_matinee:
            price = 7.00
        else:
            price = 10.00

    elif age <= 64:
        age_group = "Adult"
        if is_matinee:
            price = 8.00
        else:
            price = 13.00

    else:
        age_group = "Senior"
        if is_matinee:
            price = 6.00
        else:
            price = 7.00

    # Output result
    print(f"Age group: {age_group}")
    print(f"Ticket price: ${price:.2f}")