import os
from agent.resume_parser import load_resume
from agent.scorer import score_candidate

def run_recruiter_agent(jd_text, resume_folder):
    results = []

    for file in os.listdir(resume_folder):
        if file.endswith(".pdf"):
            path = os.path.join(resume_folder, file)
            resume_text = load_resume(path)

            evaluation = score_candidate(jd_text, resume_text)

            results.append({
                "candidate": file,
                "evaluation": evaluation
            })

    return results
