# student_validator.py
# Creates a student profile and validates all inputs

errors = []

# Collect inputs
student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

# ----- Student ID Validation -----
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if not student_id[:1].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) == 8 and not student_id[1:].isdigit():
    errors.append("Last 7 characters must be digits")

# ----- Name Validation -----
if len(name.strip()) < 2:
    errors.append("Name cannot be empty")

# ----- Age Validation -----
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except:
    errors.append("Age must be a valid integer")

# ----- Major Validation -----
valid_majors = ["CS", "IT", "CE", "DS"]

if major.upper() not in valid_majors:
    errors.append(
        f"Major must be one of: CS, IT, CE, DS (got {major})"
    )

# ----- Output Results -----
if len(errors) == 0:
    print("✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major.upper()}")
else:
    print("✗ Profile has errors:")
    for error in errors:
        print("-", error)