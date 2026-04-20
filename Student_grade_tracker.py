"""
Student Grade Tracker
CS 1300 — Lecture 5 Mini-Project

A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and
displays a formatted report.

Functions:
get_student_name — Prompt for and return student name
is_valid_score — Helper: validate a single score
get_validated_scores — Helper: retry loop for score entry
get_exam_scores — Collect exam scores with validation
calculate_average — Compute mean of a scores list
determine_letter_grade — Map average to letter grade
determine_standing — Map average to academic standing
print_divider — Helper: print a decorative line
display_report — Print the formatted grade report
main — Orchestrate the full program
test_grade_tracker — Run all unit tests
"""


def get_student_name():
    """Prompt user for student name."""
    return input("Student name: ")


def is_valid_score(score_str):
    """
    Validate that a score is an integer between 0 and 100.

    Args:
        score_str (str): Input string

    Returns:
        bool: True if valid, False otherwise
    """
    if not score_str.isdigit():
        return False
    score = int(score_str)
    return 0 <= score <= 100


def get_validated_scores(prompt):
    """
    Prompt user until a valid score is entered.

    Args:
        prompt (str): Input prompt

    Returns:
        int: Valid score
    """
    while True:
        value = input(prompt)
        if is_valid_score(value):
            return int(value)
        print("Invalid score! Enter a number between 0 and 100.")


def get_exam_scores(num_exams=3):
    """
    Collect exam scores from user.

    Args:
        num_exams (int): Number of exams

    Returns:
        list: List of integer scores
    """
    scores = []
    for i in range(num_exams):
        score = get_validated_scores(f"Exam {i+1} score: ")
        scores.append(score)
    return scores




def calculate_average(scores):
    """
    Calculate average of scores.

    Args:
        scores (list): List of numbers

    Returns:
        float: Average score
    """
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def determine_letter_grade(avg):
    """
    Determine letter grade from average.

    Args:
        avg (float): Average score

    Returns:
        str: Letter grade
    """
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def determine_standing(avg):
    """
    Determine academic standing.

    Args:
        avg (float): Average score

    Returns:
        str: Academic standing
    """
    if avg >= 90:
        return "Dean's List"
    elif avg >= 70:
        return "Good Standing"
    elif avg >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"




def print_divider(char="=", length=30):
    """Print a divider line."""
    print(char * length)


def display_report(name, scores, avg, grade, standing):
    """
    Display formatted student report.

    Args:
        name (str): Student name
        scores (list): Exam scores
        avg (float): Average
        grade (str): Letter grade
        standing (str): Academic standing
    """
    print_divider()
    print("STUDENT GRADE REPORT")
    print_divider()

    print(f"Student: {name}")
    for i, score in enumerate(scores, 1):
        print(f"Exam {i}: {score}")

    print("-" * 30)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")

    print_divider()




def main():
    """Run the student grade tracker program."""
    name = get_student_name()
    scores = get_exam_scores()

    avg = calculate_average(scores)
    grade = determine_letter_grade(avg)
    standing = determine_standing(avg)

    display_report(name, scores, avg, grade, standing)




def test_grade_tracker():
    """Test core calculation functions."""

    print("\nRunning Tests...\n")

    # Test calculate_average
    print("Test Average:", end=" ")
    if calculate_average([100, 90, 80]) == 90:
        print("PASS")
    else:
        print("FAIL")

    # Edge case
    print("Test Average Empty:", end=" ")
    if calculate_average([]) == 0:
        print("PASS")
    else:
        print("FAIL")

    # Test letter grades
    print("Test Grade A:", end=" ")
    print("PASS" if determine_letter_grade(95) == "A" else "FAIL")

    print("Test Grade C:", end=" ")
    print("PASS" if determine_letter_grade(75) == "C" else "FAIL")

    # Test standing
    print("Test Standing Dean's List:", end=" ")
    print("PASS" if determine_standing(92) == "Dean's List" else "FAIL")

    print("Test Standing Warning:", end=" ")
    print("PASS" if determine_standing(50) == "Academic Warning" else "FAIL")




if __name__ == "__main__":
    test_grade_tracker()  # run tests first
    print("\n--- Program Start ---\n")
    main()