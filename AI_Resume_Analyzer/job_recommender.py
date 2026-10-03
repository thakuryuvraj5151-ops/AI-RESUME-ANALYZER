# Job roles and their required skills

JOB_ROLES = {

    "Python Developer": [
        "python",
        "sql",
        "flask",
        "git"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "pandas",
        "power bi",
        "matplotlib"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "scikit-learn",
        "pandas",
        "numpy",
        "tensorflow"
    ],

    "AI Engineer": [
        "python",
        "artificial intelligence",
        "machine learning",
        "tensorflow",
        "keras"
    ],

    "Cloud Engineer": [
        "aws",
        "python",
        "git",
        "docker"
    ]
}


def recommend_jobs(resume_skills):

    recommendations = []

    for job_role, required_skills in JOB_ROLES.items():

        matched_skills = []

        for skill in required_skills:

            if skill in resume_skills:
                matched_skills.append(skill)

        total_required = len(required_skills)

        total_matched = len(matched_skills)

        match_percentage = (total_matched / total_required) * 100

        recommendations.append({
    "job_role": job_role,
    "match_percentage": round(match_percentage, 2),
    "matched_skills": matched_skills,
    "required_skills": required_skills
})

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations