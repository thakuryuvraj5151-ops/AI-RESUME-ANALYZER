def find_missing_skills(resume_skills, required_skills):
    """
    Find the skills required for a job role
    that are missing from the resume.
    """

    missing_skills = []

    for skill in required_skills:

        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills