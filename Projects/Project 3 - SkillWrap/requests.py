def create_request(requests, learner_id, teacher_id, skill):
    request_id = len(requests) + 1
    request = {
        "request_id": request_id,
        "learner_id": learner_id,
        "teacher_id": teacher_id,
        "skill": skill,
        "status": "Pending"
    }
    requests.append(request)
    return requests


def update_request(requests, request_id, new_status):
    for request in requests:
        if request["request_id"] == request_id:
            request["status"] = new_status
            return True
    return False


def get_student_requests(requests, student_id):
    student_requests = []
    for request in requests:
        if request["learner_id"] == student_id or request["teacher_id"] == student_id:
            student_requests.append(request)
    return student_requests