import streamlit as st
from explanation_engine import generate_explanation
from safety_rules import safety_check

st.set_page_config(page_title="SafeGen-Health", page_icon="🩺")

st.title("🩺 SafeGen-Health")
st.subheader("Patient-Friendly Medical Report Explanation")

st.warning(
    "⚠️ This system provides explanations only.\n"
    "It does NOT diagnose diseases or recommend treatments."
)

report_text = st.text_area(
    "Paste your medical report values:",
    placeholder="Example: Hb: 11.5 g/dL, Cholesterol: 210 mg/dL"
)

if st.button("Explain Report"):
    if report_text.strip() == "":
        st.error("Please enter medical report values.")
    else:
        explanation = generate_explanation(report_text)

        if safety_check(explanation):
            st.success("Explanation")
            st.write(explanation)
            st.info(
                "This explanation is for understanding only. "
                "Please consult a doctor for medical advice."
            )
        else:
            st.error("Unsafe content blocked by safety engine.")
