def calculate_resume_score(resume_skills, recommendations):

    if not resume_skills:
        return 0

    total_match = 0

    for job in recommendations:
        total_match += job["match_percentage"]

    average_match = total_match / len(recommendations)

    score = round(average_match, 2)

    return score