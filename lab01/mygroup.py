# -*- coding: utf-8 -*-
"""Список одногруппников и фильтр по среднему баллу."""

groupmates = [
    {
        "name": "Мария",
        "surname": "Орлова",
        "exams": ["Алгебра", "История", "Web"],
        "marks": [5, 4, 5],
    },
    {
        "name": "Павел",
        "surname": "Новиков",
        "exams": ["Физика", "Программирование", "КТП"],
        "marks": [4, 3, 4],
    },
    {
        "name": "Елена",
        "surname": "Васильева",
        "exams": ["Философия", "ИС", "Python"],
        "marks": [5, 5, 4],
    },
    {
        "name": "Роман",
        "surname": "Фёдоров",
        "exams": ["История", "АиГ", "Web"],
        "marks": [3, 4, 3],
    },
    {
        "name": "Ольга",
        "surname": "Морозова",
        "exams": ["Информатика", "Математика", "Python"],
        "marks": [5, 4, 5],
    },
]


def print_students(students):
    print(
        "Имя".ljust(15),
        "Фамилия".ljust(15),
        "Экзамены".ljust(40),
        "Оценки".ljust(15),
        "Среднее",
    )
    for student in students:
        avg = sum(student["marks"]) / float(len(student["marks"]))
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(40),
            str(student["marks"]).ljust(15),
            "{:.2f}".format(avg),
        )


def students_above_average(students, threshold):
    result = []
    for student in students:
        avg = sum(student["marks"]) / float(len(student["marks"]))
        if avg > threshold:
            result.append(student)
    return result


if __name__ == "__main__":
    print("Полный список:")
    print_students(groupmates)

    threshold = float(input("\nМинимальный средний балл для фильтра: "))
    print("\nСтуденты со средним выше {}:".format(threshold))
    print_students(students_above_average(groupmates, threshold))
