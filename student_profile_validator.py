# Student Profile Validator

errors = []

student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

# Student ID validation
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if len(student_id) >= 1 and not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) == 8 and not student_id[1:].isdigit():
    errors.append("Last 7 characters of Student ID must be digits")

# Name validation
if len(name.strip()) < 2:
    errors.append("Name must be at least 2 characters and not empty")

# Age validation
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
    errors.append("Age must be a valid integer")

# Major validation
valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

# Output results
if len(errors) == 0:
    print("✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name.strip()}")
    print(f"Age: {age}")
    print(f"Major: {major.upper()}")
else:
    print("✗ Profile has errors:")
    for error in errors:
        print("-", error)
