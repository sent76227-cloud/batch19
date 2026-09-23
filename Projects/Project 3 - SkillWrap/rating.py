def add_rating(ratings, learner_id, teacher_id, score, feedback):
    rating = {
        "learner_id": learner_id,
        "teacher_id": teacher_id,
        "score": score,
        "feedback": feedback
    }
    ratings.append(rating)
    return ratings


def get_average_rating(ratings, teacher_id):
    scores = []
    for rating in ratings:
        if rating["teacher_id"] == teacher_id:
            scores.append(rating["score"])

    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)