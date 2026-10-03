from flask import Flask, request, jsonify, render_template, redirect, session
from PyPDF2 import PdfReader
import io

from resume_analyzer import extract_skills
from job_recommender import recommend_jobs
from skill_gap import find_missing_skills
from resume_score import calculate_resume_score
from learning_recommendation import get_learning_recommendations
from job_matcher import match_resume_with_jobs, calculate_hybrid_score
from s3_storage import upload_resume
from resume_section_analyzer import analyze_resume_sections
from ats_analyzer import analyze_ats

from database import create_database, save_analysis, get_analysis_history
from auth import create_users_table, register_user, login_user


app = Flask(__name__)

app.secret_key = "ai_resume_analyzer_secret_key"


# Create database and users table
create_database()
create_users_table()


# --------------------------------
# PDF TEXT EXTRACTION
# --------------------------------

def extract_text_from_pdf(file):
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# --------------------------------
# HOME
# --------------------------------

@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "index.html",
        username=session["username"]
    )


# --------------------------------
# REGISTER PAGE
# --------------------------------

@app.route("/register", methods=["GET"])
def register_page():

    return render_template("register.html")


# --------------------------------
# REGISTER USER
# --------------------------------

@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["password"]

    success = register_user(username, password)

    if success:
        return redirect("/login")

    return "Username already exists. Please choose another username."


# --------------------------------
# LOGIN PAGE
# --------------------------------

@app.route("/login", methods=["GET"])
def login_page():

    return render_template("login.html")


# --------------------------------
# LOGIN USER
# --------------------------------

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    user = login_user(username, password)

    if user:

        session["user_id"] = user["id"]
        session["username"] = user["username"]

        return redirect("/")

    return "Invalid username or password."


# --------------------------------
# LOGOUT
# --------------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# --------------------------------
# RESUME ANALYSIS
# --------------------------------

@app.route("/extract", methods=["POST"])
def extract_resume():

    # Check login
    if "user_id" not in session:

        return jsonify({
            "error": "Please login first."
        }), 401


    # Get uploaded file
    file = request.files.get("resume")


    if not file:

        return jsonify({
            "error": "Please upload a resume PDF."
        }), 400


    # --------------------------------
    # READ FILE DATA
    # --------------------------------

    try:

        file_data = file.read()

        if not file_data:

            return jsonify({
                "error": "Uploaded file is empty."
            }), 400

    except Exception as e:

        return jsonify({
            "error": "Could not read uploaded file.",
            "details": str(e)
        }), 500


    # --------------------------------
    # AWS S3 UPLOAD
    # --------------------------------

    s3_filename = f"{session['user_id']}_{file.filename}"

    print("Uploading resume to AWS S3...")
    print("Filename:", s3_filename)


    try:

        s3_file = io.BytesIO(file_data)

        s3_path = upload_resume(
            s3_file,
            s3_filename
        )

        print("S3 UPLOAD SUCCESS:", s3_path)


    except Exception as e:

        print("S3 UPLOAD ERROR:", e)

        return jsonify({
            "error": "Resume could not be uploaded to AWS S3.",
            "details": str(e)
        }), 500


    # --------------------------------
    # READ PDF AGAIN
    # --------------------------------

    try:

        pdf_file = io.BytesIO(file_data)

        text = extract_text_from_pdf(pdf_file)

        print("PDF TEXT EXTRACTION SUCCESS")


    except Exception as e:

        print("PDF EXTRACTION ERROR:", e)

        return jsonify({
            "error": "Could not extract text from the PDF.",
            "details": str(e)
        }), 500


    # Check extracted text
    if not text.strip():

        return jsonify({
            "error": "Could not extract text from the PDF."
        }), 400


    # --------------------------------
    # ATS ANALYSIS
    # --------------------------------

    try:

        ats_analysis = analyze_ats(text)

    except Exception as e:

        print("ATS ERROR:", e)

        return jsonify({
            "error": "ATS analysis failed.",
            "details": str(e)
        }), 500


    # --------------------------------
    # RESUME SECTION ANALYSIS
    # --------------------------------

    section_analysis = analyze_resume_sections(text)

    sections = section_analysis["sections"]

    section_score = section_analysis["section_score"]

    section_suggestions = section_analysis["suggestions"]


    # --------------------------------
    # SKILL EXTRACTION
    # --------------------------------

    skills = extract_skills(text)


    # --------------------------------
    # JOB RECOMMENDATIONS
    # --------------------------------

    recommendations = recommend_jobs(skills)


    # --------------------------------
    # ML JOB MATCHING
    # --------------------------------

    ml_recommendations = match_resume_with_jobs(text)


    ml_score_map = {}


    for ml_job in ml_recommendations:

        role = ml_job["job_role"]

        score = ml_job["ml_match_score"]

        ml_score_map[role] = score


    # --------------------------------
    # RESUME SCORE
    # --------------------------------

    resume_score = calculate_resume_score(
        skills,
        recommendations
    )


    # --------------------------------
    # HYBRID JOB MATCH SCORE
    # --------------------------------

    for job in recommendations:

        job_role = job["job_role"]

        skill_score = job.get(
            "match_percentage",
            0
        )

        ml_score = ml_score_map.get(
            job_role,
            0
        )

        job["ml_match_score"] = round(
            ml_score,
            2
        )

        job["final_match_score"] = calculate_hybrid_score(
            skill_score,
            ml_score
        )


    # --------------------------------
    # SKILL GAP + LEARNING
    # --------------------------------

    for job in recommendations:

        job["missing_skills"] = find_missing_skills(
            skills,
            job["required_skills"]
        )

        job["learning_recommendations"] = get_learning_recommendations(
            job["missing_skills"]
        )


    # --------------------------------
    # SAVE ANALYSIS TO DATABASE
    # --------------------------------

    resume_name = file.filename


    for job in recommendations:

        save_analysis(

            session["user_id"],

            resume_name,

            resume_score,

            section_score,

            ats_analysis["ats_score"],

            ", ".join(skills),

            job["job_role"],

            job["final_match_score"],

            ", ".join(job["missing_skills"])

        )


    # --------------------------------
    # SEND RESULT TO FRONTEND
    # --------------------------------

    return jsonify({

        "message": "Resume processed successfully",

        "s3_path": s3_path,

        "skills": skills,

        "resume_score": resume_score,

        "section_score": section_score,

        "sections": sections,

        "section_suggestions": section_suggestions,

        "job_recommendations": recommendations,

        "ml_recommendations": ml_recommendations,

        "ats_analysis": ats_analysis,

        "extracted_text": text

    })


# --------------------------------
# HISTORY PAGE
# --------------------------------

@app.route("/history")
def history_page():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(
        "history.html",
        username=session["username"]
    )


# --------------------------------
# HISTORY API
# --------------------------------

@app.route("/api/history")
def history_api():

    if "user_id" not in session:

        return jsonify({
            "error": "Please login first."
        }), 401


    records = get_analysis_history(
        session["user_id"]
    )


    history_data = []


    for record in records:

        history_data.append({

            "id": record[0],

            "resume_name": record[1],

            "resume_score": record[2],

            "section_score": record[3],

            "ats_score": record[4],

            "job_role": record[5],

            "match_score": record[6],

            "missing_skills": record[7]

        })


    return jsonify(history_data)


# --------------------------------
# REPORT PAGE
# --------------------------------

@app.route("/report")
def report_page():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(
        "report.html",
        username=session["username"]
    )


# --------------------------------
# START FLASK SERVER
# --------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )