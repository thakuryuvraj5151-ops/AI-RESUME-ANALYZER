# AI Resume Analyzer & Job Recommendation System

An AI-powered web application that analyzes resumes, extracts technical skills, evaluates ATS compatibility, identifies skill gaps, recommends suitable job roles, and provides learning recommendations.

The system combines **Python, Flask, NLP, Machine Learning, TF-IDF, Cosine Similarity, SQLite, HTML, CSS, and JavaScript** to provide an interactive resume analysis dashboard.

---

## 📌 Project Overview

The **AI Resume Analyzer & Job Recommendation System** is designed to help students and job seekers understand how well their resume matches different technical job roles.

Users can upload their resume in PDF format. The system extracts the text from the resume and performs multiple types of analysis:

* Resume section analysis
* Technical skill extraction
* ATS keyword analysis
* Resume score calculation
* Job-role recommendation
* Skill-gap detection
* Learning recommendations
* ML-based job matching
* Hybrid job matching
* User-specific analysis history

The application provides all results through a web-based dashboard.

---

## 🎯 Objectives

The main objectives of this project are:

1. Automatically extract information from a resume.
2. Detect technical skills mentioned in the resume.
3. Analyze important resume sections.
4. Evaluate ATS keyword coverage.
5. Recommend suitable job roles.
6. Identify missing skills for recommended roles.
7. Suggest areas for learning and improvement.
8. Use NLP-based similarity to compare resumes with job descriptions.
9. Store user-specific resume analysis history.
10. Provide an easy-to-use web dashboard.

---

# 🚀 Features

## 1. Resume PDF Upload

Users can upload their resume in PDF format.

The system extracts readable text from the uploaded PDF using **PyPDF2**.

---

## 2. Automatic Skill Extraction

The system searches the extracted resume text for technical skills such as:

* Python
* Java
* C++
* SQL
* JavaScript
* HTML
* CSS
* Flask
* Django
* Machine Learning
* Deep Learning
* Artificial Intelligence
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* TensorFlow
* Keras
* PyTorch
* NLTK
* OpenCV
* Git
* GitHub
* AWS
* Azure
* Docker
* MySQL
* MongoDB
* Power BI
* Tableau

---

## 3. Resume Section Analysis

The system checks whether important sections are present in the resume.

Currently analyzed sections include:

* Education
* Experience
* Skills
* Projects
* Certifications

A section score is generated based on the number of detected sections.

---

## 4. ATS Analysis

The system contains an ATS analysis module that evaluates the resume using two major factors:

### Keyword Score

Checks how many relevant technical keywords are present.

### Section Score

Checks the presence of important resume sections.

### ATS Score

The final ATS score is calculated using:

```text
ATS Score =
60% Keyword Score +
40% Section Score
```

The system also identifies:

* Found keywords
* Missing keywords
* Missing sections
* Improvement suggestions

> Note: The ATS score is a project-specific heuristic score and should not be interpreted as the exact score used by commercial Applicant Tracking Systems.

---

# 🤖 Job Recommendation System

The system recommends job roles based on the technical skills detected in the resume.

Currently supported roles include:

* Python Developer
* Data Analyst
* Machine Learning Engineer
* AI Engineer
* Cloud Engineer

Each job role has a predefined set of required skills.

For example:

```text
Python Developer

Python
SQL
Flask
Git
```

The system calculates how many required skills are present in the resume.

---

# 🧠 NLP-Based Job Matching

The project also uses Natural Language Processing techniques for job matching.

The system uses:

* TF-IDF Vectorization
* Cosine Similarity

The resume text is compared with predefined job descriptions.

### TF-IDF

TF-IDF converts text into numerical vectors based on the importance of words.

### Cosine Similarity

Cosine similarity measures how similar the resume text is to a job description.

The result is converted into a percentage-based ML match score.

---

# 🔀 Hybrid Job Matching

The project combines two approaches:

### Rule-Based Skill Matching

Based on detected technical skills.

### NLP-Based Similarity Matching

Based on TF-IDF and cosine similarity.

The current hybrid score uses:

```text
Final Match Score =
50% Skill Match Score +
50% ML Match Score
```

This provides a combined indication of how closely a resume matches a particular job role.

---

# 📊 Resume Score

The project calculates an overall resume score using the average skill-match percentage across the supported job roles.

This score is intended as a project-level resume completeness/matching indicator.

It is **not a prediction of whether a candidate will get hired**.

---

# 🧩 Skill Gap Analysis

For every recommended job role, the system compares:

```text
Resume Skills
        +
Required Job Skills
        ↓
Missing Skills
```

For example:

```text
Job Role:
Machine Learning Engineer

Required:
Python
Machine Learning
Scikit-learn
Pandas
NumPy
TensorFlow

Missing:
TensorFlow
```

