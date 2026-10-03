def analyze_resume_sections(resume_text):

    text = resume_text.lower()

    sections = {

        "Education": False,
        "Experience": False,
        "Skills": False,
        "Projects": False,
        "Certifications": False

    }

    # ================= EDUCATION =================

    if (
        "education" in text
        or "academic" in text
        or "qualification" in text
    ):
        sections["Education"] = True


    # ================= EXPERIENCE =================

    if (
        "experience" in text
        or "work experience" in text
        or "employment" in text
        or "professional experience" in text
    ):
        sections["Experience"] = True


    # ================= SKILLS =================

    if (
        "skills" in text
        or "technical skills" in text
        or "technical skill" in text
        or "key skills" in text
    ):
        sections["Skills"] = True


    # ================= PROJECTS =================

    if (
        "projects" in text
        or "project" in text
        or "academic projects" in text
        or "personal projects" in text
    ):
        sections["Projects"] = True


    # ================= CERTIFICATIONS =================

    if (
        "certifications" in text
        or "certification" in text
        or "certificate" in text
        or "certificates" in text
    ):
        sections["Certifications"] = True


    # ================= COUNT SECTIONS =================

    total_sections = len(sections)

    available_sections = 0


    for section in sections:

        if sections[section]:

            available_sections += 1


    # ================= SECTION SCORE =================

    section_score = (
        available_sections / total_sections
    ) * 100


    # ================= SUGGESTIONS =================

    suggestions = []


    if not sections["Education"]:

        suggestions.append(
            "Add an Education section with your degree, college/university and graduation year."
        )


    if not sections["Experience"]:

        suggestions.append(
            "Add an Experience section with internships, work experience or relevant professional experience."
        )


    if not sections["Skills"]:

        suggestions.append(
            "Add a Skills section containing your technical and relevant professional skills."
        )


    if not sections["Projects"]:

        suggestions.append(
            "Add a Projects section with 2-3 relevant academic or personal projects."
        )


    if not sections["Certifications"]:

        suggestions.append(
            "Add a Certifications section if you have relevant courses or certifications."
        )


    # ================= RETURN RESULT =================

    return {

        "sections": sections,

        "section_score": round(
            section_score,
            2
        ),

        "suggestions": suggestions

    }