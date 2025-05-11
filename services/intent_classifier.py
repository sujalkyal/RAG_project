# File: services/intent_classifier.py
def classify_context(question: str) -> str:
    q = question.lower()
    if "compare" in q or "better" in q:
        return "compare"
    elif "interview" in q or "transcript" in q:
        return "interview"
    elif "job" in q or "company" in q or "compensation" in q:
        return "job"
    else:
        return "resume"
