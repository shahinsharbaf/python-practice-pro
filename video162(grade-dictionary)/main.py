student_scores_dictionary = {
    "Jhon": 90,
    "Edy": 68,
    "Marry": 88,
    "Evan": 79,
    "PArk": 62,
}


def convert_grade(my_dictionary):
    converted_student_scores_dictonary = {}
    for key in my_dictionary:
        if my_dictionary[key] <= 100 and my_dictionary[key] >= 85:
            converted_student_scores_dictonary[key] = "Outstanding"
        if my_dictionary[key] <= 84 and my_dictionary[key] >= 65:
            converted_student_scores_dictonary[key] = "Good"
        if my_dictionary[key] <= 64 and my_dictionary[key] >= 50:
            converted_student_scores_dictonary[key] = "Acceptable"
        if my_dictionary[key] <= 49:
            converted_student_scores_dictonary[key] = "Fail"
    return (converted_student_scores_dictonary)


print(convert_grade(student_scores_dictionary))
