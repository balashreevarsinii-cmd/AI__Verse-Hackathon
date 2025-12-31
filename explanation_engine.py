# explanation_engine.py
# Generates explanation-only content (non-diagnostic)

def generate_explanation(report_text: str) -> str:
    text = report_text.lower()
    explanations = []

    if "hb" in text or "hemoglobin" in text:
        explanations.append(
            "Hemoglobin helps carry oxygen throughout the body. "
            "Slight variations can occur due to diet, hydration, or fatigue."
        )

    if "cholesterol" in text:
        explanations.append(
            "Cholesterol levels are linked to heart health. "
            "They can be influenced by food habits and daily activity."
        )

    if "wbc" in text:
        explanations.append(
            "White blood cells support the immune system. "
            "Temporary changes may occur due to stress or minor infections."
        )

    if not explanations:
        explanations.append(
            "These report values may vary due to common lifestyle or temporary factors. "
            "A healthcare professional can provide detailed medical guidance."
        )

    return " ".join(explanations)
