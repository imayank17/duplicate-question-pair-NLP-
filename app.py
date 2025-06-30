import streamlit as st
import helper
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Page setup
st.set_page_config(page_title="Duplicate Question Checker", layout="centered")

# Title and subheader
st.title("❓  Duplicate Question Checker")
st.subheader("🔍 Enter two questions to check if they mean the same")
st.markdown("---")

# Input fields
q1 = st.text_input("**Question 1**", placeholder="E.g. What is machine learning?")
q2 = st.text_input("**Question 2**", placeholder="E.g. what do you mean by machine learning?")

# Button and result
if st.button("🔎 Check for Duplicate"):
    if not q1.strip() or not q2.strip():
        st.warning("⚠️ Please enter both questions.")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.success("✅ These questions are  **duplicates**.")
        else:
            st.error("❌ These questions are **not duplicates**.")

# Sidebar with project info
with st.sidebar:
    st.header("📦 Project Info")
    st.markdown("""
    
    A Machine Learning-powered tool to check if two Quora questions mean the same thing.
    """)

    st.markdown("---")
    st.subheader("🛠️ Tech Stack")
    st.markdown("""
    - Python & Streamlit  
    - Scikit-learn, XGBoost  
    - NLP: Tokenization, BOW, Fuzzy Matching  
    """)

    st.markdown("---")
    st.subheader("💡 How It Works")
    st.markdown("""
    - Text cleaning and preprocessing  
    - Feature engineering (lengths, tokens, fuzzy scores)  
    - Bag-of-Words vectorization  
    - Prediction using XGBoost model  
    """)

    st.markdown("---")
    st.subheader("👨‍💻 About the Creator")
    st.markdown("""
    Made with ❤️ by **Mayank**  
    Connect on [LinkedIn](https://www.linkedin.com/in/mayank-kumar-367116293/)  
    View code on [GitHub](https://github.com/imayank17)
    """)

    st.markdown("---")
    st.caption("© 2025 | NLP Project")
