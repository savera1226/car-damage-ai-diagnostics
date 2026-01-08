import streamlit as st
from model_helper import predict
import torch

st.set_page_config(page_title="AI Vehicle Damage Analysis", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stHeader { color: #00d4ff; }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #161b22;
        border-left: 5px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2555/2555013.png", width=100)
    st.title("Project Specs")
    st.info("""
    - **Model:** ResNet-50 (Fine-tuned)
    - **Dataset:** 2,378 proprietary images
    - **Accuracy:** 78.49%
    - **Classes:** 6 (Front/Rear Damage)
    """)

# --- MAIN INTERFACE ---
st.title("🚗 DeepLearning.AI: Car Damage Analysis")
st.write("Professional Diagnostic Tool for Insurance & Repair Assessments")

col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload Car Photo (JPG/PNG)", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Source Image", width='stretch')

with col2:
    if uploaded_file:
        image_path = "temp_file.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with col2:
            with st.spinner('AI Neural Engine Analyzing...'):
                # Now receiving two values from predict
                label, confidence = predict(image_path)
            st.markdown("### 📊 Diagnostic Result")
            st.write(f"**Detected:** {label}")

            # Add a progress bar to show confidence visually
            st.progress(confidence / 100)
            st.write(f"**Confidence:** {confidence:.2f}%")

            if confidence < 80:
                st.warning("⚠️ Low confidence detected. Manual inspection recommended.")
            else:
                st.success("✅ High-confidence prediction.")

            from fpdf import FPDF


            def generate_pdf_report(label, confidence):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 24)
                pdf.cell(200, 20, "Vehicle Damage Analysis Report", ln=True, align='C')

                pdf.set_font("Arial", '', 14)
                pdf.ln(10)
                pdf.cell(200, 10, f"Analysis Date: 2026-01-08", ln=True)
                pdf.cell(200, 10, f"Detected Damage: {label}", ln=True)
                pdf.cell(200, 10, f"AI Confidence Score: {confidence:.2f}%", ln=True)
                pdf.cell(200, 10, f"Model Architecture: ResNet-50 Neural Engine", ln=True)

                return pdf.output(dest='S').encode('latin-1')


            # Update your download button:
            st.download_button(
                label="📩 Download Official PDF Report",
                data=generate_pdf_report(label, confidence),
                file_name=f"Diagnostic_Report_{label}.pdf",
                mime="application/pdf"
            )