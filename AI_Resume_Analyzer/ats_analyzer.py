# =========================
# ATS KEYWORDS
# =========================

ATS_KEYWORDS = [

    "python",
    "java",
    "c++",
    "sql",
    "javascript",

    "html",
    "css",

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


# =========================
# IMPORTANT RESUME SECTIONS
# =========================

ATS_SECTIONS = {

    "Education": [
        "education",
        "academic",
        "qualification"
    ],

    "Experience": [
        "experience",
        "work experience",
        "professional experience"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "technical knowledge"
    ],

    "Projects": [
        "projects",
        "project",
        "academic project"
    ],

    "Certifications": [
        "certifications",
        "certification",
        "certificate"
    ]
}


# =========================
# ATS ANALYSIS FUNCTION
# =========================

def analyze_ats(resume_text):

    text = resume_text.lower()


    # -------------------------
    # KEYWORD ANALYSIS
    # -------------------------

    found_keywords = []

    missing_keywords = []


    for keyword in ATS_KEYWORDS:

        if keyword.lower() in text:

            found_keywords.append(keyword)

        else:

            missing_keywords.append(keyword)


    total_keywords = len(ATS_KEYWORDS)

    found_count = len(found_keywords)


    if total_keywords > 0:

        keyword_score = (
            found_count / total_keywords
        ) * 100

    else:

        keyword_score = 0


    # -------------------------
    # SECTION ANALYSIS
    # -------------------------

    section_status = {}


    for section, keywords in ATS_SECTIONS.items():

        section_found = False


        for keyword in keywords:

            if keyword.lower() in text:

                section_found = True

                break


        section_status[section] = section_found


    total_sections = len(section_status)

    found_sections = 0


    for section in section_status:

        if section_status[section]:

            found_sections += 1


    if total_sections > 0:

        section_score = (
            found_sections / total_sections
        ) * 100

    else:

        section_score = 0


    # -------------------------
    # FINAL ATS SCORE
    # -------------------------

    ats_score = (
        keyword_score * 0.6
    ) + (
        section_score * 0.4
    )


    ats_score = round(
        ats_score,
        2
    )


    # -------------------------
    # SUGGESTIONS
    # -------------------------

    suggestions = []


    if keyword_score < 50:

        suggestions.append(
            "Add more relevant technical keywords."
        )


    if keyword_score >= 50 and keyword_score < 75:

        suggestions.append(
            "Improve the use of relevant technical keywords."
        )


    for section, status in section_status.items():

        if not status:

            suggestions.append(
                "Consider adding a "
                + section
                + " section."
            )


    if len(suggestions) == 0:

        suggestions.append(
            "Resume has good ATS keyword and section coverage."
        )


    # -------------------------
    # RETURN RESULT
    # -------------------------

    return {

        "ats_score":
            ats_score,

        "keyword_score":
            round(keyword_score, 2),

        "section_score":
            round(section_score, 2),

        "found_keywords":
            found_keywords,

        "missing_keywords":
            missing_keywords,

        "sections":
            section_status,

        "suggestions":
            suggestions

    }