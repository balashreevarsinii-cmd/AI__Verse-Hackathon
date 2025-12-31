# safety_rules.py
# This module enforces ethical boundaries on AI output

BLOCKED_TERMS = [
    "diagnosis", "diagnose", "disease", "condition",
    "treatment", "medicine", "drug", "dose",
    "prescription", "cure", "therapy"
]

def safety_check(text: str) -> bool:
    """
    Returns False if unsafe medical content is detected.
    This ensures the AI never performs diagnosis or treatment.
    """
    for term in BLOCKED_TERMS:
        if term in text.lower():
            return False
    return True
