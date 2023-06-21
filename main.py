required_courses = {
    'Должность 1': ['Курс 1', 'Курс 3'],
    'Должность 2': ['Курс 2', 'Курс 3', 'Курс 4'],
    'Должность 3': ['Курс 2', 'Курс 3'],
    'Должность 4': ['Курс 1', 'Курс 2', 'Курс 3', 'Курс 4']
}

competency_course_matrix = {
    'Курс 1': ['Компетенция 1'],
    'Курс 2': ['Компетенция 3'],
    'Курс 3': ['Компетенция 4'],
    'Курс 4': ['Компетенция 2']
}

competency_model = {
    'Должность 1': {'Компетенция 1': 3, 'Компетенция 3': 1, 'Компетенция 4': 2},
    'Должность 2': {'Компетенция 2': 1, 'Компетенция 3': 3},
    'Должность 3': {'Компетенция 1': 3, 'Компетенция 2': 3, 'Компетенция 3': 3, 'Компетенция 4': 1},
    'Должность 4': {'Компетенция 1': 2, 'Компетенция 2': 2}
}

competency_results = {
    'Сотрудник 1': {'Должность': 'Должность 1', 'Компетенция 1': 2, 'Компетенция 3': 3, 'Компетенция 4': 2},
    'Сотрудник 2': {'Должность': 'Должность 3', 'Компетенция 1': 3, 'Компетенция 2': 2, 'Компетенция 3': 1, 'Компетенция 4': 1},
    'Сотрудник 3': {'Должность': 'Должность 2', 'Компетенция 2': 3, 'Компетенция 3': 1},
    'Сотрудник 4': {'Должность': 'Должность 4', 'Компетенция 1': 2, 'Компетенция 2': 3}
}

def check_required_courses(employee):
    position = employee['Должность']
    competency_scores = employee.copy()
    del competency_scores['Должность']

    required_courses_list = required_courses.get(position, [])
    courses_to_take = []

    for competency, score in competency_scores.items():
        if competency in competency_model[position] and score < competency_model[position][competency]:
            for course, competencies in competency_course_matrix.items():
                if competency in competencies and course in required_courses_list and course not in courses_to_take:
                    courses_to_take.append(course)

    return courses_to_take

for employee, scores in competency_results.items():
    courses = check_required_courses(scores)
    if courses:
        print(f"Сотруднику {employee} необходимо пройти следующие курсы: {', '.join(courses)}")
    else:
        print(f"Сотруднику {employee} не требуется проходить дополнительные курсы.")
