import streamlit as st
import pickle
import re
import base64

# Load model and vectorizer
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(page_title="Phishing Email Detector", page_icon="🛡️", layout="centered")

bg_image = get_base64("background.jpeg")
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .main-title {{
        text-align: center;
        color: #00BFFF;
        font-size: 42px;
        font-weight: bold;
    }}
    .quote {{
        text-align: center;
        font-style: italic;
        color: #AAAAAA;
        font-size: 18px;
        margin-bottom: 30px;
    }}
    .stButton button {{
        display: block;
        margin: 0 auto;
        width: 250px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }}
    .result-text {{
        font-size: 22px;
        font-weight: bold;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🛡️Phishing Email Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="quote">"Identify Malicious Emails Before They Become Threats."</div>', unsafe_allow_html=True)

st.write("Paste an email's content below to check if it's a phishing attempt.")

email_text = st.text_area("Email Content", height=200)

if st.button("🔍Analyze Email"):
    if email_text.strip() == "":
        st.warning("Please paste email content first.")
    else:
        cleaned = clean_text(email_text)
        vec = vectorizer.transform([cleaned])
        proba = model.predict_proba(vec)[0]
        phishing_score = proba[1] * 100

        if phishing_score < 40:
            st.markdown(f'<div class="result-text" style="color:#00C853;">✅ SAFE EMAIL<br>Phishing Risk: {phishing_score:.2f}%</div>', unsafe_allow_html=True)
        elif phishing_score < 70:
            st.markdown(f'<div class="result-text" style="color:#FFC107;">⚠️ SUSPICIOUS - MEDIUM RISK<br>Phishing Risk: {phishing_score:.2f}%</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-text" style="color:#FF4B4B;">🚨 HIGH RISK - PHISHING EMAIL<br>Phishing Risk: {phishing_score:.2f}%</div>', unsafe_allow_html=True)