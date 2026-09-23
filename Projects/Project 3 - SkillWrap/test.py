QUESTIONS = {
    "python": [
        ("Which symbol starts a comment in Python?", ["//", "#", "<!--"], "2"),
        ("Which type stores multiple ordered values?", ["list", "integer", "boolean"], "1"),
        ("Which keyword creates a function?", ["function", "def", "fun"], "2")
    ],
    "html": [
        ("Which tag creates a paragraph?", ["<p>", "<h1>", "<br>"], "1"),
        ("Which language creates webpage structure?", ["HTML", "Python", "SQL"], "1"),
        ("Which tag creates a link?", ["<a>", "<linktext>", "<url>"], "1")
    ],
    "css": [
        ("What does CSS mainly control?", ["Style", "Database", "Server"], "1"),
        ("Which property changes text color?", ["paint", "color", "font-paint"], "2"),
        ("Which symbol selects a class?", [".", "#", "@"][0:3], "1")
    ]
}


def take_test(student, skill):
    questions = QUESTIONS.get(skill.lower(), QUESTIONS["python"])
    print("\nAssessment for", skill)
    print("Answer at least 2 out of 3 questions correctly.")
    score = 0

    for question, options, answer in questions:
        print("\n" + question)
        for number, option in enumerate(options, 1):
            print(str(number) + ".", option)
        choice = input("Your answer: ")
        if choice == answer:
            score += 1

    skill_data = student["teach_skills"][skill]
    skill_data["score"] = score
    skill_data["verified"] = score >= 2

    if skill_data["verified"]:
        print("Assessment passed. Skill verified.")
    else:
        print("Assessment not passed. Skill is not verified.")
    return student