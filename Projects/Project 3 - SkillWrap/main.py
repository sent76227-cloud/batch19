from student import register_student
from teach_skill import add_skillto
from learn_skill import learn_skill
from test import take_test
from matching import find_teachers, find_mutual_matches
from requests import create_request, update_request, get_student_requests
from rating import add_rating, get_average_rating
from data import load_data, save_data
from statistics import show_statistics


def get_number(message):
    try:
        return int(input(message))
    except ValueError:
        print("Please enter a number.")
        return 0


def show_profile(student, ratings):
    print("\n===== Student Profile =====")
    for key, value in student.items():
        print(key, "=", value)
    print("Average rating:", get_average_rating(ratings, student["student_id"]))


def find_student(students, student_id):
    for student in students:
        if str(student["student_id"]) == str(student_id):
            return student
    return None


def register_new_student(data):
    print("\n===== Student Registration =====")
    student_id = input("Enter student id: ")
    if find_student(data["students"], student_id) is not None:
        print("This student id already exists.")
        return None

    name = input("Enter student name: ")
    course = input("Enter course: ")
    semester = input("Enter semester: ")
    email = input("Enter email: ")
    student = register_student(student_id, name, course, semester, email)
    data["students"].append(student)
    print("Registration successful.")
    return student


def show_teachers(teachers):
    if len(teachers) == 0:
        print("No verified teacher is currently available.")
        return

    for teacher in teachers:
        print("\nTeacher:", teacher["name"], "ID:", teacher["student_id"])
        for skill, details in teacher["teach_skills"].items():
            print(skill, "-", details["level"])
            print("Available:", details["available_days"], details["available_time"])
            print("Place:", details["meeting_place"])
            print("Fee:", details["fee"] if details["teaching_type"] == "paid" else "Free")


def main():
    data = load_data()
    active_student = None

    while True:
        print("\n========== SkillSwap ==========")
        print("Active student:", active_student["name"] if active_student else "None")
        print("1. Register student")
        print("2. Select student")
        print("3. Add teaching skill and take assessment")
        print("4. Add learning skill")
        print("5. Show profile")
        print("6. Find verified teachers")
        print("7. Find mutual matches")
        print("8. Send learning request")
        print("9. Manage learning requests")
        print("10. Rate a completed connection")
        print("11. Show statistics")
        print("12. Save and exit")

        choice = get_number("Enter your choice: ")

        if choice == 1:
            active_student = register_new_student(data)
        elif choice == 2:
            student_id = input("Enter student id: ")
            active_student = find_student(data["students"], student_id)
            if active_student is None:
                print("Student not found.")
            else:
                print("Student selected.")
        elif choice == 3:
            if active_student is None:
                print("Register or select a student first.")
            else:
                active_student, skill = add_skillto(active_student)
                if skill != "":
                    take_test(active_student, skill)
        elif choice == 4:
            if active_student is None:
                print("Register or select a student first.")
            else:
                learn_skill(active_student)
                print("Learning skill added successfully.")
        elif choice == 5:
            if active_student is None:
                print("Register or select a student first.")
            else:
                show_profile(active_student, data["ratings"])
        elif choice == 6:
            if active_student is None:
                print("Register or select a student first.")
            else:
                skill = input("Which skill do you want to learn? ")
                teachers = find_teachers(data["students"], skill, active_student["student_id"])
                show_teachers(teachers)
        elif choice == 7:
            if active_student is None:
                print("Register or select a student first.")
            else:
                matches = find_mutual_matches(data["students"], active_student)
                if len(matches) == 0:
                    print("No mutual match found.")
                for matched_student, skill in matches:
                    print(matched_student["name"], "can teach", skill)
        elif choice == 8:
            if active_student is None:
                print("Register or select a student first.")
            else:
                skill = input("Skill you want to learn: ")
                teachers = find_teachers(data["students"], skill, active_student["student_id"])
                show_teachers(teachers)
                if len(teachers) > 0:
                    teacher_id = input("Enter teacher id for the request: ")
                    teacher = find_student(teachers, teacher_id)
                    if teacher is not None:
                        create_request(data["requests"], active_student["student_id"], teacher_id, skill)
                        print("Learning request sent.")
                    else:
                        print("Teacher not found in the results.")
        elif choice == 9:
            if active_student is None:
                print("Register or select a student first.")
            else:
                student_requests = get_student_requests(data["requests"], active_student["student_id"])
                for request in student_requests:
                    print(request)
                request_id = get_number("Enter request id to update, or 0 to cancel: ")
                if request_id != 0:
                    new_status = input("Enter Accepted or Rejected: ").title()
                    if update_request(data["requests"], request_id, new_status):
                        print("Request updated.")
                    else:
                        print("Request not found.")
        elif choice == 10:
            if active_student is None:
                print("Register or select a student first.")
            else:
                request_id = get_number("Enter accepted request id: ")
                selected_request = None
                for request in data["requests"]:
                    if request["request_id"] == request_id and request["learner_id"] == active_student["student_id"]:
                        selected_request = request
                if selected_request is None or selected_request["status"] != "Accepted":
                    print("Accepted request not found.")
                else:
                    score = get_number("Give rating from 1 to 5: ")
                    feedback = input("Feedback: ")
                    add_rating(data["ratings"], active_student["student_id"], selected_request["teacher_id"], score, feedback)
                    update_request(data["requests"], request_id, "Completed")
                    print("Rating saved.")
        elif choice == 11:
            show_statistics(data)
        elif choice == 12:
            save_data(data)
            print("Data saved. Thank you for using SkillSwap!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

