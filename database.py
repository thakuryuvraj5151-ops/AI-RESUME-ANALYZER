import sqlite3


DATABASE_NAME = "resume_analyzer.db"


# =========================
# CREATE DATABASE
# =========================

def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_analysis (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            resume_name TEXT,

            resume_score REAL,

            section_score REAL,

            ats_score REAL,

            skills TEXT,

            job_role TEXT,

            match_score REAL,

            missing_skills TEXT

        )
    """)


    # =========================
    # CHECK EXISTING COLUMNS
    # =========================

    cursor.execute("""
        PRAGMA table_info(resume_analysis)
    """)

    columns = cursor.fetchall()

    column_names = [
        column[1]
        for column in columns
    ]


    # =========================
    # ADD USER ID IF MISSING
    # =========================

    if "user_id" not in column_names:

        cursor.execute("""
            ALTER TABLE resume_analysis
            ADD COLUMN user_id INTEGER
        """)


    # =========================
    # ADD ATS SCORE IF MISSING
    # =========================

    if "ats_score" not in column_names:

        cursor.execute("""
            ALTER TABLE resume_analysis
            ADD COLUMN ats_score REAL
        """)


    connection.commit()

    connection.close()


# =========================
# SAVE ANALYSIS
# =========================

def save_analysis(

    user_id,
    resume_name,
    resume_score,
    section_score,
    ats_score,
    skills,
    job_role,
    match_score,
    missing_skills

):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO resume_analysis
        (
            user_id,
            resume_name,
            resume_score,
            section_score,
            ats_score,
            skills,
            job_role,
            match_score,
            missing_skills
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        user_id,
        resume_name,
        resume_score,
        section_score,
        ats_score,
        skills,
        job_role,
        match_score,
        missing_skills

    ))


    connection.commit()

    connection.close()


# =========================
# GET ANALYSIS HISTORY
# =========================

def get_analysis_history(user_id):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()


    cursor.execute("""
        SELECT

            id,

            resume_name,

            resume_score,

            section_score,

            ats_score,

            job_role,

            match_score,

            missing_skills

        FROM resume_analysis

        WHERE user_id = ?

        ORDER BY id DESC

    """, (user_id,))


    records = cursor.fetchall()

    connection.close()

    return records