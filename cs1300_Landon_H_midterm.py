# Problem 1: BMI Calculator

unit = input("Enter unit system (M/I): ")

if unit.lower() == "m":
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (meters): "))
    bmi = weight / (height ** 2)

elif unit.lower() == "i":
    weight = float(input("Enter weight (lbs): "))
    height = float(input("Enter height (inches): "))
    bmi = (weight * 703) / (height ** 2)

else:
    print("Invalid unit system.")
    exit()

print("BMI:", round(bmi, 1))

# Determine category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)

# Problem 2: Password Strength Checker

password = input("Enter a password: ")

length = len(password) >= 8
upper = any(c.isupper() for c in password)
lower = any(c.islower() for c in password)
digit = any(c.isdigit() for c in password)
special = any(not c.isalnum() for c in password)

score = 0

print("Length >= 8:", "PASS" if length else "FAIL")
if length: score += 1

print("Uppercase:", "PASS" if upper else "FAIL")
if upper: score += 1

print("Lowercase:", "PASS" if lower else "FAIL")
if lower: score += 1

print("Digit:", "PASS" if digit else "FAIL")
if digit: score += 1

print("Special char:", "PASS" if special else "FAIL")
if special: score += 1

print("\nCriteria met:", score, "/ 5")

if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Moderate"
elif score >= 1:
    strength = "Weak"
else:
    strength = "No password entered"

print("Strength:", strength)

# Problem 4: Parking Fee Calculator

vehicle = input("Enter vehicle type (car/motorcycle/truck): ")
hours = float(input("Enter hours parked: "))
monthly = input("Monthly pass (yes/no): ")

fee = 0

if monthly.lower() == "yes":
    fee = 0

else:
    if vehicle == "motorcycle":
        if hours <= 2:
            fee = 1
        else:
            fee = 1 + (hours - 2) * 0.5

    elif vehicle == "car":
        if hours <= 2:
            fee = 3
        else:
            fee = 3 + (hours - 2) * 1.5

    elif vehicle == "truck":
        if hours <= 2:
            fee = 5
        else:
            fee = 5 + (hours - 2) * 2.5

    else:
        print("Invalid vehicle type")
        exit()

print("\n--- Parking Receipt ---")
print("Vehicle:", vehicle)
print("Duration:", hours, "hours")
print("Pass holder:", monthly)
print("Fee: $", round(fee,2))

# Problem 5: Word Frequency Counter

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

print("\nTotal words:", len(words))

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("\nWord Frequencies")

most_word = ""
most_count = 0

for word in unique_words:
    count = words.count(word)
    print(word + ":", count)

    if count > most_count:
        most_count = count
        most_word = word

print("\nMost frequent word:", '"' + most_word + '"', "(", most_count, "times )")