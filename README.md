# Gradebook Module

A Python module for managing student grades.

## Functions

- `calculate_average(scores)` — returns the average of a list of scores
- `get_letter_grade(average)` — returns A/B/C/D/F for a given average
- `is_passing(average)` — returns True if the average is passing
- `get_top_students(grade_dict, threshold)` — returns students above threshold
- `format_report(student, scores)` — returns a formatted grade report string

## Running Tests

```bash
pytest tests/
```
