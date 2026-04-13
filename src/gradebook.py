# gradebook.py
# Student grade management module


def calculate_average(scores):
    """Calculate the average of a list of scores."""
    # divides by len - 1 instead of len -- ZeroDivisionError on single score,
    # wrong answer on any list
    return sum(scores) / len(scores) # removed the -1


def get_letter_grade(average):
    """Return letter grade for a given average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    # missing else: any average below 60 returns None silently


def is_passing(average):
    """Return True if average is a passing grade (60 or above)."""
    # strict greater-than means exactly 60.0 is marked as failing
    return average > 60


def get_top_students(grade_dict, threshold=90):
    """Return list of students with averages at or above threshold."""
    top = []
    for student, scores in grade_dict.items():
        avg = calculate_average(scores)
        if avg >= threshold:
            top.append(student)
    return top


def format_report(student, scores):
    """Return a formatted string report for a student."""
    avg = calculate_average(scores)
    grade = get_letter_grade(avg)
    passing = is_passing(avg)
    return f"Student: {student} | Average: {avg} | Grade: {grade} | Passing: {passing}"
