def add_skillto(student):
    skill = input("Enter skill: ")
    level_choice = input("Select level (1. Beginner, 2. Intermediate, 3. Advanced): ")

    levels = {
        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced"
    }

    if level_choice not in levels:
        print("Invalid level.")
        return student, ""

    available_days = input("Available days: ")
    available_time = input("Available time: ")
    meeting_place = input("Meeting place: ")
    teaching_type = input("Teaching type (free/paid): ").lower()
    fee = 0
    if teaching_type == "paid":
        fee = input("Fee per session: ")

    student["teach_skills"][skill] = {
        "level": levels[level_choice],
        "verified": False,
        "score": 0,
        "available_days": available_days,
        "available_time": available_time,
        "meeting_place": meeting_place,
        "teaching_type": teaching_type,
        "fee": fee
    }
    return student, skill
