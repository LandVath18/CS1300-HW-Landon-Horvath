names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]


print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")
print("====================")

highest_index = 0
lowest_index = 0

for i in range(len(scores)):
    if scores[i] > scores[highest_index]:
        highest_index = i
    if scores[i] < scores[lowest_index]:
        lowest_index = i

print("Highest:", names[highest_index], "-", scores[highest_index])
print("Lowest:", names[lowest_index], "-", scores[lowest_index])


total = 0
for score in scores:
    total += score

average = total / len(scores)
print(f"Class average: {average:.2f}")


print("--- Grade Report ---")

for i in range(len(names)):
    score = scores[i]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{names[i]}: {score} -> {grade}")


names.append("Frank")
scores.append(77)

remove_index = names.index("Diana")
names.pop(remove_index)
scores.pop(remove_index)

print("Updated roster length:", len(names))