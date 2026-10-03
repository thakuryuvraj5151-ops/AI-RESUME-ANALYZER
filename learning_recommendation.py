LEARNING_RESOURCES = {

    "python": "Python Programming",

    "sql": "SQL and Database Management",

    "flask": "Flask Web Development",

    "machine learning": "Machine Learning",

    "artificial intelligence": "Artificial Intelligence",

    "deep learning": "Deep Learning",

    "pandas": "Data Analysis with Pandas",

    "numpy": "Numerical Computing with NumPy",

    "matplotlib": "Data Visualization with Matplotlib",

    "scikit-learn": "Machine Learning with Scikit-learn",

    "tensorflow": "Deep Learning with TensorFlow",

    "keras": "Neural Networks with Keras",

    "git": "Git Version Control",

    "github": "GitHub and Collaboration",

    "aws": "AWS Cloud Computing",

    "docker": "Docker and Containerization",

    "mysql": "MySQL Database",

    "mongodb": "MongoDB Database",

    "power bi": "Power BI Data Visualization",

    "tableau": "Tableau Data Visualization"
}


def get_learning_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill in LEARNING_RESOURCES:

            recommendations.append(
                LEARNING_RESOURCES[skill]
            )

        else:

            recommendations.append(
                "Learn " + skill
            )

    return recommendations