from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


JOB_DESCRIPTIONS = {

    "Python Developer": """
    We are looking for a Python Developer with experience in
    Python programming, SQL, Flask, Django, Git and REST APIs.
    The candidate should have good knowledge of backend development
    and database management.
    """,

    "Data Analyst": """
    We are looking for a Data Analyst with skills in Python,
    SQL, Pandas, NumPy, Matplotlib and Power BI.
    Knowledge of data analysis, data visualization and statistics
    is required.
    """,

    "Machine Learning Engineer": """
    We are looking for a Machine Learning Engineer with strong
    Python programming skills and knowledge of Machine Learning,
    Scikit-learn, Pandas, NumPy and TensorFlow.
    Experience with machine learning algorithms and model development
    is preferred.
    """,

    "AI Engineer": """
    We are looking for an AI Engineer with knowledge of Python,
    Artificial Intelligence, Machine Learning, TensorFlow and Keras.
    Knowledge of deep learning and neural networks is beneficial.
    """,

    "Cloud Engineer": """
    We are looking for a Cloud Engineer with experience in AWS,
    Python, Git, Docker and cloud computing.
    Knowledge of cloud infrastructure and deployment is required.
    """
}


def calculate_similarity(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0] * 100

    return round(score, 2)


def match_resume_with_jobs(resume_text):

    results = []

    for job_role, description in JOB_DESCRIPTIONS.items():

        score = calculate_similarity(
            resume_text,
            description
        )

        results.append({
            "job_role": job_role,
            "ml_match_score": score
        })

    results.sort(
        key=lambda x: x["ml_match_score"],
        reverse=True
    )

    return results

if __name__ == "__main__":

    resume = """
    I am a Python developer with experience in Python,
    SQL, Flask, Machine Learning, Pandas, NumPy and AWS.
    I have knowledge of Git and TensorFlow.
    """

    results = match_resume_with_jobs(resume)

    for result in results:

        print(
            result["job_role"],
            ":",
            result["ml_match_score"],
            "%"
        )
def calculate_hybrid_score(skill_score, ml_score):

    hybrid_score = (skill_score * 0.5) + (ml_score * 0.5)

    return round(hybrid_score, 2)