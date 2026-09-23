def learn_skill(student):
    skill = input("Enter skill: ")
    if skill not in student["learn_skills"]:
        student["learn_skills"].append(skill)
    return student