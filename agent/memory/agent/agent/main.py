import os
from dotenv import load_dotenv
from agent.jd_analyzer import load_job_description
from agent.recruiter_agent import run_recruiter_agent

load_dotenv()

JD_PATH = "data/job_description.txt"
RESUME_PATH = "data/resumes/"

def main():
    print("\n🔍 AI Recruiter Screening Agent Started...\n")

    jd_text = load_job_description(JD_PATH)
    results = run_recruiter_agent(jd_text, RESUME_PATH)

    print("\n📊 Candidate Evaluation Results\n")
    print("=" * 50)

    for result in results:
        print(f"\nCandidate: {result['candidate']}")
        print(result["evaluation"])
        print("-" * 50)

if __name__ == "__main__":
    main()
