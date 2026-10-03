# List of skills that our system can detect
SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",
    "nltk",
    "opencv",
    "git",
    "github",
    "aws",
    "azure",
    "docker",
    "mysql",
    "mongodb",
    "power bi",
    "tableau"
]


def extract_skills(resume_text):
    """
    Detect skills present in the resume text.
    """

    resume_text = resume_text.lower()

    detected_skills = []

    for skill in SKILLS:

        if skill.lower() in resume_text:
            detected_skills.append(skill)

    return detected_skills