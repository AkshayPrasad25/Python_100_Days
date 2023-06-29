students_scores={
    "Harry": 81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

student_grades={}

for student in students_scores:
    score=students_scores[student]
    if score>90:
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds expectations"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"

print(student_grades)
