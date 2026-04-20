"""
Week 14 - Lists Part II Exercises
CS 1300

Covers:
- Tuples
- List vs Tuple
- Nested Lists
- List Comprehensions
- Generators
"""

# ================================
# UNIT 1 EXERCISES
# ================================

print("\n=== UNIT 1: TUPLES ===")

# Beginner
rgb_color = (255, 128, 0)
print(rgb_color[0])  # Red
print(rgb_color[1])  # Green
print(rgb_color[2])  # Blue

palette = []
palette.append(rgb_color)
print("Palette:", palette)

# Intermediate
student1 = ("Alice", "A", 20)
student2 = ("Bob", "B", 21)
student3 = ("Charlie", "C", 19)

classroom = [student1, student2, student3]

print("Second student name:", classroom[1][0])

name, grade, age = classroom[0]
print(f"{name} is {age} years old and has grade {grade}")

# Advanced
student = ("Alice", [85, 90, 78], "B")

print("Original:", student)

student[1].append(92)

avg = sum(student[1]) / len(student[1])

if avg >= 90:
    new_grade = "A"
elif avg >= 80:
    new_grade = "B"
elif avg >= 70:
    new_grade = "C"
elif avg >= 60:
    new_grade = "D"
else:
    new_grade = "F"

updated_student = (student[0], student[1], new_grade)

print("Updated:", updated_student)


# ================================
# UNIT 2 EXERCISES
# ================================

print("\n=== UNIT 2: LIST VS TUPLE ===")

# Beginner
grades = [85, 90, 78]
today = (4, 19, 2026)

def boost_grades(grades):
    for i in range(len(grades)):
        grades[i] += 5

boost_grades(grades)
print("Boosted grades:", grades)

# List used because grades change, tuple used because date is fixed

# Intermediate
def find_range(*args):
    return (min(args), max(args))

print(find_range(1, 5, 3))
print(find_range(1, 2, 3, 4, 5, 6, 7))

test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))

# Advanced
def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    avg = total / count if count > 0 else 0
    return (count, total, avg)

def update_student_records(records, bonus):
    new_records = []
    for name, grade in records:
        new_records.append((name, grade + bonus))
    return new_records

records = [("Alice", 85), ("Bob", 90)]
updated = update_student_records(records, 5)

print("Stats:", calculate_statistics(10, 20, 30))
print("Updated Records:", updated)


# ================================
# UNIT 3 EXERCISES
# ================================

print("\n=== UNIT 3: NESTED LISTS ===")

# Beginner
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Grid:", grid)
print("Center:", grid[1][1])

for row in grid:
    print(row)

# Intermediate
scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [s for s in scores if s >= 60]

letter_grades = [
    "A" if s >= 90 else
    "B" if s >= 80 else
    "C" if s >= 70 else
    "D"
    for s in passing_grades
]

print("Passing:", passing_grades)
print("Letters:", letter_grades)

# Advanced
table = [[i*j for j in range(1,5)] for i in range(1,5)]

print("Multiplication Table:")
for row in table:
    print(row)

def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

print("Diagonal Sum:", sum_diagonal(table))

# Generator
even_gen = (num for row in table for num in row if num % 2 == 0)

print("First 5 even numbers:")
for _ in range(5):
    print(next(even_gen))