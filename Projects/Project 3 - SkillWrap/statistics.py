def show_statistics(data):
    verified_skills = 0
    total_skills = 0

    for student in data["students"]:
        total_skills += len(student["teach_skills"])
        for skill in student["teach_skills"].values():
            if skill["verified"]:
                verified_skills += 1

    accepted_requests = 0
    for request in data["requests"]:
        if request["status"] == "Accepted":
            accepted_requests += 1

    print("\n===== Application Statistics =====")
    print("Students registered:", len(data["students"]))
    print("Teaching skills added:", total_skills)
    print("Verified skills:", verified_skills)
    print("Learning requests:", len(data["requests"]))
    print("Accepted requests:", accepted_requests)
    print("Ratings submitted:", len(data["ratings"]))