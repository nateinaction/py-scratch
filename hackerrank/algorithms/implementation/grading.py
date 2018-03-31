def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade % 5 >= 3 and grade >= 38:
            base = 5
            new_grades.append(base * round(grade / base))
        else:
            new_grades.append(grade)
    return new_grades
