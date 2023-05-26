from collections import Counter

print(f"{'Задание 1' :-^60}")
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names_students = dict(Counter([student['first_name'] for student in students]))
for name in names_students:
    print(f"{name}: {names_students[name]}")


print(f"{'Задание 2' :-^60}")
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names_students = [student['first_name'] for student in students]
print(f"Самое частое имя среди учеников: {max(set(names_students), key = names_students.count)}")


print(f"{'Задание 3' :-^60}")
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for school_class in range(0, len(school_students)):
    class_names = [class_student['first_name'] for class_student in school_students[school_class]]
    print(f"Самое частое имя в классе {school_class + 1}: {max(set(class_names), key = class_names.count)}")


print(f"{'Задание 4' :-^60}")
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_school in school:
    print(f"Класс {class_school['class']}: девочки {(lambda x: [is_male[x['first_name']] for x in class_school['students']])(class_school).count(False)}, мальчики {(lambda x: [is_male[x['first_name']] for x in class_school['students']])(class_school).count(True)}")


print(f"{'Задание 5' :-^60}")
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

girls_and_boys = []

for class_school in school:
    girls_and_boys.append({
        'class': class_school['class'],
        'girls': (lambda x: [is_male[x['first_name']] for x in class_school['students']])(class_school).count(False),
        'boys': (lambda x: [is_male[x['first_name']] for x in class_school['students']])(class_school).count(True)
    })

print(f"Больше всего мальчиков в классе {max(girls_and_boys, key=lambda x: x['boys'])['class']}")
print(f"Больше всего девочек в классе {max(girls_and_boys, key=lambda x: x['girls'])['class']}")

print('-' * 60)