gpa = float(input("Enter GPA (0.0-4.0): "))
credits = int(input("Enter credit hours completed: "))
prereq = input("Prerequisite completed? (yes/no): ").lower()

if gpa >= 3.5 and credits >= 60 and prereq == "yes":
    status = "Approved: You meet all requirements."

elif gpa >= 3.5 and credits >= 60 and prereq == "no":
    status = "Conditionally approved: Complete the prerequisite first."

elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."

elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."

else:
    status = "Denied: GPA is below minimum threshold."

print("\n--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print("Credits:", credits)
print("Prerequisite:", prereq.capitalize())
print("Status:", status)
print("----------------------------")


print("\n")
