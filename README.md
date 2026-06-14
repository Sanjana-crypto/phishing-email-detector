# 🛡️ Phishing Email Detector – SOC Triage Tool

🔗 **Live Demo**: [https://phishing-email-detector-kfgxepseyah4d8qi3w6fpx.streamlit.app/](https://phishing-email-detector-kfgxepseyah4d8qi3w6fpx.streamlit.app/)

A machine learning-based phishing email detection tool with a Streamlit web interface...

# 🛡️ Phishing Email Detector – SOC Triage Tool

A machine learning-based phishing email detection tool with a Streamlit web interface, built to assist SOC (Security Operations Center) analysts in triaging suspicious emails by classifying them as **Safe**, **Suspicious (Medium Risk)**, or **High-Risk Phishing** based on email content.

---

## 📌 Project Overview

Phishing emails are one of the most common attack vectors used in social engineering attacks. SOC L1 analysts spend significant time manually reviewing reported emails to determine whether they are malicious. This project automates that initial triage step using Natural Language Processing (NLP) and Machine Learning.

---

## ✨ Features

- Classifies email content into three risk levels:
  - ✅ **Safe Email**
  - ⚠️ **Suspicious – Medium Risk**
  - 🚨 **High Risk – Phishing Email**
- Displays a confidence percentage (phishing risk score)
- Simple, clean web interface built with Streamlit
- Trained on a real-world email dataset (~18,600 emails)

---

## 🧠 How It Works

1. **Dataset**: Email text data labeled as "Safe Email" or "Phishing Email"
2. **Preprocessing**: Lowercasing, removing numbers/punctuation, cleaning text
3. **Feature Extraction**: TF-IDF Vectorization (5000 features)
4. **Model**: Logistic Regression (with class balancing)
5. **Prediction**: Outputs phishing probability score, categorized into 3 risk levels

---

## 📊 Model Performance

- **Accuracy**: 96.5%
- **Phishing Recall**: 0.98
- **Precision (Phishing)**: 0.93

| Metric | Safe Email | Phishing Email |
|--------|-----------|-----------------|
| Precision | 0.99 | 0.93 |
| Recall | 0.95 | 0.98 |
| F1-score | 0.97 | 0.96 |

---

## 🖥️ Tech Stack

- **Python**
- **scikit-learn** (Logistic Regression, TF-IDF)
- **pandas** (data handling)
- **Streamlit** (web interface)

---

## ⚙️ How to Run Locally

1. Clone this repository
```bash
git clone https://github.com/Sanjana-crypto/phishing-email-detector.git
cd phishing-email-detector
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

---

## 🔐 SOC Relevance

Phishing emails are a primary vector for social engineering attacks, credential theft, and malware delivery. This tool replicates the **initial triage step** performed by SOC L1 analysts — quickly assessing reported emails to prioritize escalation. Automating this step helps reduce response time and analyst workload.

---

## 🚀 Future Improvements

- URL/domain reputation checking (e.g., VirusTotal API integration)
- Email header analysis (sender domain spoofing detection)
- Highlight suspicious keywords/phrases in the email
- Support for deep learning models (BERT-based classification)

---



## 📷 Demo Screenshots

### ✅ Safe Email
![Safe Email](Safe%20Email.png)

### ⚠️ Suspicious Email - Medium Risk
![Suspicious Email](Suspicious%20Email.png)

### 🚨 High Risk Phishing Email
![High Risk Email](High%20risk%20Email.png)
