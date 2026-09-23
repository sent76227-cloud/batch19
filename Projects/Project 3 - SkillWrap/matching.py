def find_teachers(students, skill, learner_id):
    teachers = []
    wanted_skill = skill.lower()

    for student in students:
        if student["student_id"] == learner_id:
            continue

        for teacher_skill, details in student["teach_skills"].items():
            if teacher_skill.lower() == wanted_skill and details["verified"]:
                teachers.append(student)

    return teachers


def find_mutual_matches(students, student):
    matches = []

    for other_student in students:
        if other_student["student_id"] == student["student_id"]:
            continue

        for learning_skill in student["learn_skills"]:
            if learning_skill.lower() in [skill.lower() for skill in other_student["teach_skills"]]:
                skill_data = other_student["teach_skills"][learning_skill]
                if skill_data["verified"]:
                    matches.append((other_student, learning_skill))

    return matches