from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def score_candidate(jd, resume_text):
    prompt = f"""
You are a senior technical recruiter.

Job Description:
{jd}

Candidate Resume:
{resume_text}

Evaluate the candidate on:
1. Skill Match (0–40)
2. Experience Relevance (0–30)
3. Domain Fit (0–20)
4. Resume Clarity (0–10)

Return response in EXACT format:

Total Score: <number>/100
Decision: Hire / Maybe / Reject
Justification:
- point 1
- point 2
- point 3
"""

    response = llm.invoke(prompt)
    return response.content
