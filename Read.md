# 🩺 SafeGen-Health

**SafeGen-Health** is a safety-bounded Generative AI system designed to help
patients understand medical report values in simple, human-friendly language.
The system focuses strictly on explanation and health literacy and does not
perform diagnosis, disease prediction, or treatment recommendation.

---

## ❓ Problem Statement

Medical reports are written using technical terminology intended for healthcare
professionals. Patients often receive lab reports containing numerical values
without context, leading to confusion, anxiety, and unsafe self-diagnosis using
unverified online sources.

Existing digital tools either:
- Display only reference ranges without explanation, or
- Provide uncontrolled medical advice through chatbots.

There is a critical need for a **safe, non-diagnostic Generative AI system**
focused purely on patient understanding.

---

## 💡 Proposed Solution

SafeGen-Health uses a **constrained Generative AI pipeline** to convert medical
report values into simple explanations that:
- Describe what a parameter generally represents
- Explain why values may vary (non-clinical)
- Maintain a calm and reassuring tone

The system is **explicitly restricted** from generating diagnosis, disease names,
or medical advice.

---

## ⭐ Novelty of the Project

The novelty of SafeGen-Health lies in its **architecture**, not in prediction.

### Key Novel Contributions:
- **Safety-Bounded Generative AI**  
  AI generation is strictly constrained using a dedicated safety rule engine.

- **Explanation-Centric AI**  
  The system improves health literacy rather than automating medical decisions.

- **Ethics-by-Design Architecture**  
  Safety and ethics are implemented as independent software modules.

Unlike typical hackathon projects that use uncontrolled chatbots, this project
demonstrates how Generative AI can be responsibly deployed in healthcare.

---

## 🧠 System Pipeline

1. User inputs medical report values
2. Text preprocessing and parameter detection
3. Safety rule enforcement
4. Generative explanation creation
5. Disclaimer injection
6. Patient-friendly output display

---

## 🔒 Safety & Ethical Design

SafeGen-Health enforces multiple safety layers:
- Diagnosis-related keywords are blocked
- Treatment and medication advice is prohibited
- Mandatory disclaimers are displayed
- AI supports doctors but never replaces them

This design allows real-world deployment without ethical or legal risk.

---

## 🛠️ Tech Stack

- Python
- Streamlit (Web UI)
- Modular Generative Logic
- Rule-Based Safety Engine

---

## ▶️ How to Run the Prototype

```bash
pip install -r requirements.txt
streamlit run app.py

Hb: 11.5 g/dL
Cholesterol: 215 mg/dL
WBC: 6200 cells/mcL
