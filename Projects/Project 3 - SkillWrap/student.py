def register_student(student_id,student_name,course,semester,email):
    student = {"student_id":student_id,
    "name":student_name,
    "course":course,
    "semester":semester,
    "email":email,
    "teach_skills":{},
    "learn_skills":[]
    }
    return student
'''Input
 ↓
register_student()
 ↓
Dictionary
 ↓
return student
 ↓
student_data
 ↓
Display data'''
    