---

# 📚 Learning Recommendations

When a skill is missing, the system provides a learning recommendation.

Examples:

```text
Missing Skill → Recommendation

Python → Python Programming

SQL → SQL and Database Management

Machine Learning → Machine Learning

Docker → Docker and Containerization

AWS → AWS Cloud Computing
```

This helps users understand what they can learn to improve their job-role match.

---

# 👤 User Authentication

The application provides:

* User registration
* User login
* Password hashing
* Logout
* Session management

Passwords are stored using password hashing instead of storing plain-text passwords.

---

# 📜 Analysis History

Every authenticated user can view their previous resume analyses.

The history contains information such as:

* Resume name
* Resume score
* Section score
* Recommended job role
* Match score
* Missing skills

Each user's history is filtered using their user ID.

Therefore, users only see their own analysis history.

---

# 🗄️ Database

The project currently uses **SQLite**.

### Users Table

Stores:

```text
id
username
password
```

### Resume Analysis Table

Stores:

```text
id
user_id
resume_name
resume_score
section_score
skills
job_role
match_score
missing_skills
```

SQLite was selected initially because it is lightweight and easy to use during development.

---

# 🏗️ Project Architecture

```text
                    USER
                      │
                      ▼
              Upload Resume PDF
                      │
                      ▼
                Flask Backend
                      │
                      ▼
              PDF Text Extraction
                      │
                      ▼
              Extracted Resume Text
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Skill         ATS         Section
   Extraction    Analysis      Analysis
          │           │           │
          └───────────┼───────────┘
                      ▼
              Job Recommendation
                      │
              ┌───────┴────────┐
              ▼                ▼
       Rule-Based Match    NLP Matching
                              │
                       TF-IDF + Cosine
                              │
              ┌───────────────┘
              ▼
          Hybrid Score
              │
       ┌──────┴──────┐
       ▼             ▼
  Skill Gap     Learning
  Analysis    Recommendations
       │             │
       └──────┬──────┘
              ▼
        Web Dashboard
              │
              ▼
        Database History
```

---

# 📁 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
│
├── resume_analyzer.py
├── job_recommender.py
├── skill_gap.py
├── resume_score.py
├── learning_recommendation.py
├── job_matcher.py
├── resume_section_analyzer.py
├── ats_analyzer.py
│
├── database.py
├── auth.py
├── resume_analyzer.db
│
├── templates/
│   ├── index.html
│   ├── history.html
│   ├── login.html
│   └── register.html
│
├── static/
│
└── uploads/
```

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Backend

* Python
* Flask

## NLP / Machine Learning

* Scikit-learn
* TF-IDF
* Cosine Similarity

## PDF Processing

* PyPDF2

## Database

* SQLite

## Authentication

* Flask Sessions
* Werkzeug Password Hashing

---

# ⚙️ Installation

## Step 1: Install Python

Make sure Python is installed.

Check:

```bash
python --version
```

---

## Step 2: Install Required Libraries

Run:

```bash
python -m pip install flask pandas scikit-learn PyPDF2
```

---

## Step 3: Open the Project

Open the project folder in VS Code:

```text
AI_Resume_Analyzer
```

---

## Step 4: Run Flask Application

Run:

```bash
python app.py
```

If using a specific Python installation:

```bash
C:\Python314\python.exe app.py
```

---

## Step 5: Open the Application

Open the Flask URL shown in the terminal.

Usually:

```text
http://127.0.0.1:5000
```

---

# 🔄 Application Workflow

```text
1. User opens application
             ↓
2. User registers/logs in
             ↓
3. User uploads resume PDF
             ↓
4. Flask receives the PDF
             ↓
5. PyPDF2 extracts resume text
             ↓
6. Skills are detected
             ↓
7. Resume sections are analyzed
             ↓
8. ATS keywords are analyzed
             ↓
9. Job roles are matched
             ↓
10. TF-IDF similarity is calculated
             ↓
11. Hybrid score is generated
             ↓
12. Missing skills are identified
             ↓
13. Learning recommendations are generated
             ↓
14. Results are displayed on dashboard
             ↓
15. Analysis is stored in database
```

---

# 🔌 API Endpoint

## Resume Analysis API

### Endpoint

```text
POST /extract
```

### Request

The request contains a PDF resume uploaded using the `resume` form field.

### Response

The API returns information such as:

```json
{
    "message": "Resume processed successfully",
    "skills": [],
    "resume_score": 0,
    "section_score": 0,
    "sections": {},
    "job_recommendations": [],
    "ml_recommendations": [],
    "ats_analysis": {},
    "extracted_text": ""
}
```

---

# 📜 History API

### Endpoint

```text
GET /api/history
```

This endpoint returns the analysis history of the currently logged-in user.

---

# 🔐 Authentication Routes

### Register

```text
GET /register
POST /register
```

### Login

```text
GET /login
POST /login
```

### Logout

```text
GET /logout
```

---

# 🧮 Algorithms Used

## 1. Keyword Matching

The system searches the resume text for predefined technical skills.

---

## 2. Skill Match Percentage

The basic job match percentage is calculated using:

```text
Matched Skills
----------------------- × 100
Required Skills
```

---

## 3. TF-IDF

TF-IDF is used to convert resume and job-description text into numerical vectors.

---

## 4. Cosine Similarity

Cosine similarity is used to calculate textual similarity between:

```text
Resume
   ↕
Job Description
```

---

## 5. Hybrid Matching

The project combines:

```text
Rule-Based Skill Matching
+
NLP-Based Similarity Matching
```

to produce the final job match score.

---

# 📈 Dashboard

The dashboard provides a visual representation of the analysis.

It includes:

* Resume score
* Section score
* Detected skills
* Job recommendations
* Skill gaps
* ML matching results
* ATS analysis
* Charts
* Learning recommendations
* Analysis history

Chart.js is used for graphical visualization.

---

# 🔒 Security Considerations

The project includes basic security mechanisms:

* Password hashing
* Session-based authentication
* User-specific history
* Database parameterized queries

For production deployment, additional security improvements should be implemented.

---

# ⚠️ Current Limitations

The current version has some limitations:

1. Skill extraction is based on a predefined skill list.
2. ATS analysis uses heuristic keyword and section matching.
3. Job descriptions are manually defined.
4. TF-IDF matching is text similarity rather than a trained hiring model.
5. The hybrid score uses manually selected weights.
6. Resume score does not represent actual hiring probability.
7. PDF extraction may not work perfectly with scanned/image-only PDFs.
8. The current database is SQLite and is intended primarily for development.
9. The current application uses a development Flask configuration.

---

# 🔮 Future Scope

Future versions can include:

### Advanced NLP

* Named Entity Recognition
* Better skill extraction
* Skill aliases
* Context-aware skill detection
* spaCy integration
* Transformer-based NLP models

### Improved Job Recommendation

* Larger job dataset
* Real-world job descriptions
* More job categories
* Personalized recommendations
* Learning-based ranking

### Resume Improvement

* Resume grammar analysis
* Resume formatting analysis
* Bullet-point improvement
* Achievement detection
* Experience quality analysis

### Database

Migration from SQLite to:

```text
PostgreSQL
```

for production environments.

### Cloud Deployment

The application can be deployed using:

```text
AWS EC2
AWS S3
PostgreSQL
```

Possible cloud architecture:

```text
User
 ↓
AWS EC2
 ↓
Flask Application
 ├── NLP/ML
 ├── Database
 └── Resume Processing
       ↓
     AWS S3
```

---

# 🎓 Academic Value

This project demonstrates concepts from multiple areas of Computer Science:

* Web Development
* Python Programming
* Flask
* Database Management
* Natural Language Processing
* Machine Learning
* Information Retrieval
* Text Similarity
* Authentication
* API Development
* Data Analysis
* Cloud Computing

Therefore, the project can be extended into a complete final-year B.Tech CSE project.

---

# 👨‍💻 How the Project Works in Simple Words

The complete system can be explained in one sentence:

> **The user uploads a resume, the system extracts its text and skills, analyzes ATS compatibility, compares the resume with different job descriptions using NLP, identifies suitable roles and missing skills, and provides learning recommendations through a web dashboard.**

---

# 🧪 Example

Suppose a resume contains:

```text
Python
SQL
Flask
Machine Learning
Pandas
NumPy
Git
AWS
```

The system may detect:

```text
Skills:
Python
SQL
Flask
Machine Learning
Pandas
NumPy
Git
AWS
```

Then it compares these skills with job requirements.

For example:

```text
Python Developer
        ↓
Python ✓
SQL ✓
Flask ✓
Git ✓
        ↓
High Skill Match
```

For another role:

```text
Cloud Engineer
        ↓
AWS ✓
Python ✓
Git ✓
Docker ✗
        ↓
Docker identified as missing skill
```

The system can then provide:

```text
Missing Skill:
Docker

Learning Recommendation:
Docker and Containerization
```

---
# Deployed Link : 
https://ai-resume-analyzer-2-6584.onrender.com

# 📌 Disclaimer

This project is an academic/software engineering project.

The scores generated by the system are intended to demonstrate resume analysis, keyword matching, NLP similarity, and recommendation techniques.

They should not be treated as official ATS scores, hiring decisions, or guarantees of employment.

---

# 📄 License

This project is developed for educational and academic purposes.

You may modify and extend the project according to your requirements.
